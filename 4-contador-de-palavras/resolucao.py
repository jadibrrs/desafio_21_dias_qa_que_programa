def contar_palavras(ent):
    palavras = ent.split()

    numero_palavras = len(palavras)

    return numero_palavras

while True:
    entrada = input("\nDigite o texto para verificar o número de palavras: ")

    resultado = contar_palavras(entrada)

    if resultado == 1:
        print(f"Seu texto contém {resultado} palavra.")
    elif resultado == 0:
        print("Seu texto não contém palavras.")
    else:
        print(f"Seu texto contém {resultado} palavras.")

    continuar = input("\nGostaria de continuar? Aperte [ENTER] para continuar ou digite [S] para sair: ")

    if continuar.lower() == 's':
        print("Programa encerrado.")
        break