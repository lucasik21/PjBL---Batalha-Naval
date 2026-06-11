# Aqui importamos as bibliotecas random e time para utiliza-las futuramente para aleatorizar a jogada do computador,
# e o time para dar a sensação de jogar a rodada
import random
import time

# Embaixo é feito um dicionário com os barcos e elementos e qual emoji é atribuido a tal
PORTA_AVIOES = "🛫"
NAVIO_TANQUE = "🚚"
CONTRATORPEDEIRO = "🚢"
SUBMARINO = "🚤"
DESTROIER = "⛵"

AGUA = "🌊"
ACERTO = "❌"
ERRO = "⭕"

# Atribuimos um valor aos barcos em uma lista
FROTA = [
    (PORTA_AVIOES, 5),
    (NAVIO_TANQUE, 4),
    (CONTRATORPEDEIRO, 3),
    (SUBMARINO, 2),
    (DESTROIER, 1)
]
# Cria a primeira função para verificar os valores de cada navio
def verifica_navio(valor):
    return valor in [
        PORTA_AVIOES,
        NAVIO_TANQUE,
        CONTRATORPEDEIRO,
        SUBMARINO,
        DESTROIER
    ]

# Cria uma função para atribuir um nome a cada barco, criando a variável de símbolo
def nome_navio(simbolo):

    if simbolo == PORTA_AVIOES:
        return "Porta-Aviões"

    if simbolo == NAVIO_TANQUE:
        return "Navio-Tanque"

    if simbolo == CONTRATORPEDEIRO:
        return "Contratorpedeiro"

    if simbolo == SUBMARINO:
        return "Submarino"

    if simbolo == DESTROIER:
        return "Destroier"

    return "Desconhecido"

# Criamos a tela inicial, para o jogador digitar seu nome, para ser interativo e que pedia nas regras
def tela_inicial():
    print("=" * 40)
    print("        🚢 BATALHA NAVAL 🚢")
    print("=" * 40)

    jogador = input("Digite seu nome: ")

    print("\nBem-vindo,", jogador)
    print("Prepare-se para a batalha!\n")

    return jogador

# Aqui se cria o tabuleiro que se utiliza no código inteiro, em apenas loops com for que se cria a matriz, e utilizamos
# a AGUA do dicionário acima.
def criar_tabuleiro():
    matriz = []
    for i in range(10):
        linha = []
        for j in range(10):
            
            linha.append(AGUA)
        matriz.append(linha)
    return matriz

# Aqui também se cria outra função muito utilizada, para dar print ao usuário sobre a matriz, onde se pede qual
# tabuleiro ele quer, e o título em string que se vai usar.
# Feito também uma formatação abaixo, para caber tudo certinho
def mostrar_tabuleiro(tabuleiro, titulo):

    print("\n====== {} ======".format(titulo))

    print("      A   B   C   D    E   F   G   H    I   J")

    for i in range(len(tabuleiro)):
        linha_formatada = ""

        for elemento in tabuleiro[i]:
            linha_formatada += "{:<3}".format(elemento)

        print("{:2} | {}".format(i + 1, linha_formatada))

# E então a parte mais importante, sobre o posicionamento dos barcos pelo que o usuário digita, pedindo linha e coluna
# Ele verifica com if se podem ser usadas tais linhas e colunas, e então pedem a direção, que se verifica com for com
# flag, e no vertical ele vai preenchendo, porém a cada linha que se for preenchida, ele soma.
def posicionando_navios_jogador(tabuleiro):

    letras = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]

    for simbolo, tamanho in FROTA:

        while True:

            print("\nPosicionando", simbolo)
            print("Tamanho:", tamanho)

            try:
                linha = int(input("Linha inicial (1-10): ")) - 1
            except ValueError:
                print("Digite apenas números.")
                continue

            coluna = input("Coluna (A-J): ").upper()

            if coluna not in letras:
                print("Coluna inválida!")
                continue

            coluna = letras.index(coluna)

            if linha < 0 or linha > 9:
                print("Linha inválida!")
                continue

            direcao = input("Horizontal (H) ou Vertical (V)? ").upper()

            if direcao not in ["H", "V"]:
                print("Direção inválida!")
                continue

            # HORIZONTAL
            if direcao == "H":

                if coluna + tamanho > 10:
                    print("Navio ultrapassa o tabuleiro!")
                    continue

                livre = True

                for i in range(tamanho):
                    if tabuleiro[linha][coluna + i] != AGUA:
                        livre = False

                if not livre:
                    print("Já existe um navio nessa posição!")
                    continue

                for i in range(tamanho):
                    tabuleiro[linha][coluna + i] = simbolo

            # VERTICAL
            else:

                if linha + tamanho > 10:
                    print("Navio ultrapassa o tabuleiro!")
                    continue

                livre = True

                for i in range(tamanho):
                    if tabuleiro[linha + i][coluna] != AGUA:
                        livre = False

                if not livre:
                    print("Já existe um navio nessa posição!")
                    continue

                for i in range(tamanho):
                    tabuleiro[linha + i][coluna] = simbolo

            mostrar_tabuleiro(
                tabuleiro,
                "TABULEIRO DO JOGADOR"
            )

            break

