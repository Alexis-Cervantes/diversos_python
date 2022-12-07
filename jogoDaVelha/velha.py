X = "X"
O = "O"
VAZIO = " "

# Lista criada para exemplificar as posições da lista
# tabuleiro = [0, 1, 2,
#              3, 4, 5,
#              6, 7, 8]

# LAGUNS TESTES:

# VENCE O 'X'
# tabuleiro = [X, O, X,
#              O, X, O,
#              O, VAZIO, X]

# VAZIO
# tabuleiro = [VAZIO, VAZIO, VAZIO,
#              VAZIO, VAZIO, VAZIO,
#              VAZIO, VAZIO, VAZIO]

# VENCE O 'O'
# tabuleiro = [X, O, X,
#              X, X, VAZIO,
#              O, O, O]

# DEU VELHA - EMPATE
# tabuleiro = [X, O, X,
#              O, X, O,
#              O, X, O]
# variavel FLAG para criar uma indicação que algo aconteceu 
alinhamento = False 
vencedor = VAZIO
# -------------------------horizontal---------------------------
# if tabuleiro[0] == tabuleiro[1] == tabuleiro[2]:
#     print("O jogo acabou")
# if tabuleiro[3] == tabuleiro[4] == tabuleiro[5]:
#     print("O jogo acabou")
# if tabuleiro[6] == tabuleiro[7] == tabuleiro[8]:
#     print("O jogo acabou")

# Reemplazando as estruturas condicionais pelas interações com for e range
for i in range(0, 9, 3):
    if tabuleiro[i] == tabuleiro[i+1] == tabuleiro[i+2] != VAZIO:
        # print("O jogo acabou")
        alinhamento = True
        vencedor = tabuleiro[i]
# --------------------------vertical-------------------------------
# if tabuleiro[0] == tabuleiro[3] == tabuleiro[6]:
#     print("O jogo acabou")
# if tabuleiro[1] == tabuleiro[4] == tabuleiro[7]:
#     print("O jogo acabou")
# if tabuleiro[2] == tabuleiro[5] == tabuleiro[8]:
#     print("O jogo acabou")

# Reemplazando as estruturas condicionais pelas interações com for e range
if not alinhamento:
    for i in range(3):
        if tabuleiro[i] == tabuleiro[i+3] == tabuleiro[i+6] != VAZIO:
            # print("O jogo acabou")
            alinhamento = True
            vencedor = tabuleiro[i]
# -------------------------diagonal-----------------------------------
# if tabuleiro[0] == tabuleiro[4] == tabuleiro[8]:
#     print("O jogo acabou")
# if tabuleiro[2] == tabuleiro[4] == tabuleiro[6]:
#     print("O jogo acabou")

# Reemplazando as estruturas condicionais pelas interações com for e range
if not alinhamento:
    for i in range(0, 3, 2):
        if tabuleiro[0+i] == tabuleiro[4] == tabuleiro[8-i] != VAZIO:
            # print("O jogo acabou")
            alinhamento = True
            vencedor = tabuleiro[i]
# Para mostrar na tela quem venceu:
if alinhamento:
    print("Vencedor: ", vencedor)
else:
# Para verificar se todos os espaçõs foram preenchidos e deu EMPATE
    if not VAZIO in tabuleiro:
        print("Jogo empatou: Deu velha!")