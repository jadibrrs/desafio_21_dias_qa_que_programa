entrada = input("\nDigite um texto: ").lower()  # Convertendo para minúsculas para não diferenciar maiúsculas de minúsculas
frequencia_letras = {}

# Contando a frequência de cada letra
for caractere in entrada:
    if caractere.isalpha():
        if caractere in frequencia_letras:
            frequencia_letras[caractere] += 1
        else:
            frequencia_letras[caractere] = 1

# Exibindo os resultados
if frequencia_letras == {}:
    print("Não foram fornecidas letras.")
else: 
    print("\nFrequência de cada letra:")
    for letra, frequencia in frequencia_letras.items(): #letra, frequencia
        print(f"{letra}: {frequencia}")