# Aqui foi feito utilizando a biblioteca random, onde para cada simbolo, utilizando o nome_navio, ele vai ocupar certa
# posição. Nesse caso, o computador escolhe um número aleatório de 0 a 9, e dentro disso ele preenche, também escolhendo
# aleatoriamente o sentido.
def posicionando_navios_computador(tabuleiro):

    for simbolo, tamanho in FROTA:

        while True:

            direcao = random.choice(["H", "V"])

            linha = random.randint(0, 9)
            coluna = random.randint(0, 9)

            # Horizontal
            if direcao == "H":

                if coluna + tamanho > 10:
                    continue

                livre = True

                for i in range(tamanho):
                    if tabuleiro[linha][coluna + i] != AGUA:
                        livre = False

                if livre:
                    for i in range(tamanho):
                        tabuleiro[linha][coluna + i] = simbolo
                    break

            # Vertical
            else:

                if linha + tamanho > 10:
                    continue

                livre = True

                for i in range(tamanho):
                    if tabuleiro[linha + i][coluna] != AGUA:
                        livre = False

                if livre:
                    for i in range(tamanho):
                        tabuleiro[linha + i][coluna] = simbolo
                    break


def ataque_jogador(tabuleiroComputador, feedbackJogador):

    letras = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]

    while True:

        try:
            linha = int(input("Linha do ataque (1-10): ")) - 1
        except ValueError:
            print("Digite apenas números para a linha.")
            continue

        coluna = input("Coluna (A-J): ").upper()

        if linha < 0 or linha > 9:
            print("Linha inválida!")
            continue

        if coluna not in letras:
            print("Coluna inválida!")
            continue

        coluna = letras.index(coluna)

        # Verifica se já atacou essa posição
        if feedbackJogador[linha][coluna] != AGUA:
            print("Você já atacou essa posição!")
            continue

        # Acertou um navio
        if verifica_navio(tabuleiroComputador[linha][coluna]):
            time.sleep(0.5)
            print("💥 ACERTOU UMA EMBARCAÇÃO!")

            navio = tabuleiroComputador[linha][coluna]
            
            feedbackJogador[linha][coluna] = ACERTO
            tabuleiroComputador[linha][coluna] = AGUA
            time.sleep(0.8)
            if navio_afundou(tabuleiroComputador, navio):
                print("💀", nome_navio(navio), "AFUNDADO!")

            print("Navios restantes do computador:", contar_navios(tabuleiroComputador))

        # Errou
        else:
            time.sleep(0.5)
            print("...")
            time.sleep(0.5)
            print("Água!")

            feedbackJogador[linha][coluna] = ERRO

        break

def navio_afundou(tabuleiro, simbolo):

    for linha in tabuleiro:
        for elemento in linha:

            if elemento == simbolo:
                return False
            
    return True

def contar_navios(tabuleiro):

    quantidade = 0

    for linha in tabuleiro:
        for elemento in linha:
            if verifica_navio(elemento):
                quantidade += 1

    return quantidade

def ataque_computador(tabuleiroJogador, feedbackComputador):

    while True:

        linha = random.randint(0, 9)
        coluna = random.randint(0, 9)

        if feedbackComputador[linha][coluna] != AGUA:
            continue

        time.sleep(0.2)

        print("\nComputador atacou:",
              linha + 1,
              chr(coluna + 65))

        if verifica_navio(tabuleiroJogador[linha][coluna]):
            
            navio = tabuleiroJogador[linha][coluna]

            print("💥 O computador acertou um navio!")
            time.sleep(0.5)
            feedbackComputador[linha][coluna] = ACERTO
            tabuleiroJogador[linha][coluna] = AGUA

            if navio_afundou(tabuleiroJogador, navio):
                print("💀 Seu", nome_navio(navio), "FOI AFUNDADO!")
                time.sleep(1)
            print("Seus navios restantes:", contar_navios(tabuleiroJogador))

        else:

            print("🌊 O computador errou!")
            time.sleep(1)
            feedbackComputador[linha][coluna] = ERRO

        break

def main():
    nome = tela_inicial()
    tabuleiroJogador = criar_tabuleiro()
    feedbackJogador = criar_tabuleiro()

    tabuleiroComputador = criar_tabuleiro()
    feedbackComputador = criar_tabuleiro()

    # MOSTRA TABULEIRO DO JOGADOR
    mostrar_tabuleiro(
        tabuleiroJogador,
        "TABULEIRO DO JOGADOR"
    )

    # JOGADOR POSICIONA NAVIOS
    posicionando_navios_jogador(
        tabuleiroJogador
    )

    # COMPUTADOR POSICIONA NAVIOS
    posicionando_navios_computador(
        tabuleiroComputador
    )

    # INÍCIO DO JOGO
    while True:

        mostrar_tabuleiro(
            feedbackJogador,
            f"ATAQUES DE {nome} NO COMPUTADOR"
        )

        mostrar_tabuleiro(
            tabuleiroJogador,
            "SEUS NAVIOS"
        )

        ataque_jogador(
            tabuleiroComputador,
            feedbackJogador
        )

        if contar_navios(tabuleiroComputador) == 0:

            print("\n🏆 VOCÊ VENCEU!")
            break

        print("\n💻 Computador está pensando...")
        time.sleep(0.2)

        print('...', end="")
        time.sleep(1)
        print()

        ataque_computador(
            tabuleiroJogador,
            feedbackComputador
        )


        if contar_navios(tabuleiroJogador) == 0:

            print("\n💻 O COMPUTADOR VENCEU!")
            break
    
    print(f"\nObrigado por jogar, {nome}!")

    print("\n===== CRÉDITOS =====")
    print("Desenvolvido por:")
    print("Guilherme Matos Brum de Oliveira")
    print("Gustavo Povoas Schulz")
    print("Lucas Maeshiba Ikeda")

# Executa o programa
if __name__ == "__main__":
    main()