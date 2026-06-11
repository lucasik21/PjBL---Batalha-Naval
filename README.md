# PjBL---Batalha-Naval
Projeto feito em Python para desenvolver habilidades proposto pela professora Marina da PUCPR
 Descrição
O jogador posiciona sua frota manualmente no tabuleiro e tenta afundar os navios do computador antes que o computador afunde os seus. O computador posiciona e ataca de forma aleatória
.
Fluxo do jogo

1. **Tela inicial** — Digite seu nome para começar.
2. **Posicionamento** — Para cada navio da frota, informe:
   - Linha inicial (1–10)
   - Coluna (A–J)
   - Direção: **H** (horizontal) ou **V** (vertical)
3. **Rodadas** — Jogador e computador se alternam atacando:
   - Informe linha e coluna para atacar o tabuleiro do computador.
   - O computador ataca aleatoriamente o seu tabuleiro.
4. **Fim de jogo** — Vence quem afundar toda a frota adversária primeiro.

*Funções Principais
| `tela_inicial()' : Exibe o menu e captura o nome do jogador |
| `criar_tabuleiro()` | Cria uma matriz 10x10 preenchida com água |
| `mostrar_tabuleiro()` | Exibe o tabuleiro formatado no terminal |
| `posicionando_navios_jogador()` | Permite ao jogador posicionar sua frota manualmente |
| `posicionando_navios_computador()` | Posiciona a frota do computador aleatoriamente |
| `ataque_jogador()` | Processa o ataque do jogador |
| `ataque_computador()` | Gera e processa o ataque aleatório do computador |
| `contar_navios()` | Conta as células de navio restantes em um tabuleiro |
| `verifica_navio()` | Verifica se um valor corresponde a um navio |
.
*Desenvolvedores
Guilherme Matos Brum de Oliveira
Gustavo Povoas Schulz
Lucas Maeshiba Ikeda
- Guilherme Matos Brum de Oliveira
- Gustavo Povoas Schulz
- Lucas Maeshiba Ikeda
