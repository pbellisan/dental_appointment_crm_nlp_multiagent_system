# dental_appointment_crm_nlp_multiagent_system

##📋 Adım Adım Geliştirme Planı (To-Do List)
#Faz 1: Temel Altyapı ve Veritabanı
• [ ] PostgreSQL veritabanı şemasının tasarlanması (patients, appointments, call_logs).
• [ ] SQLAlchemy / SQLModel ile Python modellerinin oluşturulması.
• [ ] Temel FastAPI projesinin ayağa kaldırılması.
#Faz 2: Multi-Agent Orkestrasyonu
• [ ] Ajan 1 (Karşılayıcı): Gemini 1.5 Flash ile hızlı yanıt sistemi.
• [ ] Ajan 2 (Planlayıcı): Claude 3.5 Sonnet ile takvim ve kural yönetimi.
• [ ] Ajan 3 (Denetçi): GPT-4o ile sentiment analizi ve resepsiyona aktarma kararı.
• [ ] Ajanlar arası veri transferi mantığının kurulması.
#Faz 3: Ses Entegrasyonu (Voice AI)
• [ ] Vapi.ai veya Retell AI üzerinden telefon hattı yapılandırması.
• [ ] Gecikme (latency) optimizasyonu için STT ve TTS akışlarının ayarlanması.
• [ ] Fonksiyon Çağrıları (Function Calling): AI'nın doğrudan veritabanına randevu yazabilmesi.
#Faz 4: CRM Dashboard (Frontend)
• [ ] Reflex ile admin paneli arayüzü tasarımı.
• [ ] Canlı arama izleme ekranı.
• [ ] Randevu takvimi ve hasta yönetimi modülleri.
#Faz 5: Test ve Yayına Alma
• [ ] Uçtan uca telefon testleri.
• [ ] Token tüketimi ve maliyet analizi dashboard'u.
• [ ] Dockerize ederek cloud (AWS/GCP) kurulumuna hazır hale getirme.
🛠️ Kurulum Notları
Geliştirme aşamasında buraya bağımlılıklar ve ortam değişkenleri eklenecektir.
