import random

def escolher_palavra(substantivos_por_letra):
    palavras = [random.choice(substantivos_por_letra[letra]) for letra in 'abcdefghijklmnopqrstuvwxyz']
    return random.choice(palavras)

def mostrar_palavra_oculta(palavra, letras_corretas):
    palavra_oculta = ''
    for letra in palavra:
        if letra in letras_corretas:
            palavra_oculta += letra
        else:
            palavra_oculta += '_'
    return palavra_oculta

def jogar_forca():
    palavra_secreta = escolher_palavra(substantivos_por_letra)
    letras_corretas = []
    tentativas = 15

    print("\n########## Jogo da Forca ##########")
    print("Bem-vindo/a ao Jogo da Forca!")
    
    while tentativas > 0:
        palavra_oculta = mostrar_palavra_oculta(palavra_secreta, letras_corretas)
        print("\nPalavra: " + palavra_oculta)
        print("Tentativas restantes: " + str(tentativas))
        
        chute = input("Digite uma letra: ").lower()

        # Verifica se a letra já foi escolhida antes
        if chute in letras_corretas:
            print("Você já escolheu essa letra. Tente novamente.")
            continue

        # Verifica se a letra está na palavra
        if chute in palavra_secreta:
            print("Letra correta!")
            letras_corretas.append(chute)
        else:
            print("Letra incorreta.")
            tentativas -= 1

        # Verifica se o jogador acertou todas as letras
        if all(letra in letras_corretas for letra in palavra_secreta):
            print("\nParabéns! Você acertou a palavra:", palavra_secreta)
            break

    if tentativas == 0:
        print("\nFim do jogo. A palavra correta era:", palavra_secreta)

substantivos_por_letra = {
    'a': ['abacaxi', 'abelha', 'arco', 'avião', 'amigo', 'abóbora', 'alface', 'anel', 'água', 'árvore'],
    'b': ['bola', 'barco', 'banana', 'bicicleta', 'barraca', 'bebê', 'botão', 'bolsa', 'brinquedo', 'bússola'],
    'c': ['cadeira', 'cachorro', 'coração', 'cavalo', 'carro', 'castelo', 'cachecol', 'cola', 'céu', 'camiseta'],
    'd': ['dado', 'dente', 'dedo', 'dança', 'dado', 'diário', 'diamante', 'doce', 'duende', 'duna'],
    'e': ['elefante', 'escada', 'estrela', 'escola', 'escova', 'escudo', 'esmeralda', 'espelho', 'espinha', 'espada'],
    'f': ['foca', 'foguete', 'fada', 'fazenda', 'floresta', 'futebol', 'fivela', 'foca', 'fogão', 'folha'],
    'g': ['girafa', 'gato', 'guitarra', 'gota', 'garrafa', 'globo', 'grilo', 'gruta', 'guarda-chuva', 'guitarra'],
    'h': ['hipopótamo', 'helicóptero', 'hamburguer', 'harpa', 'haste', 'hélice', 'horizonte', 'hiena', 'herói', 'hino'],
    'i': ['iglu', 'iguana', 'índio', 'ilha', 'ilusão', 'inspiração', 'impressora', 'iluminador', 'ícone', 'instrumento'],
    'j': ['jacaré', 'jardim', 'joaninha', 'janela', 'jogador', 'jipe', 'jovem', 'juba', 'juramento', 'joia'],
    'k': ['kiwi', 'ketchup', 'kung fu', 'karaokê', 'kinect', 'kilt', 'kiropraxia', 'kit', 'koala', 'kombi'],
    'l': ['leão', 'lua', 'lápis', 'limão', 'lago', 'lanterna', 'livro', 'lente', 'líder', 'leite'],
    'm': ['macaco', 'montanha', 'mochila', 'martelo', 'melancia', 'melodia', 'máscara', 'mamute', 'minuto', 'mapa'],
    'n': ['navio', 'nariz', 'navalha', 'nuvem', 'nota', 'ninho', 'número', 'nível', 'ninja', 'noite'],
    'o': ['olho', 'ouro', 'onda', 'ocelote', 'organizador', 'óculos', 'oceano', 'orelha', 'ovelha', 'ônibus'],
    'p': ['pato', 'pipa', 'palavra', 'piano', 'ponte', 'papel', 'pérola', 'pote', 'pássaro', 'porta'],
    'q': ['quadro', 'quarto', 'quintal', 'quimono', 'queijo', 'quilha', 'quilo', 'quente', 'quintal', 'quina'],
    'r': ['rato', 'rosa', 'raio', 'roda', 'rio', 'rainha', 'relógio', 'rampa', 'rancho', 'rede'],
    's': ['sapo', 'sol', 'sanduíche', 'sapato', 'sabonete', 'sorvete', 'sela', 'sino', 'safira', 'serpente'],
    't': ['tigre', 'toca', 'travesseiro', 'tênis', 'trem', 'tartaruga', 'tijolo', 'teatro', 'trono', 'tocha'],
    'u': ['urso', 'uva', 'universo', 'uísque', 'uva-passa', 'urânio', 'urutu', 'uvaia', 'ultraleve', 'umidade'],
    'v': ['vaca', 'violinista', 'vassoura', 'ventilador', 'vaso', 'violão', 'vulcão', 'vampiro', 'viseira', 'velocidade'],
    'w': ['webcam', 'whisky', 'waffle', 'walkman', 'wifi', 'websites', 'waterpolo', 'winchester', 'wolverine', 'whiskas'],
    'x': ['xadrez', 'xícara', 'xale', 'xerife', 'xerox', 'xale', 'xenofobia', 'xarope', 'xenônio', 'xícara'],
    'y': ['yeti', 'yoga', 'yakisoba', 'yogurte', 'yurt', 'yin-yang', 'yoga', 'youtuber', 'yale', 'yogini'],
    'z': ['zebra', 'zangão', 'zíper', 'zoológico', 'zumbi', 'zona', 'zaragata', 'zombaria', 'zoologia', 'ziguezague']
}

jogar_forca()