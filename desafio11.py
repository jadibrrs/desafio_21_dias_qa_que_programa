def adicionar_numero_a_lista(lista):
    novo_numero = int(input())
    lista.append(novo_numero)

def organizar_e_exibir_lista(lista):
    lista.sort()
    print(f"\nLista atual: {lista}")

########################################################
lista = []

print("\n########## Ordenador de Lista ##########")
quantidade = int(input("\nBem-vindo(a) ao ordenador. Digite a quantidade de números que gostaria de acrescentar à lista: "))

if quantidade > 0:
    print("\nUm por vez, digite os números que gostaria acrescentar à lista: ")
    for i in range(0, quantidade, +1):
        adicionar_numero_a_lista(lista)

organizar_e_exibir_lista(lista)