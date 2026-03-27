import os
import json
from datetime import datetime
from typing import Dict, Any, Optional

# Mock API Çağrıları (Gerçek kütüphanelerle -google-generativeai, anthropic, openai- değiştirilecektir)
class AIAgentOrchestrator:
    def __init__(self):
        self.api_keys = {
            "gemini": os.getenv("GEMINI_API_KEY", ""),
            "claude": os.getenv("ANTHROPIC_API_KEY", ""),
            "openai": os.getenv("OPENAI_API_KEY", "")
        }

    async def get_initial_greeting(self, patient_name: Optional[str] = None) -> str:
        """
        MODEL: Gemini 1.5 Flash (Düşük Gecikme)
        Görevi: Aramayı hızlıca karşılamak.
        """
        name_part = f" {patient_name}" if patient_name else ""
        # Burada Gemini API çağrısı simüle ediliyor
        return f"Merhaba{name_part}, Diş Kliniğimize hoş geldiniz. Ben dijital asistanınızım. Size nasıl yardımcı olabilirim?"

    async def analyze_sentiment_and_urgency(self, user_input: str) -> Dict[str, Any]:
        """
        MODEL: GPT-4o (Yüksek Denetim Gücü)
        Görevi: Kullanıcının aciliyet durumunu ve duygusunu ölçmek.
        """
        # Prompt: "Kullanıcı girdisini analiz et: Acil mi? Duygu durumu ne? Resepsiyona aktarılmalı mı?"
        # Örnek Çıktı: {"urgency": "high", "transfer": True, "reason": "Severe pain"}
        
        urgency_keywords = ["ağrı", "kanama", "şiddetli", "dayanamıyorum", "acil"]
        is_urgent = any(word in user_input.lower() for word in urgency_keywords)
        
        return {
            "is_urgent": is_urgent,
            "sentiment": "Anxious" if is_urgent else "Neutral",
            "should_transfer": is_urgent
        }

    async def manage_appointment_logic(self, user_request: str, available_slots: list) -> Dict[str, Any]:
        """
        MODEL: Claude 3.5 Sonnet (Üstün Muhakeme)
        Görevi: Takvimi kontrol edip en uygun randevuyu önermek.
        """
        # Claude burada karmaşık kuralları (Örn: Dolgu 45dk, Kanal 90dk sürer) yönetir.
        # Prompt: "Kullanıcı 'Salı öğleden sonra' diyor. Mevcut boşluklar: [...]. En iyi saati seç."
        
        return {
            "suggested_time": "2023-10-25T14:30:00",
            "procedure": "Genel Kontrol",
            "confidence_score": 0.95
        }

    async def route_call(self, user_input: str, context: Dict[str, Any]):
        """
        Ana Orkestrasyon Mantığı:
        Girdiyi alır, modellere dağıtır ve nihai aksiyonu belirler.
        """
        # 1. Adım: GPT-4o ile güvenliği kontrol et
        safety_check = await self.analyze_sentiment_and_urgency(user_input)
        
        if safety_check["should_transfer"]:
            return {
                "action": "TRANSFER",
                "target": "Receptionist",
                "message": "Durumunuzun aciliyetini anlıyorum, sizi hemen resepsiyona bağlıyorum."
            }
        
        # 2. Adım: Claude ile randevu detaylarını planla
        appointment_plan = await self.manage_appointment_logic(user_input, context.get("slots", []))
        
        return {
            "action": "CONFIRM_APPOINTMENT",
            "details": appointment_plan,
            "message": f"Anlıyorum. Sizin için {appointment_plan['suggested_time']} saatine randevu oluşturuyorum. Onaylıyor musunuz?"
        }

# --- KULLANIM ÖRNEĞİ (Simülasyon) ---
async def test_run():
    orchestrator = AIAgentOrchestrator()
    
    # Durum 1: Normal Randevu İsteği
    print("--- SENARYO 1: NORMAL ---")
    res1 = await orchestrator.route_call("Yarın öğleden sonra bir kontrol için gelebilir miyim?", {"slots": ["14:00", "15:00"]})
    print(f"AI Kararı: {res1['action']} - Mesaj: {res1['message']}")

    # Durum 2: Acil Durum
    print("\n--- SENARYO 2: ACİL ---")
    res2 = await orchestrator.route_call("Dişim çok şiddetli ağrıyor, duramıyorum!", {})
    print(f"AI Kararı: {res2['action']} - Mesaj: {res2['message']}")

if __name__ == "__main__":
    import asyncio
    asyncio.run(test_run())

