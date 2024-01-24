import random

def gerar_numero():
    #numero = random.randint(1, 100)
    numero = 67
    return numero

def verificar_resposta(numero, resposta, pontos):

    if numero == resposta:
        pontos += 1
        print(f"Correto! O número {resposta} é a resposta certa!")
        print(f"Pontuação: {pontos}")
        return True
    elif numero < resposta:
        print("O número correto é menor que a sua resposta.")
        return False
    else:
        print("O número correto é maior que a sua resposta.")
        return False

def acao(acao):
    global numero
    global pontos
    global jogar

    if acao == 1:
        print("\nSelecionamos um número entre os números 1 e 100. Adivinhe qual é!")
        numero = gerar_numero()
        for i in range(7, 0, -1):
            resposta = int(input("\nDigite sua resposta: "))
            if verificar_resposta(numero, resposta, pontos):
                pontos += 1
                break
            if i == 1:
                print(f"Não foi desta vez! A resposta era {numero}.\nJogo encerrado.")
            else:
                print(f"Você tem {i-1} tentativas.")
    elif acao == 2:
        print(f"Pontuação: {pontos}")
    elif acao == 3:
        pontos = 0
    elif acao == 4:
        print("Programa encerrado.")
        jogar = False
    else:
        print("Digite uma ação válida.")

numero = 0
pontos = 0
jogar = True

print("#################### Jogo da Adivinhação ###################")

while jogar: 
    acao_usuario = int(input("\nSelecione: [1] Jogar, [2] Ver Pontuação, [3] Zerar Pontuação ou [4] Sair\n"))
    acao(acao_usuario)