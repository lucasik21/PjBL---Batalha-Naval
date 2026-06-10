matriz10x10 = [
    [ 0,  1, 2, 3, 4, 5 , 6, 7, 8, 9, 10,],
    ["A", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ["B", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ["C", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ["D", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ["E", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ["F", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ["G", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ["H", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ["I", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ["J", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
for i in range(11):
     print(matriz10x10[i])



def cordBarcos():   
    print()
    print("para começar escolhe a onde quer deixar seus barcos")
    for escolhas in range (1, 6):
        print()
        print(f" --Escolha o barco numero {escolhas}-- ")
        print()
        while True:
            linha = int(input("digite uma linha de 0 a 10: "))
            linha = linha + 1
            coluna = int(input("agr uma coluna de 0 a 10: "))
            coluna = coluna + 1
            linha_certa = linha in range(1, 10)
            coluna_certa = coluna in range(1, 10)

            if linha_certa and coluna_certa:
                matriz10x10[linha][coluna] = 1
                for i in range(11):
                    print(matriz10x10[i])
                print("✅ Posição registrada com sucesso!")
                break

            if not linha_certa and not coluna_certa:
                print("❌ Você errou tudo! Tente novamente.\n")
        
            elif not linha_certa:
             print("❌ Você digitou uma linha que não existe! Tente novamente.\n")
        
            elif not coluna_certa:
                print("❌ Você digitou uma coluna que não existe! Tente novamente.\n")
    for i in range(11):
        print(matriz10x10[i])

cordBarcos()