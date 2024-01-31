import requests

def obter_taxas_moeda(moeda_base):
    url = f"https://open.er-api.com/v6/latest/{moeda_base}"
    resposta = requests.get(url)

    if resposta.status_code == 200:
        dados = resposta.json()
        return dados['rates']
    else:
        print(f"Erro ao obter taxas. Código de status: {resposta.status_code}")
        return None

def converter_moeda(valor, moeda_origem, moeda_destino, taxas):
    if moeda_origem not in taxas or moeda_destino not in taxas:
        print("Moeda inválida. Verifique as opções disponíveis.")
        return None

    taxa_origem = taxas[moeda_origem]
    taxa_destino = taxas[moeda_destino]

    valor_convertido = valor * (taxa_destino / taxa_origem)
    return valor_convertido

def main():
    moeda_base = input("Insira a moeda de origem (por exemplo, USD): ")
    valor = float(input("Insira o valor a ser convertido: "))
    moeda_destino = input("Insira a moeda de destino (por exemplo, EUR): ")

    taxas = obter_taxas_moeda(moeda_base)

    if taxas is not None:
        valor_convertido = converter_moeda(valor, moeda_base, moeda_destino, taxas)

        if valor_convertido is not None:
            print(f"{valor} {moeda_base} é equivalente a {valor_convertido:.2f} {moeda_destino}")

if __name__ == "__main__":
    main()