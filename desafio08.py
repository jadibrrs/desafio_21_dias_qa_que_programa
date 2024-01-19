def adicionar_tarefa_inicial(lista, tarefa_inicial):
    lista.append(tarefa_inicial)

def adicionar_tarefa(lista):
    tarefa = input("Digite a tarefa: ")
    lista.append(tarefa)

def remover_tarefa(lista):
    if not lista:
        print("A lista de tarefas está vazia.")
        return

    print("Selecione a tarefa que deseja remover: ")

    exibir_lista(lista)

    try:
        indice_remover = int(input("\nDigite o número da tarefa que deseja remover: "))
        if 1 <= indice_remover <= len(lista):
            lista.pop(indice_remover - 1)
            print("Tarefa removida com sucesso.")
        else:
            print("\Índice inválido. Tarefa não removida.")
    except ValueError:
        print("Entrada inválida. Certifique-se de digitar um número válido.")

def selecionar_acao():
    acao = int(input("\nSelecione uma ação: \n[1] Adicionar nova tarefa \n[2] Remover tarefa \n[3] Listar tarefas \n[4] Sair \n"))
    return acao

def exibir_lista(lista):
    print("\nLista de tarefas:")

    for i, tarefa in enumerate(lista, start=1):
            print(f"\n{i}.{tarefa}")

lista = []

entrada = input("\nSeja bem-vindo(a) à lista de tarefas! \nAdicione uma tarefa para iniciar: ")

adicionar_tarefa_inicial(lista, entrada)

exibir_lista(lista)

while True:
    acao = selecionar_acao()
    
    if acao == 1:
        adicionar_tarefa(lista)
    elif acao ==2: 
        remover_tarefa(lista)
    elif acao == 3:
        exibir_lista(lista)
    elif acao == 4:
        break
    else:
        print("Selecione uma ação válida.")