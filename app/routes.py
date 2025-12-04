from datetime import date
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from app import database, models, schemas

router = APIRouter(prefix="/documentos", tags=["Documentos"])

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


# 🔹 Criar documento
@router.post("/", response_model=schemas.DocumentoOut)
def criar_documento(doc: schemas.DocumentoCreate, db: Session = Depends(get_db)):
    novo_doc = models.Documento(
        tipo_documento=doc.tipo_documento,
        partes=",".join(doc.partes),
        situacao=doc.situacao,
        formato=doc.formato,
        dados_livro=doc.dados_livro,
        telefone_contato=doc.telefone_contato,
        data=doc.data or None, 
        justificativa_nao_conclusao=doc.justificativa_nao_conclusao
    )
    db.add(novo_doc)
    db.commit()
    db.refresh(novo_doc)
    novo_doc.partes = novo_doc.partes.split(",") if novo_doc.partes else []
    return novo_doc


# 🔹 Listar documentos (com filtro opcional)
@router.get("/", response_model=list[schemas.DocumentoOut])
def listar_documentos(
    situacao: str | None = Query(default=None, description="Filtrar por situação"),
    data: date | None = Query(default=None, description="Filtrar por data (YYYY-MM-DD)"),
    db: Session = Depends(get_db)
):
    query = db.query(models.Documento)

    # filtro por situação, se informado
    if situacao:
        query = query.filter(models.Documento.situacao == situacao)

    # filtro por data, se informado
    if data:
        query = query.filter(models.Documento.data == data)

    docs = query.all()
    for d in docs:
        d.partes = d.partes.split(",") if d.partes else []
    return docs


# 🔹 Visualizar documento por ID
@router.get("/{id}", response_model=schemas.DocumentoOut)
def obter_documento(id: int, db: Session = Depends(get_db)):
    doc = db.query(models.Documento).filter(models.Documento.id == id).first()
    if not doc:
        raise HTTPException(status_code=404, detail="Documento não encontrado")
    doc.partes = doc.partes.split(",") if doc.partes else []
    return doc


# 🔹 Atualizar documento
@router.put("/{id}", response_model=schemas.DocumentoOut)
def atualizar_documento(id: int, dados: schemas.DocumentoUpdate, db: Session = Depends(get_db)):
    doc = db.query(models.Documento).filter(models.Documento.id == id).first()
    if not doc:
        raise HTTPException(status_code=404, detail="Documento não encontrado")

    data = dados.dict(exclude_unset=True)
    if "partes" in data and data["partes"] is not None:
        data["partes"] = ",".join(data["partes"])

    for campo, valor in data.items():
        setattr(doc, campo, valor)

    db.commit()
    db.refresh(doc)
    doc.partes = doc.partes.split(",") if doc.partes else []
    return doc


# 🔹 Excluir documento
@router.delete("/{id}")
def deletar_documento(id: int, db: Session = Depends(get_db)):
    doc = db.query(models.Documento).filter(models.Documento.id == id).first()
    if not doc:
        raise HTTPException(status_code=404, detail="Documento não encontrado")
    db.delete(doc)
    db.commit()
    return {"mensagem": "Documento removido com sucesso"}
