from fastapi import FastAPI

app = FastAPI()

TAREFAS = [
{"id": 1, "titulo" : "comprar ovos"},
{"id": 2, "titulo": "comprar sabonete"}

]

@app.get('/tarefas')
def listar():
    return TAREFAS

@app.post('/Adicionar-Nova-Tarefas')
def Adicionar(NovaTarefa):
    NovaTarefa = "nova tarefa"

@app.delete('/Concluir-Tarefas')
def Adicionar(NovaTarefa):
    NovaTarefa = "Excluir"