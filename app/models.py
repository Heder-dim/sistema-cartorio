from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from app.database import Base

class Documento(Base):
    __tablename__ = "documentos"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String, index=True)
    tipo = Column(String)
    descricao = Column(String)
    status = Column(String, default="Pendente")
    criado_em = Column(DateTime, default=datetime.utcnow)
