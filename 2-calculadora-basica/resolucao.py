print("Olá! Bem-vindo (a) à calculadora!\nVocê poderá realizar operações básicas de matemática, como adição, subtração, multiplicação e divisão.")

calcular = True

while calcular:
    try:
        numero1 = float(input("\nDigite o primeiro número: "))

        operacao = int(input("Escolha a operação - [1] Somar, [2] Subtrair, [3] Multiplicar ou [4] Dividir: ")) 

        while operacao < 1 or operacao > 4:
            print()
            operacao = int(input("Opção inválida. Por favor, insira um código da operação entre 1 e 4: "))

        numero2 = float(input("Digite o segundo número: "))

        if operacao == 1:
            resultado = numero1 + numero2
        elif operacao == 2:
            resultado = numero1 - numero2
        elif operacao == 3:
            resultado = numero1 * numero2
        else:
            if numero2 == 0:
                raise ValueError("Não é possível realizar a divisão por zero. Encerrando o programa.")
            else:
                resultado = numero1 / numero2

        print(f"\nResultado: {resultado}.\n")

        continuar = input("Deseja continuar? Digite [S] para Sim ou [N] para Não: ")

        if continuar.lower() == "n":
            calcular = False
        elif continuar.lower() == "s":
            calcular = True
        else:
            print("Opção inválida. Encerrando o programa.")
            calcular = False

    except ValueError as e:
        if "divisão por zero" in str(e):
            print(f"Erro: {e}")
        else: 
            print(f"Erro: {e}")
            print("Opção inválida. Encerrando o programa.")
        calcular = False