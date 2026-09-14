from .models import Tarefa


tarefas = []


def criar_tarefa(titulo: str, descricao: str):
    nova_tarefa = Tarefa(titulo, descricao)

    tarefas.append(nova_tarefa)

    return nova_tarefa


def listar_tarefas():
    return tarefas