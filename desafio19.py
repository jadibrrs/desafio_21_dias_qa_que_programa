import csv

def criar_arquivo():
    with open('agenda_de_contatos.csv', 'w', newline='') as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow(['Nome', 'Número de Telefone', 'E-mail'])

def adicionar_contato(nome, telefone, email):
    with open('agenda_de_contatos.csv', 'a', newline='') as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow([nome, telefone, email])

def excluir_contato(nome):
    nova_lista = []
    contato_encontrado = False
    with open('agenda_de_contatos.csv', 'r', newline='') as arquivo:
        agenda_de_contatos = csv.reader(arquivo)
        for linha in agenda_de_contatos:
            if linha[0] != nome:
                nova_lista.append(linha)
            else:
                contato_encontrado = True
    
    with open('agenda_de_contatos.csv', 'w', newline='') as arquivo:
        escritor = csv.writer(arquivo)
        for linha in nova_lista:
            escritor.writerow(linha)

    if contato_encontrado:
        print("\nContato removido com sucesso!")
    else:
        print(f'\nContato "{nome}" não encontrado na agenda.')

def listar_contatos():
    with open('agenda_de_contatos.csv', 'r') as arquivo:
        agenda_de_contatos = list(csv.reader(arquivo))

        print('\n------ Agenda de Contatos ------\n')
        for linha in agenda_de_contatos:
            if linha[0] != 'Nome':
                print(f'Nome: {linha[0]}\nNúmero de telefone: {linha[1]}\nE-mail: {linha[2]}\n\n')

def buscar_contato():
    with open('agenda_de_contatos.csv', 'r') as arquivo:
        agenda_de_contatos = list(csv.reader(arquivo))

        contato_desejado = input("Digite o nome do contato que deseja procurar: ")
        contato_encontrado = False
        for linha in agenda_de_contatos:
            if linha[0] == contato_desejado:
                print(f'\nNome: {linha[0]}\nNúmero de telefone: {linha[1]}\nE-mail: {linha[2]}\n')
                contato_encontrado = True
                break
        if not contato_encontrado:
            print(f'\nContato "{contato_desejado}" não encontrado.')

def exibir_menu():
    print('\n########## Menu ##########\n1. Buscar contato\n2. Adicionar contato\n3. Exibir contatos\n4. Excluir contato\n5. Sair')

try:
    agenda = open('agenda_de_contatos.csv', 'r')
    agenda.close()
except FileNotFoundError:
    criar_arquivo()

while True:
    exibir_menu()
    opcao = int(input('\nEscolha uma opção (1, 2, 3, 4 ou 5): '))

    if opcao == 1:
        buscar_contato()
    elif opcao == 2:
        nome = input('\nDigite o nome do contato: ')
        telefone = input('Digite o número de telefone: ')
        email = input("Digite o e-mail: ")
        adicionar_contato(nome, telefone, email)
        print("\nContato adicionado com sucesso!")
    elif opcao == 3:
        listar_contatos()
    elif opcao == 4:
        nome = input('Digite o nome do contato que deseja excluir: ')
        excluir_contato(nome)
    elif opcao == 5:
        print("\nSaindo do programa. Até mais!")
        break
    else:
        print("\nOpção inválida. Por favor, escolha 1, 2, 3, 4 ou 5.")