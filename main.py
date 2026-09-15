from fastapi import FastAPI

from app import crud, schemas


app = FastAPI(title="API Containerizada")


@app.get("/")
def inicio():
    return {"mensagem": "API funcionando!"}


@app.post("/tarefas", response_model=schemas.TarefaResponse)
def criar_tarefa(dados: schemas.TarefaCreate):
    return crud.criar_tarefa(
        dados.titulo,
        dados.descricao
    )


@app.get("/tarefas")
def listar_tarefas():
    return crud.listar_tarefas()