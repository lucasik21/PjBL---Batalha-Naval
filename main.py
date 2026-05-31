# Fazer o jogo da Batalha Naval, utilizando 4 matrizes, e cada uma sendo para certo modo de jogo: tabuleiro_jogador, feedback_jogador, tabuleiro_computador, feedback_computador.
import random

def criar_tabuleiro():
    matriz = []
    for i in range(10):
        linha = []

        for j in range(10):
            linha.append("-")

        matriz.append(linha)
    return matriz

def mostrar_tabuleiro(tabuleiro, titulo):
    letras = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]

    print("=== {} ===".format(titulo))
    print("     {}".format(" ".join(letras)))

    for i in range(len(tabuleiro)):
        print("{:2} | {}".format(i + 1, " ".join(tabuleiro[i])))

def posicionando_navios_jogador(tabuleiro):

    letras = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]

    for i in range(5):

        while True:
            print("\nPosicionando navio {}".format(i + 1))

            linha = int(input("Linha (1-10): ")) - 1
            coluna = input("Coluna (A-J): ").upper()

            if linha < 0 or linha > 9:
                print("Linha inválida!")
                continue

            if coluna not in letras:
                print("Coluna inválida!")
                continue

            coluna = letras.index(coluna)

            if tabuleiro[linha][coluna] == "N":
                print("Já existe um navio nessa posição!")
                continue

            tabuleiro[linha][coluna] = "N"
            mostrar_tabuleiro(tabuleiro, "TABULEIRO DO JOGADOR")
            break

def main():
    tabuleiro = criar_tabuleiro()

    mostrar_tabuleiro(tabuleiro, "TABULEIRO DO JOGADOR")

    posicionando_navios_jogador(tabuleiro)

    mostrar_tabuleiro(tabuleiro, "TABULEIRO DO JOGADOR")

main()