import os
from fastapi import FastAPI, Request, BackgroundTasks, Depends
from sqlalchemy.orm import Session
from datetime import datetime
import json

# Önceki fazlarda yazdığımız dosyaları içeri aktarıyoruz
from database import get_db, log_call, create_patient_if_not_exists, add_appointment
from orchestrator import AIAgentOrchestrator

app = FastAPI(title="Disci AI Voice Gateway")
orchestrator = AIAgentOrchestrator()

# --- VAPI.AI WEBHOOK YAPILANDIRMASI ---

@app.post("/vapi-webhook")
async def vapi_webhook(request: Request, db: Session = Depends(get_db)):
    """
    Vapi.ai'den gelen tüm olayları (Arama başladı, kullanıcı konuştu, arama bitti) dinler.
    """
    payload = await request.json()
    event_type = payload.get("message", {}).get("type")

    # 1. SENARYO: Arama Başladı (Selamlama)
    if event_type == "conversation-start":
        # Gemini 1.5 Flash ile hızlı selamlama al
        greeting = await orchestrator.get_initial_greeting()
        return {
            "message": {
                "type": "conversation-update",
                "content": greeting,
                "voice": "eleven-labs/kore" # Profesyonel bir ses seçimi
            }
        }

    # 2. SENARYO: Kullanıcı Konuştu (Anlık Karar)
    elif event_type == "user-interruption" or event_type == "model-output-incomplete":
        # Burada asenkron olarak orkestratör devreye girer
        user_input = payload.get("message", {}).get("transcript", "")
        # Örn: "Dişim çok ağrıyor" -> GPT-4o Denetimi -> Transfer Kararı
        decision = await orchestrator.route_call(user_input, {"slots": ["10:00", "14:30"]})
        
        if decision["action"] == "TRANSFER":
            return {
                "message": {
                    "type": "transfer-call",
                    "destination": "+905XXXXXXXXX", # Gerçek resepsiyon numarası
                    "summary": "Hasta acil ağrı şikayetiyle bağlandı."
                }
            }
        
        return {
            "message": {
                "type": "conversation-update",
                "content": decision["message"]
            }
        }

    # 3. SENARYO: Arama Bitti (Kayıt ve Analiz)
    elif event_type == "end-of-call-report":
        # Görüşme özetini ve transkripti veritabanına kaydet
        call_data = payload.get("message", {})
        transcript = call_data.get("transcript", "")
        summary = call_data.get("summary", "Özet çıkarılamadı.")
        phone = call_data.get("customer", {}).get("number", "Unknown")
        
        # Arka planda hastayı bul/oluştur ve görüşmeyi logla
        patient = create_patient_if_not_exists(db, phone, "Bilinmeyen Hasta")
        log_call(db, patient.id, transcript, summary, "Analiz Ediliyor", False)
        
        return {"status": "recorded"}

    return {"status": "ignored"}

# --- MANUEL RANDEVU OLUŞTURMA API (AI İÇİN) ---

@app.post("/create-appointment")
async def api_create_appointment(data: dict, db: Session = Depends(get_db)):
    """
    AI, kullanıcıdan onay aldığında bu endpoint'i çağırır (Function Calling).
    """
    patient_id = data.get("patient_id")
    time_str = data.get("time") # "2023-10-25 14:30"
    procedure = data.get("procedure")
    
    dt_object = datetime.strptime(time_str, "%Y-%m-%d %H:%M")
    new_apt = add_appointment(db, patient_id, dt_object, procedure)
    
    return {"status": "success", "appointment_id": new_apt.id}

if __name__ == "__main__":
    import uvicorn
    # Uygulamayı dış dünyaya açmak için (ngrok vb. gereklidir)
    uvicorn.run(app, host="0.0.0.0", port=8000)

