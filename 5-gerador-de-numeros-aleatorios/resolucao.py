import random

def gerar_numeros_mega_sena():
    numeros = []

    while len(numeros) < 6:
        numero = random.randint(1, 60)

        if numero not in numeros:
            numeros.append(numero)
    
    return numeros


while True:
    mega_sena = gerar_numeros_mega_sena()
    print(f"\nNúmeros da Mega Sena: {mega_sena}")

    continuar = input("\nGostaria de continuar? Aperte [ENTER] para continuar ou digite [S] para sair: ")

    if continuar.lower() == 's':
        print("Programa encerrado.")
        break
