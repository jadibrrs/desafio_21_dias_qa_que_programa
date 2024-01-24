import re

# ^: Início da string
# [ ]: Define uma classe de caracteres (por exemplo, [aeiou] corresponde a qualquer vogal); qualquer caractere entre os especificados
# +: Corresponde a uma ou mais repetições do caractere anterior.
# @: O caractere "@" literal
# \.: O caractere "." literal (separando o domínio da extensão)
# {m,}: Corresponde a m ou mais repetições do caractere anterior
# $: Fim da string

def validar_email(email):
    condicoes = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(condicoes, email) is not None


email_entrada = input("\nDigite um e-mail: ")

email_entrada = email_entrada.strip()

if validar_email(email_entrada):
    print("O e-mail é válido.")
else:
    print("O e-mail não é válido.")