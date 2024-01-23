# Dia 13: Validador de E-mail

## Desafio

Desenvolva um script que verifique se uma string fornecida pelo usuário é um e-mail válido.

## Conhecimentos necessários para resolver este desafio

- Expressões Regulares (Regex): Aprenda a usar expressões regulares em Python para validar formatos de e-mail.
- Condições e Manipulação de Strings: Use condições para verificar a validade.

## Dica

Pesquise sobre expressões regulares em Python, pois são essenciais para validar e-mails com precisão.

Considere os elementos abaixo para considerar um e-mail válido:
- O endereço de e-mail deve conter um único símbolo "@" que separa a parte local e o domínio.
- A parte local (antes do "@") deve consistir em letras maiúsculas e minúsculas, dígitos e alguns caracteres especiais como ".", "_", "%", "+", e "-".
- O domínio (após o "@") deve ser composto por letras maiúsculas e minúsculas, dígitos e os caracteres especiais ".", e "-".
- O domínio deve ter pelo menos um ponto "." para separar o domínio de alto nível (TLD) do domínio de segundo nível (SLD), como em "exemplo.com".
- O TLD (Top-Level Domain) deve consistir de pelo menos duas letras maiúsculas ou minúsculas.
- Os espaços em branco não são permitidos em um endereço de e-mail.

## Testes

Realize alguns testes em seu script no terminal. Execute seu script usando os valores abaixo, para ver se ele se comporta como esperado.

- TESTE 01:

E-mail fornecido: "usuario@email.com"

Resultado esperado: E-mail válido

- TESTE 02:

E-mail fornecido: "email.com"

Resultado esperado: E-mail inválido

- TESTE 03:

E-mail fornecido: "usuario@.com"

Resultado esperado: E-mail inválido

- TESTE 04:

E-mail fornecido: "usuario@dominio"

Resultado esperado: E-mail inválido

- TESTE 05:

E-mail fornecido: "@dominio.com"

Resultado esperado: E-mail inválido

- TESTE 06:

E-mail fornecido: "meu email@dominio.com"

Resultado esperado: E-mail inválido

- TESTE 07:

E-mail fornecido: "meu@dominio.c"

Resultado esperado: E-mail inválido

Você pode fazer outros testes caso ache necessário.