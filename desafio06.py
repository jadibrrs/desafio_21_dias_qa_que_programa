def converter(opcao, valor):
    conversoes = {
        "1": lambda valor: valor * 0.621371,
        "2": lambda valor: valor * 1.60934,
        "3": lambda valor: valor * 3.28084,
        "4": lambda valor: valor * 0.3048,
        "5": lambda valor: (valor * 9/5) + 32,
        "6": lambda valor: (valor - 32) * 5/9
    }
    
    operacao = conversoes.get(opcao)
    if operacao is not None:
        return operacao(valor)
    else:
        return f"Operação '{opcao}' inválida."
        
    
def obter_numero_input(mensagem):
    while True:
        try:
            entrada = float(input(mensagem))
            return entrada
        except ValueError:
            print("Digite um valor numérico válido.")

while True:
    conversao = input("\nSelecione a operação que deseja converter: \n[1] Quilômetros para Milhas\n[2] Milhas para Quilômetros\n[3] Metros para Pés\n[4] Pés para Metros\n[5] Graus Celsius para Fahrenheit\n[6] Graus Fahrenheit para Celsius\n")

    entrada = obter_numero_input("Digite o valor que deseja converter: ")

    resultado = converter(conversao, entrada)

    print(f"Resultado: {resultado}")

    continuar = input("\nGostaria de continuar? Aperte [ENTER] para continuar ou digite [S] para sair: ")

    if continuar.lower() == 's':
        print("Programa encerrado.")
        break