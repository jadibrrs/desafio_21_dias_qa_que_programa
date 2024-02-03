def run_quiz(questions, start_index, end_index):
    score = 0

    for i in range(start_index, end_index):
        question, options, correct_answer = questions[i]
        print(f"\n{question} Responda A, B ou C.")
        for j, option in enumerate(options, start=1):
            print(f"{option}")

        user_answer = input("\nSua resposta: ")

        if user_answer.lower() == correct_answer.lower():
            print("Correto!")
            score += 1
        else:
            print(f"Incorreto. A resposta correta era: {correct_answer}")

    return score


# Lista de perguntas, opções de resposta e respostas corretas
questions_list = [
    ("Qual é a capital do Brasil?", ["a) Rio de Janeiro", "b) São Paulo", "c) Brasília"], "c"),
    ("Quem escreveu 'Dom Quixote'?", ["a) William Shakespeare", "b) Miguel de Cervantes", "c) Jane Austen"], "b"),
    ("Qual é o maior planeta do sistema solar?", ["a) Terra", "b) Júpiter", "c) Marte"], "b"),
    ("Qual é a capital da Argentina?", ["a) Buenos Aires", "b) Rio de Janeiro", "c) Madrid"], "a"),
    ("Qual é o maior rio do mundo?", ["a) Yangtze", "b) Amazonas", "c) Nilo"], "b"),
    ("Quem pintou a 'Mona Lisa'?", ["a) Leonardo da Vinci", "b) Vincent Van Gogh", "c) Claude Monet"], "a"),
    ("Quem é o autor de 'Romeu e Julieta'?", ["a) Lord Byron", "b) Jane Austen", "c) William Shakespeare"], "c"),
    ("Qual é o símbolo químico do oxigênio?", ["a) O", "b) O2", "c) Ox"], "a"),
    ("Qual é o segundo maior planeta do sistema solar?", ["a) Júpiter", "b) Saturno", "c) Urano"], "b"),
    ("Quem foi o primeiro presidente dos Estados Unidos?", ["a) George Washington", "b) Thomas Jefferson", "c) Abraham Lincoln"], "a"),
    ("Qual é a montanha mais alta do mundo?", ["a) Montanha do Vale da Morte", "b) Monte Everest", "c) Monte Kilimanjaro"], "b"),
    ("Qual é o maior rio totalmente brasileiro?", ["a) Amazonas", "b) São Francisco", "c) Paraná"], "b"),
    ("Quem foi o líder do movimento pela independência do Brasil?", ["a) Dom Pedro I", "b) Tiradentes", "c) Getúlio Vargas"], "a"),
    ("Em que ano o Brasil sediou a Copa do Mundo de Futebol pela última vez?", ["a) 2002", "b) 2010", "c) 2014"], "c"),
    ("Quem escreveu 'O Pequeno Príncipe'?", ["a) J.K. Rowling", "b) Antoine de Saint-Exupéry", "c) Gabriel García Márquez"], "b"),
    ("Qual é o maior oceano do mundo?", ["a) Oceano Atlântico", "b) Oceano Índico", "c) Oceano Pacífico"], "c"),
    ("Quem foi o inventor da lâmpada elétrica?", ["a) Nikola Tesla", "b) Thomas Edison", "c) Marie Curie"], "b"),
    ("Quem foi o arquiteto responsável pela criação de Brasília, a capital do Brasil?", ["a) Oscar Niemeyer", "b) Lúcio Costa", "c) Paulo Mendes da Rocha"], "a"),
    ("Qual é o prato típico brasileiro feito com feijão-preto, arroz, carne-seca, linguiça e outros ingredientes?", ["a) Acarajé", "b) Feijoada", "c) Moqueca"], "b"),
    ("Quantas estrelas possui a bandeira do Brasil?", ["a) 26", "b) 27", "c) 28"], "b"),
]

def main():
    index = 0
    while True:
        end_index = index + 3 if index + 3 <= len(questions_list) else len(questions_list)
        score = run_quiz(questions_list, index, end_index)
        print(f"Sua pontuação parcial: {score}/{end_index - index}")

        play_again = input("Deseja jogar novamente? (Digite 'SAIR' para encerrar ou aperte [ENTER] para continuar): ").lower()
        if play_again == 'sair':
            break

        index = (index + 3) % len(questions_list)

if __name__ == "__main__":
    main()