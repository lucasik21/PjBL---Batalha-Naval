import random
import time
import sys

matriz10x10 = [
    [ "",  "  1️⃣ "," 2️⃣  ",  "3️⃣ ", " 4️⃣ ", " 5️⃣ ", " 6️⃣ ", " 7️⃣ ", " 8️⃣ ", " 9️⃣ ", " 🔟 ",],
    ["1️⃣ ", "🌊 ", "🌊 ", "🌊 ", "🌊 ", "🌊 ", "🌊 ", "🌊 ", "🌊 ", "🌊 ", "🌊 "],
    ["2️⃣ ", "🌊 ", "🌊 ", "🌊 ", "🌊 ", "🌊 ", "🌊 ", "🌊 ", "🌊 ", "🌊 ", "🌊 "], 
    ["3️⃣ ", "🌊 ", "🌊 ", "🌊 ", "🌊 ", "🌊 ", "🌊 ", "🌊 ", "🌊 ", "🌊 ", "🌊 "],
    ["4️⃣ ", "🌊 ", "🌊 ", "🌊 ", "🌊 ", "🌊 ", "🌊 ", "🌊 ", "🌊 ", "🌊 ", "🌊 "],
    ["5️⃣ ", "🌊 ", "🌊 ", "🌊 ", "🌊 ", "🌊 ", "🌊 ", "🌊 ", "🌊 ", "🌊 ", "🌊 "],
    ["6️⃣ ", "🌊 ", "🌊 ", "🌊 ", "🌊 ", "🌊 ", "🌊 ", "🌊 ", "🌊 ", "🌊 ", "🌊 "],
    ["7️⃣ ", "🌊 ", "🌊 ", "🌊 ", "🌊 ", "🌊 ", "🌊 ", "🌊 ", "🌊 ", "🌊 ", "🌊 "],
    ["8️⃣ ", "🌊 ", "🌊 ", "🌊 ", "🌊 ", "🌊 ", "🌊 ", "🌊 ", "🌊 ", "🌊 ", "🌊 "],
    ["9️⃣ ", "🌊 ", "🌊 ", "🌊 ", "🌊 ", "🌊 ", "🌊 ", "🌊 ", "🌊 ", "🌊 ", "🌊 "],
    ["🔟", "🌊 ", "🌊 ", "🌊 ", "🌊 ", "🌊 ", "🌊 ", "🌊 ", "🌊 ", "🌊 ", "🌊 "]
    ]
for i in range(11):
     print(*matriz10x10[i])



def cordBarcosH():   
    print()
    print("para começar escolhe a onde quer deixar seus barcos")
    for escolhas in range (1, 6):
        print()
        print(f" --Escolha o barco numero {escolhas}-- ")
        print()
        while True:
            linha = int(input("digite uma linha de 1 a 10: "))
            coluna = int(input("agr uma coluna de 1 a 10: "))
            linha_certa = linha in range(1, 11)
            coluna_certa = coluna in range(1, 11)

            if linha_certa and coluna_certa:
                matriz10x10[linha][coluna] = "🛥️  "
                for i in range(11):
                    print(*matriz10x10[i])
                print("✅ Posição registrada com sucesso!")
                break

            if not linha_certa and not coluna_certa:
                print("❌ Você errou tudo! Tente novamente.\n")
        
            elif not linha_certa:
             print("❌ Você digitou uma linha que não existe! Tente novamente.\n")
        
            elif not coluna_certa:
                print("❌ Você digitou uma coluna que não existe! Tente novamente.\n")
    for i in range(11):
        print(*matriz10x10[i])

cordBarcosH()

print()
print()
print()
print("vez do bot")

def computador_pensando(segundos_totais=3):
    print("O computador está pensando", end="")
    
    # Cada ciclo de 3 pontinhos leva cerca de 1.5 segundos
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

print()
print()

matriz10x10R = [
    [ "",  "  1️⃣ "," 2️⃣  ",  "3️⃣ ", " 4️⃣ ", " 5️⃣ ", " 6️⃣ ", " 7️⃣ ", " 8️⃣ ", " 9️⃣ ", " 🔟 ",],
    ["1️⃣ ", "🌊 ", "🌊 ", "🌊 ", "🌊 ", "🌊 ", "🌊 ", "🌊 ", "🌊 ", "🌊 ", "🌊 "],
    ["2️⃣ ", "🌊 ", "🌊 ", "🌊 ", "🌊 ", "🌊 ", "🌊 ", "🌊 ", "🌊 ", "🌊 ", "🌊 "],
    ["3️⃣ ", "🌊 ", "🌊 ", "🌊 ", "🌊 ", "🌊 ", "🌊 ", "🌊 ", "🌊 ", "🌊 ", "🌊 "],
    ["4️⃣ ", "🌊 ", "🌊 ", "🌊 ", "🌊 ", "🌊 ", "🌊 ", "🌊 ", "🌊 ", "🌊 ", "🌊 "],
    ["5️⃣ ", "🌊 ", "🌊 ", "🌊 ", "🌊 ", "🌊 ", "🌊 ", "🌊 ", "🌊 ", "🌊 ", "🌊 "],
    ["6️⃣ ", "🌊 ", "🌊 ", "🌊 ", "🌊 ", "🌊 ", "🌊 ", "🌊 ", "🌊 ", "🌊 ", "🌊 "],
    ["7️⃣ ", "🌊 ", "🌊 ", "🌊 ", "🌊 ", "🌊 ", "🌊 ", "🌊 ", "🌊 ", "🌊 ", "🌊 "],
    ["8️⃣ ", "🌊 ", "🌊 ", "🌊 ", "🌊 ", "🌊 ", "🌊 ", "🌊 ", "🌊 ", "🌊 ", "🌊 "],
    ["9️⃣ ", "🌊 ", "🌊 ", "🌊 ", "🌊 ", "🌊 ", "🌊 ", "🌊 ", "🌊 ", "🌊 ", "🌊 "],
    ["🔟", "🌊 ", "🌊 ", "🌊 ", "🌊 ", "🌊 ", "🌊 ", "🌊 ", "🌊 ", "🌊 ", "🌊 "]
    ]


