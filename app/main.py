from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from app import crud, schemas
from app.database import Base, engine, get_db

Base.metadata.create_all(bind=engine)

app = FastAPI(title="API Containerizada")


@app.get("/")
def inicio():
    return {"mensagem": "API funcionando!"}


@app.post("/tarefas", response_model=schemas.TarefaResponse)
def criar_tarefa(
    dados: schemas.TarefaCreate,
    db: Session = Depends(get_db)
):
    return crud.criar_tarefa(
        db,
        dados.titulo,
        dados.descricao
    )


@app.get("/tarefas", response_model=list[schemas.TarefaResponse])
def listar_tarefas(db: Session = Depends(get_db)):
    return crud.listar_tarefas(db)