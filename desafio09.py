import random

def verificar_se_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5)+ 1):
        if numero % i == 0:
            return False
    return True

pontos = 0
jogar = True

print("\n#################### Jogo do Número Primo ####################")

modo = int(input("Selecione o modo de jogo: [1] Fácil, [2] Médio ou [3] Difícil.\n"))

while jogar == True and modo == 1:
    numero = random.randint(2, 50)
    resposta = input(f"\nO número {numero} é primo? Digite [Primo] ou [Não primo]: ")

    if resposta.lower() == "primo" and verificar_se_primo(numero) or resposta.lower() == "não primo" and not verificar_se_primo(numero):
        pontos = pontos + 1
        print(f"Parabéns, acertou! Agora seu placar é de {pontos} pontos.")
    elif resposta.lower() == "não primo" and verificar_se_primo(numero) or resposta.lower() == "primo" and not verificar_se_primo(numero):
        print(f"Não foi dessa vez! Seu placar continua em {pontos} pontos. Tente novamente!")
    else:
        print("Resposta inválida!")

    jogar = input("\nGostaria de continuar? Aperte [ENTER] para continuar ou digite [S] para sair: ")

    if jogar.lower() == 's':
        print("Programa encerrado.")
        break
    else:
        jogar = True

while jogar == True and modo == 2:
    numero = random.randint(2, 100)
    resposta = input(f"\nO número {numero} é primo? Digite [Primo] ou [Não primo]: ")

    if resposta.lower() == "primo" and verificar_se_primo(numero) or resposta.lower() == "não primo" and not verificar_se_primo(numero):
        pontos = pontos + 1
        print(f"Parabéns, acertou! Agora seu placar é de {pontos} pontos.")
    elif resposta.lower() == "não primo" and verificar_se_primo(numero) or resposta.lower() == "primo" and not verificar_se_primo(numero):
        print(f"Não foi dessa vez! Seu placar continua em {pontos} pontos. Tente novamente!")
    else:
        print("Resposta inválida!")

    jogar = input("\nGostaria de continuar? Aperte [ENTER] para continuar ou digite [S] para sair: ")

    if jogar.lower() == 's':
        print("Programa encerrado.")
        break
    else:
        jogar = True

while jogar == True and modo == 3:
    numero = random.randint(2, 500)
    resposta = input(f"\nO número {numero} é primo? Digite [Primo] ou [Não primo]: ")

    if resposta.lower() == "primo" and verificar_se_primo(numero) or resposta.lower() == "não primo" and not verificar_se_primo(numero):
        pontos = pontos + 1
        print(f"Parabéns, acertou! Agora seu placar é de {pontos} pontos.")
    elif resposta.lower() == "não primo" and verificar_se_primo(numero) or resposta.lower() == "primo" and not verificar_se_primo(numero):
        print(f"Não foi dessa vez! Seu placar continua em {pontos} pontos. Tente novamente!")
    else:
        print("Resposta inválida!")

    jogar = input("\nGostaria de continuar? Aperte [ENTER] para continuar ou digite [S] para sair: ")

    if jogar.lower() == 's':
        print("Programa encerrado.")
        break
    else:
        jogar = True