from sqlalchemy.orm import Session

from app.models import Tarefa


def criar_tarefa(db: Session, titulo: str, descricao: str):
    nova_tarefa = Tarefa(
        titulo=titulo,
        descricao=descricao
    )

    db.add(nova_tarefa)
    db.commit()
    db.refresh(nova_tarefa)

    return nova_tarefa


def listar_tarefas(db: Session):
    return db.query(Tarefa).all()