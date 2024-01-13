def verificar_palindromo(ent):
    ent = ent.lower().replace(" ", "")

    ent = ''.join(e for e in ent if e.isalnum())

    for i in range(len(ent)//2):
        if ent[i] != ent[len(ent)-i-1]:
            return False
    
    return True

while True:
    entrada = input("\nDigite uma palavra ou frase para verificar se é um palíndromo: ")

    if verificar_palindromo(entrada):
        print(f"{entrada} é um palíndromo!")
    else:
        print(f"{entrada} não é um palíndromo.")

    continuar = input("\nGostaria de continuar? Aperte [ENTER] para continuar ou digite [S] para sair: ")

    if continuar.lower() == 's':
        print("Programa encerrado.")
        break