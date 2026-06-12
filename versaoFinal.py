
import random
import time
import sys

matriz10x10 = [
    ["", " 1️⃣", " 2️⃣", " 3️⃣", " 4️⃣", " 5️⃣", " 6️⃣", " 7️⃣", " 8️⃣", " 9️⃣", " 🔟"],
    ["1️⃣", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊"],
    ["2️⃣", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊"],
    ["3️⃣", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊"],
    ["4️⃣", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊"],
    ["5️⃣", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊"],
    ["6️⃣", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊"],
    ["7️⃣", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊"],
    ["8️⃣", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊"],
    ["9️⃣", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊"],
    ["🔟","🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊"]
]

def print_matriz(matriz):
    for linha in matriz:
        print(*[celula + " " for celula in linha])

print_matriz(matriz10x10)

def cordBarcosH():   
    print()
    print("Para começar, escolha onde quer deixar seus barcos")
    for escolhas in range(1, 6):
        print()
        print(f" -- Escolha o barco número {escolhas} -- ")
        print()
        while True:
            try:
                linha = int(input("Digite uma linha de 1 a 10: "))
                coluna = int(input("Agora uma coluna de 1 a 10: "))
            except ValueError:
                print("❌ Por favor, digite números válidos.\n")
                continue

            linha_certa = linha in range(1, 11)
            coluna_certa = coluna in range(1, 11)

            if linha_certa and coluna_certa:
                if matriz10x10[linha][coluna] == "🛥️":
                    print("❌ Já existe um barco nessa posição! Escolha outra.\n")
                    continue
                matriz10x10[linha][coluna] = "🛥️"
                print_matriz(matriz10x10)
                print("✅ Posição registrada com sucesso!")
                break

            if not linha_certa and not coluna_certa:
                print("❌ Você errou tudo! Tente novamente.\n")
    
            elif not linha_certa:
                print("❌ Você digitou uma linha que não existe! Tente novamente.\n")
    
            elif not coluna_certa:
                print("❌ Você digitou uma coluna que não existe! Tente novamente.\n")
    print_matriz(matriz10x10)

cordBarcosH()

print("\n\n\nVez do bot")

def computador_pensando(segundos_totais=3):
    print("O computador está pensando", end="")
    
    ciclos = int(segundos_totais / 0.7)
    
    for _ in range(ciclos):
        for _ in range(3):
            time.sleep(0.5)
            print(".", end="")
            sys.stdout.flush()
            
        time.sleep(0.5)
        print("\b\b\b   \b\b\b", end="")
        sys.stdout.flush()
        
computador_pensando(3)

print("\n\n")

# Tabuleiro do bot
matriz10x10R = [
    ["", "1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣", "7️⃣", "8️⃣", "9️⃣", "🔟"],
    ["1️⃣", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊"],
    ["2️⃣", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊"],
    ["3️⃣", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊"],
    ["4️⃣", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊"],
    ["5️⃣", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊"],
    ["6️⃣", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊"],
    ["7️⃣", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊"],
    ["8️⃣", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊"],
    ["9️⃣", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊"],
    ["🔟", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊"]
]

def barco():
    while True:
        n = random.randint(1, 10)
        g = random.randint(1, 10)
        if matriz10x10R[n][g] != "🛥️":
            matriz10x10R[n][g] = "🛥️"
            break

for _ in range(5):
    barco()

# Confere quantos barcos existem e adiciona mais até 5
item_procurado = "🛥️"
total = sum(linha.count(item_procurado) for linha in matriz10x10R)
while total < 5:
    barco()
    total = sum(linha.count(item_procurado) for linha in matriz10x10R)

# Tabuleiro de resultados do jogador para o tabuleiro do bot
matriz10x10RD = [
    ["", "1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣", "7️⃣", "8️⃣", "9️⃣", "🔟"],
    ["1️⃣", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊"],
    ["2️⃣", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊"],
    ["3️⃣", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊"],
    ["4️⃣", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊"],
    ["5️⃣", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊"],
    ["6️⃣", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊"],
    ["7️⃣", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊"],
    ["8️⃣", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊"],
    ["9️⃣", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊"],
    ["🔟", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊", "🌊"]
]

pontosJogador = 0
pontosBot = 0

def jogadaPlayer():
    global pontosJogador
    while True:
        try:
            linha = int(input("Digite uma linha de 1 a 10: "))
            coluna = int(input("Digite uma coluna de 1 a 10: "))
        except ValueError:
            print("❌ Por favor, digite números válidos.\n")
            continue

        if linha in range(1, 11) and coluna in range(1, 11):
            alvo = matriz10x10R[linha][coluna]
            if alvo == "🛥️":
                pontosJogador += 1
                print("Você acertou um barco inimigo!")
                matriz10x10RD[linha][coluna] = "💥"
                print_matriz(matriz10x10RD)
            elif alvo == "🌊":
                print("Errou (água)!")
                matriz10x10RD[linha][coluna] = "✖️"
                print_matriz(matriz10x10RD)
                break
            elif alvo in ["✖️", "💥"]:
                print("Casa já explorada, tente outra posição!")
                print_matriz(matriz10x10RD)
                continue
            else:
                print("Casa já explorada, tente outra posição!")
                print_matriz(matriz10x10RD)
                continue
        else:
            print("Coordenadas incoras, tente novamente.")

def jogadaBot():
    global pontosBot
    while True:
        linhaBot = random.randint(1, 10)
        colunaBot = random.randint(1, 10)
        alvoBot = matriz10x10[linhaBot][colunaBot]
        if alvoBot == "🛥️":
            pontosBot += 1
            print("O bot acertou seu barco!")
            matriz10x10[linhaBot][colunaBot] = "💥"
            print_matriz(matriz10x10)
            break
        elif alvoBot == "🌊":
            print("O bot errou!")
            matriz10x10[linhaBot][colunaBot] = "✖️"
            print_matriz(matriz10x10)
            break
        elif alvoBot in ["✖️", "💥"]:
            print("Já tentou essa posição, tenta outra")
            continue
        else:
            print("O bot errou (casa já explorada)")
            print_matriz(matriz10x10)
            break

def rodadas():
    while True:
        jogadaPlayer()
        jogadaBot()

        if pontosJogador == 5:
            print("Você ganhou!")
            break
        elif pontosBot == 5:
            print("O bot ganhou, você perdeu!")
            break


rodadas()
print("obrigado por jogar")
print("membros:")
print("gustavo schulz!")
print("lucas ikeda!")
print("guilherme matos!")









