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

n = random.randint(1, 10)