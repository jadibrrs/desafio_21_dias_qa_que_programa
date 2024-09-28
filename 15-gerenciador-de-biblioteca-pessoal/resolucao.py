import csv

def criar_arquivo():
    with open('biblioteca.csv', 'w', newline='') as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow(['Título', 'Autor', 'Ano de Publicação'])

def adicionar_livro(titulo, autor, ano):
    with open('biblioteca.csv', 'a', newline='') as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow([titulo, autor, ano])

def remover_livro(titulo):
    livros = []
    with open('biblioteca.csv', 'r', newline='') as arquivo:
        leitor = csv.reader(arquivo)
        for linha in leitor:
            if linha[0] != titulo:
                livros.append(linha)

    with open('biblioteca.csv', 'w', newline='') as arquivo:
        escritor = csv.writer(arquivo)
        for livro in livros:
            escritor.writerow(livro)

def listar_livros():
    with open('biblioteca.csv', 'r') as arquivo:
        leitor = csv.reader(arquivo)
        for linha in leitor:
            if linha[0] != "Título":             
                print(f'Título: {linha[0]}, Autor: {linha[1]}, Ano: {linha[2]}')

def menu():
    print("\n########## Menu ##########\n1. Adicionar Livro\n2. Listar Livros\n3. Remover livro\n4. Sair")

try:
    livro = open('biblioteca.csv', 'r')
    livro.close()
except FileNotFoundError:
    criar_arquivo()

while True:
    menu()
    opcao = int(input("\nEscolha uma opção (1, 2, 3 ou 4): "))

    if opcao == 1:
        titulo = input("\nDigite o título do livro: ")
        autor = input("Digite o nome do autor: ")
        ano = input("Digite o ano de publicação: ")
        adicionar_livro(titulo, autor, ano)
        print("\nLivro adicionado com sucesso!")
    elif opcao == 2:
        print("\n------ Lista de Livros ------")
        listar_livros()
    elif opcao == 3:
        titulo = input("\nDigite o título do livro que deseja remover: ")
        remover_livro(titulo)
        print("\nLivro removido com sucesso!")
    elif opcao == 4:
        print("\nSaindo do programa. Até mais!")
        break
    else:
        print("\nOpção inválida. Por favor, escolha 1, 2, 3 ou 4.")