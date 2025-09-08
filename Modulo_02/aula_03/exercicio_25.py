"""25. Gerenciamento de Tarefas: Crie um dicionário para gerenciar tarefas. As chaves são os
nomes das tarefas, e os valores são listas de status (ex: ["pendente", "em andamento",
"concluído"]). Peça ao usuário para adicionar uma tarefa e seu status. Depois, imprima"""


tarefas = {
    "Estudar Python": ["em andamento"],
    "Limpar quarto": ["pendente"]
}

nome_tarefa = input("Digite o nome da tarefa: ")
status_tarefa = input("Digite os status da tarefa: ")

lista_status = [s.strip() for s in status_tarefa.split(",")]

tarefas[nome_tarefa] = lista_status

print("\nTarefas atuais:")
for tarefa, status in tarefas.items():
    print(f"{tarefa}: {status}")