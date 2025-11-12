from sqlalchemy import Column, Integer, String, DateTime, Text, Date
from datetime import datetime
from app.database import Base


class Documento(Base):
    __tablename__ = "documentos"

    id = Column(Integer, primary_key=True, index=True)
    tipo_documento = Column(String, nullable=False)
    partes = Column(String)  # nomes separados por vírgula
    situacao = Column(String)
    formato = Column(String)
    data = Column(Date, nullable=True)
    dados_livro = Column(Text)
    justificativa_nao_conclusao = Column(Text, nullable=True)  # 👈 novo campo opcional
    telefone_contato = Column(String)
    criado_em = Column(DateTime, default=datetime.utcnow)
