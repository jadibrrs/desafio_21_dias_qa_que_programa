import time

def temporizador(segundos):
    segundos = int(segundos)

    print(f"\nTemporizador iniciado para {segundos} segundos.")
    
    for segundo_atual in range(segundos, 0, -1):
        print(segundo_atual)
        time.sleep(1)
    
    print("0\nTempo expirado!")

def contador(segundos):
    segundos = int(segundos)

    print(f"\nIniciando contagem até {segundos} segundos.")

    for segundo_atual in range(1, segundos, +1):
        print(segundo_atual)
        time.sleep(1)
    
    print(f"{segundo_atual + 1}\nTempo expirado!")

def solicitar_operacao():
    operacao = float(input("\nSelecione a operação desejada:\n[1]Contador\n[2] Temporizador\n"))

    if operacao == 1:
        entrada = input("\nDigite quantos segundos gostaria de temporizar: ")
        temporizador(entrada)
    elif operacao == 2:
        entrada = input("\nDigite quantos segundos gostaria de contar: ")
        contador(entrada)
    else:
        print("Operação inválida.")

while True:
    solicitar_operacao()

    continuar = input("\nGostaria de utilizar o contador/temporizador novamente?\nAperte [ENTER] para continuar ou digite [S] para sair: ")

    if continuar.lower() == 's':
        print("Programa encerrado.")
        break
