# PjBL---Batalha-Naval

 ## Descrição
Projeto de **Batalha Naval** em Python, criado para a disciplina de Raciocínio Algorítmico da professora Marina.

Funcionando via terminal e desta vez, com a adição de funções, último conteúdo visto na matéria.

## Execução do Projeto
Ele funciona via Python, então é necessário da linguagem instalada na sua máquina, normalmente utilizado nas IDEs (PyCharm e VSCode)

## Como jogar
O jogo ocorre em turnos:

- O jogador escolhe uma posição para atacar o tabuleiro inimigo
- O computador realiza ataques aleatórios
- O sistema indica:
  - 💥 Acerto
  - 🌊 Água
  - 💀 Navio afundado

Controles
- Linhas: `1 a 10`
- Colunas: `A a J`

## Fluxo do jogo

1. **Tela inicial** — Digite seu nome para começar.
2. **Posicionamento** — Para cada navio da frota, informe:
   - Linha inicial (1–10)
   - Coluna (A–J)
   - Direção: **H** (horizontal) ou **V** (vertical)
3. **Rodadas** — Jogador e computador se alternam atacando:
   - Informe linha e coluna para atacar o tabuleiro do computador.
   - O computador ataca aleatoriamente o seu tabuleiro.
4. **Fim de jogo** — Vence quem afundar toda a frota adversária primeiro.

## Humano x Máquina
Fizemos o modo de jogador humano contra uma máquina que a partir da biblioteca random, faz sua jogada.

# Considerações Finais
No desenvolvimento do código, tivemos dificuldade na formatação do tabuleiro, para deixar visivelmente paralelo e organizado, já que utilizamos emojis e seu caractere depende da fonte e como é tratado.
Foi feito o desafio, com muito esforço já que tem diferentes embarcações com seus diferentes tamanhos, 

Feito por:
- Guilherme Matos Brum de Oliveira
- Gustavo Povoas Schulz
- Lucas Maeshiba Ikeda