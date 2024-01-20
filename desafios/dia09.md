# Dia 9: Jogo do Número Primo

## Desafio

Desenvolva um jogo que gera aleatoriamente um número e o jogador deve determinar se esse número é primo ou não. O jogador ganha pontos por cada resposta correta.

## Conhecimentos necessários para resolver este desafio

- Lógica para verificar números primos: Aprenda a lógica matemática por trás dos números primos.
- Geração de Números Aleatórios: Use o módulo random para gerar números aleatórios.
- Criação de funções para organizar melhor o seu código.
- Input do jogador e Condições: Receba a resposta do jogador e verifique se está correta.

## Dica

Um número primo é aquele que só é divisível por 1 e por ele mesmo. Você pode criar uma função que verifica se um número é primo ou não, e então usá-la para determinar a resposta do jogador.
A cada acerto ele ganha um ponto
Crie um menu inicial que contém opções pra Jogar, Ver Pontuação, Zerar Pontuação, Sair

## Testes

Realize alguns testes em seu script no terminal. Execute seu script usando os valores abaixo, para ver se ele se comporta como esperado.

- TESTE 01: O programa gera o número 7. O jogador responde "Primo". A resposta está correta, e o jogador ganha pontos.
- TESTE 02: O programa gera o número 10. O jogador responde "Não Primo". A resposta está correta, e o jogador ganha pontos.
- TESTE 03: O programa gera o número 15. O jogador responde "Primo". A resposta está incorreta, e o jogador não ganha pontos - e o jogo acaba.
- TESTE 04: O programa gera o número 3. O jogador responde "Não Primo". A resposta está incorreta, e o jogador não ganha - pontos e o jogo acaba.
- TESTE 05: O jogador escolhe a opção de ver sua pontuação e ela está correta.
- TESTE 06: O jogador escolhe a opção de zerar sua pontuação e ao jogar novamente e acertar, sua pontuação vai pra 1.
- TESTE 07: O jogador escolhe a opção de sair.

Você pode fazer outros testes caso ache necessário.

Obs.: Números primos de 2 a 50 -> 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47.