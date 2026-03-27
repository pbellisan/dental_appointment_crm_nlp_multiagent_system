import os
from datetime import datetime
from typing import List, Optional

# SQLAlchemy bileşenleri
from sqlalchemy import create_engine, Column, Integer, String, DateTime, Text, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, Session

# Veritabanı URL'si (Yerel PostgreSQL veya Docker için yapılandırma)
# Format: postgresql://user:password@localhost:5432/db_name
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:password@localhost:5432/disci_ai")

# SQLAlchemy Kurulumu
Base = declarative_base()
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# --- VERİ MODELLERİ (TABLES) ---

class Patient(Base):
    """Hasta bilgilerinin saklandığı ana tablo"""
    __tablename__ = "patients"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String(100), nullable=False)
    phone_number = Column(String(20), unique=True, index=True, nullable=False)
    medical_history = Column(Text, nullable=True) # Alerjiler, eski işlemler vb.
    created_at = Column(DateTime, default=datetime.utcnow)

    # İlişkiler
    appointments = relationship("Appointment", back_populates="patient")
    call_logs = relationship("CallLog", back_populates="patient")

class Appointment(Base):
    """Randevu kayıtları tablosu"""
    __tablename__ = "appointments"

    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer, ForeignKey("patients.id"))
    appointment_time = Column(DateTime, nullable=False)
    procedure_type = Column(String(100)) # Örn: Dolgu, Diş Çekimi
    status = Column(String(50), default="Beklemede") # Beklemede, Onaylandı, İptal
    notes = Column(Text)
    
    patient = relationship("Patient", back_populates="appointments")

class CallLog(Base):
    """AI ile yapılan telefon görüşmelerinin detayları"""
    __tablename__ = "call_logs"

    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer, ForeignKey("patients.id"), nullable=True)
    call_start = Column(DateTime, default=datetime.utcnow)
    transcript = Column(Text) # Tüm görüşme metni
    summary = Column(Text) # AI tarafından oluşturulan kısa özet
    sentiment = Column(String(50)) # Duygu durumu (Pozitif, Öfkeli, Acil)
    is_transferred = Column(Boolean, default=False) # Operatöre aktarıldı mı?
    
    patient = relationship("Patient", back_populates="call_logs")

# --- VERİTABANI İŞLEMLERİ (CRUD) ---

def init_db():
    """Tabloları veritabanında oluşturur"""
    Base.metadata.create_all(bind=engine)

def get_db():
    """Veritabanı oturumu oluşturur"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# AI Ajanlarının kullanacağı yardımcı fonksiyonlar
def create_patient_if_not_exists(db: Session, phone: str, name: str):
    """Hastayı telefon numarasına göre bulur veya yeni kayıt açar"""
    patient = db.query(Patient).filter(Patient.phone_number == phone).first()
    if not patient:
        patient = Patient(full_name=name, phone_number=phone)
        db.add(patient)
        db.commit()
        db.refresh(patient)
    return patient

def add_appointment(db: Session, patient_id: int, time: datetime, procedure: str):
    """Yeni bir randevu kaydı oluşturur"""
    new_apt = Appointment(
        patient_id=patient_id,
        appointment_time=time,
        procedure_type=procedure,
        status="Onaylandı"
    )
    db.add(new_apt)
    db.commit()
    db.refresh(new_apt)
    return new_apt

def log_call(db: Session, patient_id: Optional[int], transcript: str, summary: str, sentiment: str, transferred: bool):
    """Görüşme detaylarını kaydeder"""
    log = CallLog(
        patient_id=patient_id,
        transcript=transcript,
        summary=summary,
        sentiment=sentiment,
        is_transferred=transferred
    )
    db.add(log)
    db.commit()
    return log

if __name__ == "__main__":
    # Dosya doğrudan çalıştırıldığında tabloları oluşturur
    print("Veritabanı tabloları oluşturuluyor...")
    init_db()
    print("İşlem tamamlandı.")

