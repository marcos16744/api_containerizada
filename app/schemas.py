from pydantic import BaseModel


class TarefaCreate(BaseModel):
    titulo: str
    descricao: str


class TarefaResponse(BaseModel):
    titulo: str
    descricao: str



