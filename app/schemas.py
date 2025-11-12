from pydantic import BaseModel
from datetime import datetime

class DocumentoBase(BaseModel):
    titulo: str
    tipo: str
    descricao: str
    status: str = "Pendente"

class DocumentoCreate(DocumentoBase):
    pass

class DocumentoUpdate(BaseModel):
    titulo: str | None = None
    tipo: str | None = None
    descricao: str | None = None
    status: str | None = None

class DocumentoOut(DocumentoBase):
    id: int
    criado_em: datetime

    class Config:
        orm_mode = True