def barco():
    n = random.randint(1, 11)
    g = random.randint(1, 11)
    matriz10x10R[n][g] = "🛥️  "
        
for n in range(5):
    barco()

item_procurado = "🛥️  "

total = sum(linha.count(item_procurado) for linha in matriz10x10R)

while total <5:
    barco()
    total = sum(linha.count(item_procurado) for linha in matriz10x10R)




#a partir daqui e o 1v1
matriz10x10RD = [ [ "",  "  1️⃣ "," 2️⃣  ",  "3️⃣ ", " 4️⃣ ", " 5️⃣ ", " 6️⃣ ", " 7️⃣ ", " 8️⃣ ", " 9️⃣ ", " 🔟 ",],
    ["1️⃣ ", "🌊 ", "🌊 ", "🌊 ", "🌊 ", "🌊 ", "🌊 ", "🌊 ", "🌊 ", "🌊 ", "🌊 "],
    ["2️⃣ ", "🌊 ", "🌊 ", "🌊 ", "🌊 ", "🌊 ", "🌊 ", "🌊 ", "🌊 ", "🌊 ", "🌊 "],
    ["3️⃣ ", "🌊 ", "🌊 ", "🌊 ", "🌊 ", "🌊 ", "🌊 ", "🌊 ", "🌊 ", "🌊 ", "🌊 "],
    ["4️⃣ ", "🌊 ", "🌊 ", "🌊 ", "🌊 ", "🌊 ", "🌊 ", "🌊 ", "🌊 ", "🌊 ", "🌊 "],
    ["5️⃣ ", "🌊 ", "🌊 ", "🌊 ", "🌊 ", "🌊 ", "🌊 ", "🌊 ", "🌊 ", "🌊 ", "🌊 "],
    ["6️⃣ ", "🌊 ", "🌊 ", "🌊 ", "🌊 ", "🌊 ", "🌊 ", "🌊 ", "🌊 ", "🌊 ", "🌊 "],
    ["7️⃣ ", "🌊 ", "🌊 ", "🌊 ", "🌊 ", "🌊 ", "🌊 ", "🌊 ", "🌊 ", "🌊 ", "🌊 "],
    ["8️⃣ ", "🌊 ", "🌊 ", "🌊 ", "🌊 ", "🌊 ", "🌊 ", "🌊 ", "🌊 ", "🌊 ", "🌊 "],
    ["9️⃣ ", "🌊 ", "🌊 ", "🌊 ", "🌊 ", "🌊 ", "🌊 ", "🌊 ", "🌊 ", "🌊 ", "🌊 "],
    ["🔟", "🌊 ", "🌊 ", "🌊 ", "🌊 ", "🌊 ", "🌊 ", "🌊 ", "🌊 ", "🌊 ", "🌊 "]
]

pontosJogador = 0 
pontosBot = 0 


def jogadaPlayer():
    while True: 
        linha = int(input("digite uma linha de 1 a 10:"))
        coluna = int(input("digite uma coluna de 1 a 10:"))
        
        if linha in range(1, 11) and coluna in range(1, 11):
            
            alvo = matriz10x10R[linha][coluna]
            if alvo == "🛥️  ":
                pontosJogador = pontosJogador + 1
                print("vc acertou um barco inimigo!")
                matriz10x10RD[linha][coluna] = "💥"
                for i in range(11):
                    print(*matriz10x10RD)
            elif alvo == "🌊 ":
                print("errrrrouuuuuuu(agua)")
                matriz10x10RD[linha][coluna] = "✖️"
                for i in range(11):
                    print(*matriz10x10RD)
                break
            elif alvo == "✖️ ":
                print("errrrrouuuu(casa ja explorada)")
                for i in range(11):
                    print(*matriz10x10RD)
                break
            else:
                print("errrrrouuuu(casa ja explorada)")
                for i in range(11):
                    print(*matriz10x10RD)
                break
        else:
            print("cordenadas incorretas, tente dnv:")

def jogadaBot():
    h = random.randint(1, 11)
    j = random.randint(1, 11)
    linhaBot = h
    colunaBot = j
    while True:
        alvoBot = matriz10x10[linhaBot][colunaBot]
        if alvoBot == "🛥️  ":
            pontosBot = pontosBot + 1
            print("o bot acertou seu barco")
            matriz10x10[linhaBot][colunaBot] = "💥"
            for i in range(11):
                print(*matriz10x10)
        elif alvoBot == "🌊":
            print("o bot errou")
            matriz10x10[linhaBot][colunaBot] = "✖️"
            for i in range(11):
                print(*matriz10x10)
            break
        elif alvoBot == "✖️":
            print("o bot errou(casa ja explorada)")
            for i in range(11):
                print(*matriz10x10)
            break
        else:
            print("errrrrouuuu(casa ja explorada)")
            for i in range(11):
                print(*matriz10x10)
            break

def rodadas():
    while True:
        jogadaPlayer()
        jogadaBot()

        if pontosJogador == "5":
            print("vc ganhou")
            break
        elif pontosBot == "5":
            print("o bot ganhou, vc perdeu")
            break







