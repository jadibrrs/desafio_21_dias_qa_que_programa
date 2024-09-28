def criar_consulta_select():
    colunas = input("Digite as colunas separadas por vírgula: ")
    tabela = input("Digite o nome da tabela: ")
    condicao = input("Digite a condição WHERE (ou deixe em branco se não houver): ")
    
    consulta = f"SELECT {colunas} FROM {tabela}"
    if condicao:
        consulta += f" WHERE {condicao}"

    print(f"Consulta SQL gerada: \"{consulta}\"")

def criar_comando_update():
    tabela = input("Digite o nome da tabela: ")
    coluna_valor = input("Digite a coluna e seu novo valor no formato 'coluna = valor': ")
    condicao = input("Digite a condição WHERE: ")

    comando = f"UPDATE {tabela} SET {coluna_valor} WHERE {condicao}"
    print(f"Comando SQL gerado: \"{comando}\"")

def criar_comando_insert():
    tabela = input("Digite o nome da tabela: ")
    colunas = input("Digite as colunas separadas por vírgula: ")
    valores = input("Digite os valores correspondentes no mesmo formato: ")

    comando = f"INSERT INTO {tabela} ({colunas}) VALUES ({valores})"
    print(f"Comando SQL gerado: \"{comando}\"")

while True:
    # Menu Interativo
    print("\n### Construtor de Consultas SQL ###")
    print("1. Criar Consulta SQL SELECT")
    print("2. Criar Comando SQL UPDATE")
    print("3. Criar Comando SQL INSERT")
    print("4. Sair")

    opcao = int(input("\nEscolha a opção (1, 2, 3 ou 4): "))

    if opcao == 1:
        criar_consulta_select()
    elif opcao == 2:
        criar_comando_update()
    elif opcao == 3:
        criar_comando_insert()
    elif opcao == 4:
        break
    else:
        print("Opção inválida. Por favor, escolha 1, 2 ou 3.")
