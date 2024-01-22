# Dia 12: Análise de Frequência de Letras

## Desafio

Desenvolva um programa que analise a frequência de cada letra em um texto fornecido pelo usuário.

## Conhecimentos necessários para resolver este desafio

- Manipulação de Strings: Aprenda a contar a frequência de caracteres e a checar se um determinado caractere é uma letra (pode utilizar a função isalpha()).
- Manipulação de Dicionários: Aprenda a adicionar, obter e atualizar dados em um dicionário.
- Loops em Strings: Pratique a iteração em strings para análise.

## Dica

Use um dicionário para rastrear a contagem de cada letra no texto.

Certifique-se de tratar letras maiúsculas e minúsculas da mesma forma para obter resultados precisos.

Ignore espaços em branco, pontuações, números e caracteres especiais no texto, se desejar contar apenas letras. Considere o uso da função isalpha() para verificar se um caractere é uma letra antes de contar.

## Testes

Realize alguns testes em seu script no terminal. Execute seu script usando os valores abaixo, para ver se ele se comporta como esperado.

- TESTE 01:

Texto fornecido: "hello world"

Resultado esperado:

{

    'h': 1,

    'e': 1,

    'l': 3,

    'o': 2,

    'w': 1,

    'r': 1,

    'd': 1

}

- TESTE 02:

Texto fornecido: "programming is fun"

Resultado esperado:

{

    'p': 1,

    'r': 2,

    'o': 1,

    'g': 2,

    'a': 1,

    'm': 2,

    'i': 2,

    'n': 2,

    's': 1,

    'f': 1,

    'u': 1

}

- TESTE 03:

Texto fornecido: "testing 123321"

Resultado esperado:

{
    
    't': 2,

    'e': 1,

    's': 1,

    'i': 1,

    'n': 1,

    'g': 1

}

Você pode fazer outros testes caso ache necessário.