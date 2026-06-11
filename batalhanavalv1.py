import random
import time
import sys

NAVIO = "🛥️ "
AGUA = "🌊"
ACERTO = "❌"
ERRO = "⭕"

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
        print("{:2} | {}".format(i + 1, " ".join(tabuleiro[i])))

def posicionando_navios_jogador(tabuleiro):
    letras = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]

    for i in range(5):
        while True:
            print("\nPosicionando navio {}".format(i + 1))

            try:
                linha = int(input("Linha (1-10): ")) - 1
            except ValueError:
                print("Linha inválida! Digite apenas números.")
                continue
                
            coluna = input("Coluna (A-J): ").upper()

            if linha < 0 or linha > 9:
                print("Linha inválida!")
                continue

            if coluna not in letras:
                print("Coluna inválida!")
                continue

            coluna = letras.index(coluna)

            
            if tabuleiro[linha][coluna] == NAVIO:
                print("Já existe um navio nessa posição!")
                continue

            
            tabuleiro[linha][coluna] = NAVIO
            
            mostrar_tabuleiro(tabuleiro, "TABULEIRO DO JOGADOR")
            break

def posicionando_navios_computador(tabuleiro):
    for i in range(5):
        while True:
            linha = random.randint(0, 9)
            coluna = random.randint(0, 9)

            if tabuleiro[linha][coluna] == NAVIO:
                continue
            tabuleiro[linha][coluna] = NAVIO
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
        if tabuleiroComputador[linha][coluna] == NAVIO:

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
            if elemento == NAVIO:
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

        if tabuleiroJogador[linha][coluna] == NAVIO:

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