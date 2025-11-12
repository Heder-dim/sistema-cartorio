from pydantic import BaseModel
from datetime import datetime, date
from typing import List, Optional

class DocumentoBase(BaseModel):
    tipo_documento: str
    partes: List[str] = []
    situacao: Optional[str] = None
    formato: Optional[str] = None
    dados_livro: Optional[str] = None
    telefone_contato: Optional[str] = None
    data: Optional[date] = None
    justificativa_nao_conclusao: Optional[str] = None  # 👈 novo campo

class DocumentoCreate(DocumentoBase):
    pass

class DocumentoUpdate(BaseModel):
    tipo_documento: Optional[str] = None
    partes: Optional[List[str]] = None
    situacao: Optional[str] = None
    formato: Optional[str] = None
    dados_livro: Optional[str] = None
    telefone_contato: Optional[str] = None
    data: Optional[date] = None
    justificativa_nao_conclusao: Optional[str] = None  # 👈 novo campo

class DocumentoOut(DocumentoBase):
    id: int
    criado_em: datetime

    class Config:
        from_attributes = True  
