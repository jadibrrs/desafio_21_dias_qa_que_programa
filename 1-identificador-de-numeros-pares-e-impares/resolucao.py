print("Insira um número: ")

try:
    numero = int(input())

    if numero % 2 == 0:
        print("Este número é par.")
    elif numero % 2 == 1:
        print("Este número é ímpar.")
    else:
        print("Este valor não é um número.")
except ValueError:
    print("Entrada inválida. Por favor, insira um número inteiro.")
