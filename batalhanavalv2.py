import random
import time
import sys

PORTA_AVIOES = "🛫"
NAVIO_TANQUE = "⛴️"
CONTRATORPEDEIRO = "🚢"
SUBMARINO = "🚤"
DESTROIER = "🛥️"

AGUA = "🌊"
ACERTO = "❌"
ERRO = "⭕"

FROTA = [
    (PORTA_AVIOES, 5),
    (NAVIO_TANQUE, 4),
    (CONTRATORPEDEIRO, 3),
    (SUBMARINO, 2),
    (DESTROIER, 1)
]

def verifica_navio(valor):
    return valor in [
        PORTA_AVIOES,
        NAVIO_TANQUE,
        CONTRATORPEDEIRO,
        SUBMARINO,
        DESTROIER
    ]
# Fazer o jogo da Batalha Naval, utilizando 4 matrizes, e cada uma sendo para certo modo de jogo: tabuleiro_jogador, feedback_jogador, tabuleiro_computador, feedback_computador.
def tela_inicial():
    print("=" * 40)
    print("        🚢 BATALHA NAVAL 🚢")
    print("=" * 40)

    jogador = input("Digite seu nome: ")

    print("\nBem-vindo,", jogador)
    print("Prepare-se para a batalha!\n")

    return jogador


def criar_tabuleiro():
    matriz = []
    for i in range(10):
        linha = []
        for j in range(10):
            
            linha.append(AGUA)
        matriz.append(linha)
    return matriz

def mostrar_tabuleiro(tabuleiro, titulo):
    letras = [" A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]

    print("\n====== {} ======".format(titulo))
    
  
    print("     {}".format("  ".join(letras)))

    for i in range(len(tabuleiro)):
        linha_formatada = ""

        for elemento in tabuleiro[i]:
            linha_formatada += "{:<3}".format(elemento)

        print("{:2} | {}".format(i + 1, linha_formatada))

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

            print("💥 ACERTOU UMA EMBARCAÇÃO!")

            feedbackJogador[linha][coluna] = ACERTO
            tabuleiroComputador[linha][coluna] = AGUA

            print("Navios restantes do computador:", contar_navios(tabuleiroComputador))

        # Errou
        else:

            print("Água!")

            feedbackJogador[linha][coluna] = ERRO

        break

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

        print("\nComputador atacou:",
              linha + 1,
              chr(coluna + 65))

        if verifica_navio(tabuleiroJogador[linha][coluna]):

            print("💥 O computador acertou um navio!")

            feedbackComputador[linha][coluna] = ACERTO
            tabuleiroJogador[linha][coluna] = AGUA

            print("Seus navios restantes:", contar_navios(tabuleiroJogador))

        else:

            print("🌊 O computador errou!")

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

    mostrar_tabuleiro(
    tabuleiroComputador,
    "TABULEIRO DO COMPUTADOR (TESTE)"
)
    # INÍCIO DO JOGO
    while True:

        mostrar_tabuleiro(
            feedbackJogador,
            f"ATAQUES DE {nome} NO COMPUTADOR"
        )

        ataque_jogador(
            tabuleiroComputador,
            feedbackJogador
        )

        if contar_navios(tabuleiroComputador) == 0:

            print("\n🏆 VOCÊ VENCEU!")
            break

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