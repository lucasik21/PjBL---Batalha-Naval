# Fazer o jogo da Batalha Naval, utilizando 4 matrizes, e cada uma sendo para certo modo de jogo: tabuleiro_jogador, feedback_jogador, tabuleiro_computador, feedback_computador.
import random

def criar_tabuleiro():
    matriz = []
    for i in range(10):
        linha = []
        for j in range(10):
            
            linha.append("🌊")
        matriz.append(linha)
    return matriz

def mostrar_tabuleiro(tabuleiro, titulo):
    letras = [" A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]

    print("\n=== {} ===".format(titulo))
    
  
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

            
            if tabuleiro[linha][coluna] == "🛥️ ":
                print("Já existe um navio nessa posição!")
                continue

            
            tabuleiro[linha][coluna] = "🛥️ "
            
            mostrar_tabuleiro(tabuleiro, "TABULEIRO DO JOGADOR")
            break

def posicionando_navios_computador(tabuleiro):
    for i in range(5):
        while True:
            linha = random.randint(0, 9)
            coluna = random.randint(0, 9)

            if tabuleiro[linha][coluna] == "🛥️":
                continue
            tabuleiro[linha][coluna] = "🛥️"
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
        if feedbackJogador[linha][coluna] != "🌊":
            print("Você já atacou essa posição!")
            continue

        # Acertou um navio
        if tabuleiroComputador[linha][coluna] == "🛥️":

            print("💥 ACERTOU UMA EMBARCAÇÃO!")

            feedbackJogador[linha][coluna] = "❌"

            # Remove o navio do tabuleiro oculto
            tabuleiroComputador[linha][coluna] = "💥"
            print("Navios restantes do computador:", contar_navios(tabuleiroComputador))

        # Errou
        else:

            print("Água!")

            feedbackJogador[linha][coluna] = "⭕"

        break

def contar_navios(tabuleiro):

    quantidade = 0

    for linha in tabuleiro:
        for elemento in linha:
            if elemento == "🛥️":
                quantidade += 1

    return quantidade

def ataque_computador(tabuleiroJogador, feedbackComputador):

    while True:

        linha = random.randint(0, 9)
        coluna = random.randint(0, 9)

        if feedbackComputador[linha][coluna] != "🌊":
            continue

        print("\nComputador atacou:",
              linha + 1,
              chr(coluna + 65))

        if tabuleiroJogador[linha][coluna] == "🛥️":

            print("💥 O computador acertou um navio!")

            feedbackComputador[linha][coluna] = "❌"

            tabuleiroJogador[linha][coluna] = "💥"
            print("Seus navios restantes:", contar_navios(tabuleiroJogador))

        else:

            print("🌊 O computador errou!")

            feedbackComputador[linha][coluna] = "⭕"

        break

def main():

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
            "SEUS ATAQUES NO COMPUTADOR"
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

    print("\nObrigado por jogar!")

# Executa o programa
if __name__ == "__main__":
    main()