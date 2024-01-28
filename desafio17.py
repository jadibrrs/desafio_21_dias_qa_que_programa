import csv
from datetime import datetime

def criar_arquivo():
    with open('despesas_pessoais.csv', 'w', newline='') as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow(['Despesa', 'Valor', 'Categoria', 'Data'])

def adicionar_despesa(despesa, valor, categoria, data):
    with open('despesas_pessoais.csv', 'a', newline='') as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow([despesa, valor, categoria, data])

def remover_despesa(despesa):
    nova_lista = []
    with open('despesas_pessoais.csv', 'r', newline='') as arquivo:
        lista_de_despesas = csv.reader(arquivo)
        for linha in lista_de_despesas:
            if linha[0] != despesa:
                nova_lista.append(linha)

    with open('despesas_pessoais.csv', 'w', newline='') as arquivo:
        escritor = csv.writer(arquivo)
        for linha in nova_lista:
            escritor.writerow(linha)

def listar_categorias(lista_de_despesas):
    lista_de_categorias = []

    for linha in lista_de_despesas:
        if linha[0] != 'Despesa': 
            if linha[2] not in lista_de_categorias:
                lista_de_categorias.append(linha[2])
    print(f'Categorias: {lista_de_categorias}')

def listar_despesas():
    with open('despesas_pessoais.csv', 'r') as arquivo:
        lista_de_despesas = list(csv.reader(arquivo))
        total = 0.00

        print("Opções: \n[1] Listar todas as despesas \n[2] Listar por categoria \n[3] Listar por data\n")
        listar = int(input("Digite a opção desejada: "))
        
        if listar == 1:
            print("\n------ Lista de Despesas ------")
            for linha in lista_de_despesas:
                if linha[0] != 'Despesa':             
                    print(f'Despesa: {linha[0]}, Valor: R$ {linha[1]}, Categoria: {linha[2]}, Data: {linha[3]}')
                    total += float(linha[1])

        if listar == 2:
            listar_categorias(lista_de_despesas)

            categoria_input = input("Digite o nome da categoria: ")
            print(f'Categoria selecionada: {categoria_input}')

            print("\n------ Lista de Despesas ------")
            for linha in lista_de_despesas:
                if linha[2] == categoria_input:             
                    print(f'Despesa: {linha[0]}, Valor: R$ {linha[1]}, Categoria: {linha[2]}, Data: {linha[3]}')
                    total += float(linha[1])

        if listar == 3:
            data_input = input("Digite a data no formato (dd/mm/aaaa): ")
            print(f'Data selecionada: {data_input}')

            print("\n------ Lista de Despesas ------")
            for linha in lista_de_despesas:
                if linha[3] == data_input:           
                    print(f'Despesa: {linha[0]}, Valor: R$ {linha[1]}, Categoria: {linha[2]}, Data: {linha[3]}')
                    total += float(linha[1])

        print(f'Total: R$ {total}')

def menu():
    print("\n########## Menu ##########\n1. Adicionar despesa\n2. Listar despesas\n3. Remover despesa\n4. Sair")

try:
    livro = open('despesas_pessoais.csv', 'r')
    livro.close()
except FileNotFoundError:
    criar_arquivo()

while True:
    menu()
    opcao = int(input("\nEscolha uma opção (1, 2, 3 ou 4): "))

    if opcao == 1:
        despesa = input("\nDigite o nome da despesa: ")
        valor = float(input("Digite o valor da despesa: R$ "))
        categoria = input("Digite a categoria da despesa: ")

        data = input("Digite a data no formato (dd/mm/aaaa): ")
        
        adicionar_despesa(despesa, valor, categoria, data)
        print("\nDespesa adicionada com sucesso!")
    elif opcao == 2:
        listar_despesas()
    elif opcao == 3:
        despesa = input("\nDigite o nome da despesa que deseja remover: ")
        remover_despesa(despesa)
        print("\nDespesa removida com sucesso!")
    elif opcao == 4:
        print("\nSaindo do programa. Até mais!")
        break
    else:
        print("\nOpção inválida. Por favor, escolha 1, 2, 3 ou 4.")