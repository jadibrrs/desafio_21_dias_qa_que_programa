import random

def senha_numeros_carac_espec(comprimento):
    senha = ''.join(random.choice("0123456789!@#$%^&*()_-+=<>?") for i in range(comprimento))
    return senha

def senha_numeros(comprimento):
    senha = ''.join(random.choice("0123456789") for i in range(comprimento))
    return senha

def senha_letras_maiusc_numeros(comprimento):
    senha = ''.join(random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789") for i in range(comprimento))
    return senha

def senha_letrasminusc_numeros_carac_espec(comprimento):
    senha = ''.join(random.choice("abcdefghijklmnopqrstuvwxyz!@#$%^&*()_-+=<>?") for i in range(comprimento))
    return senha

def senha_letras_maiusc_minusc_numeros_carac_espec(comprimento):
    senha = ''.join(random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()_-+=<>?") for i in range(comprimento))
    return senha

print("\n########## Gerador de Senha ##########")
comprimento = int(input("\nQuantos caracteres deseja em sua senha? Digite um número: "))

print("\nA senha poderá conter diferentes tipos de caracteres: \n[1] Números e caracteres especiais \n[2] Números \n[3] Números e letras maiúsculas \n[4] Números, letras maiúsculas e caracteres especiais \n[5] Números, caracteres especiais, letras maiúsculas e minúsculas")
tipo_de_senha = int(input("\nSelecione quais tipos de caracteres gostaria de ter em sua senha: "))

if tipo_de_senha == 1:
    print("Senha: ", senha_numeros_carac_espec(comprimento))
elif tipo_de_senha == 2:
    print("Senha: ", senha_numeros(comprimento))
elif tipo_de_senha == 3:
    print("Senha: ", senha_letras_maiusc_numeros(comprimento))
elif tipo_de_senha == 4:
    print("Senha: ", senha_letrasminusc_numeros_carac_espec(comprimento))
elif tipo_de_senha == 5:
    print("Senha: ", senha_letras_maiusc_minusc_numeros_carac_espec(comprimento))
else:
    print("Digite um tipo válido.")