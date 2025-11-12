from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import database, models, schemas

router = APIRouter(prefix="/documentos", tags=["Documentos"])

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Criar documento
@router.post("/", response_model=schemas.DocumentoOut)
def criar_documento(doc: schemas.DocumentoCreate, db: Session = Depends(get_db)):
    novo_doc = models.Documento(**doc.dict())
    db.add(novo_doc)
    db.commit()
    db.refresh(novo_doc)
    return novo_doc

# Listar todos
@router.get("/", response_model=list[schemas.DocumentoOut])
def listar_documentos(db: Session = Depends(get_db)):
    return db.query(models.Documento).all()

# Visualizar documento
@router.get("/{id}", response_model=schemas.DocumentoOut)
def obter_documento(id: int, db: Session = Depends(get_db)):
    doc = db.query(models.Documento).filter(models.Documento.id == id).first()
    if not doc:
        raise HTTPException(status_code=404, detail="Documento não encontrado")
    return doc

# Editar documento
@router.put("/{id}", response_model=schemas.DocumentoOut)
def atualizar_documento(id: int, dados: schemas.DocumentoUpdate, db: Session = Depends(get_db)):
    doc = db.query(models.Documento).filter(models.Documento.id == id).first()
    if not doc:
        raise HTTPException(status_code=404, detail="Documento não encontrado")

    for campo, valor in dados.dict(exclude_unset=True).items():
        setattr(doc, campo, valor)

    db.commit()
    db.refresh(doc)
    return doc

# Excluir documento
@router.delete("/{id}")
def deletar_documento(id: int, db: Session = Depends(get_db)):
    doc = db.query(models.Documento).filter(models.Documento.id == id).first()
    if not doc:
        raise HTTPException(status_code=404, detail="Documento não encontrado")
    db.delete(doc)
    db.commit()
    return {"mensagem": "Documento removido com sucesso"}
