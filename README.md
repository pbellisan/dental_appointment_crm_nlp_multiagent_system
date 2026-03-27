Dişçi AI: Çoklu Ajan (Multi-Agent) Randevu & CRM Sistemi
Bu proje, diş kliniklerine gelen aramaları AI (Yapay Zeka) ile karşılayan, hastalarla doğal dilde konuşarak randevu oluşturan ve tüm süreci bir CRM paneli üzerinden yöneten uçtan uca bir çözümdür.
🚀 Proje Vizyonu
Sadece bir bot değil, kliniğin dijital resepsiyonisti olarak çalışan; Gemini 1.5 Flash, Claude 3.5 Sonnet ve GPT-4o modellerini hibrit (multi-agent) bir yapıda kullanarak maliyet ve hızı optimize eden bir sistem.
🏗️ Teknik Mimari (Tech Stack)
Bileşen
Teknoloji
Görev
Backend
Python / FastAPI
API ve İş Mantığı
Orchestrator
LangGraph / CrewAI
Model Seçimi ve Ajan Yönetimi
Ses (STT/TTS)
Deepgram / ElevenLabs
Ses-Metin Dönüşümü ve Ses Üretimi
Frontend
Reflex (Python-based React)
CRM Dashboard & Yönetim
Veritabanı
PostgreSQL
Hasta Kayıtları ve Randevu Takibi
Telefon Entegrasyonu
Vapi.ai / Twilio
Hat Bağlantısı ve Webhook

📋 Adım Adım Geliştirme Planı (To-Do List)
Faz 1: Temel Altyapı ve Veritabanı
• [ ] PostgreSQL veritabanı şemasının tasarlanması (patients, appointments, call_logs).
• [ ] SQLAlchemy / SQLModel ile Python modellerinin oluşturulması.
• [ ] Temel FastAPI projesinin ayağa kaldırılması.
Faz 2: Multi-Agent Orkestrasyonu
• [ ] Ajan 1 (Karşılayıcı): Gemini 1.5 Flash ile hızlı yanıt sistemi.
• [ ] Ajan 2 (Planlayıcı): Claude 3.5 Sonnet ile takvim ve kural yönetimi.
• [ ] Ajan 3 (Denetçi): GPT-4o ile sentiment analizi ve resepsiyona aktarma kararı.
• [ ] Ajanlar arası veri transferi mantığının kurulması.
Faz 3: Ses Entegrasyonu (Voice AI)
• [ ] Vapi.ai veya Retell AI üzerinden telefon hattı yapılandırması.
• [ ] Gecikme (latency) optimizasyonu için STT ve TTS akışlarının ayarlanması.
• [ ] Fonksiyon Çağrıları (Function Calling): AI'nın doğrudan veritabanına randevu yazabilmesi.
Faz 4: CRM Dashboard (Frontend)
• [ ] Reflex ile admin paneli arayüzü tasarımı.
• [ ] Canlı arama izleme ekranı.
• [ ] Randevu takvimi ve hasta yönetimi modülleri.
Faz 5: Test ve Yayına Alma
• [ ] Uçtan uca telefon testleri.
• [ ] Token tüketimi ve maliyet analizi dashboard'u.
• [ ] Dockerize ederek cloud (AWS/GCP) kurulumuna hazır hale getirme.
🛠️ Kurulum Notları
Geliştirme aşamasında buraya bağımlılıklar ve ortam değişkenleri eklenecektir.
👨‍💻 Katkıda Bulunma
Bu proje şu an geliştirme aşamasındadır. Adım adım ilerlemek için To-Do listesini takip ediniz.
