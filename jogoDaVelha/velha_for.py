X = "X"
O = "O"
VAZIO = " "

# VAZIO
tabuleiro = [VAZIO, VAZIO, VAZIO,
             VAZIO, VAZIO, VAZIO,
             VAZIO, VAZIO, VAZIO]

# Lista criada para exemplificar as posições da lista
# tabuleiro = [0, 1, 2,
#              3, 4, 5,
#              6, 7, 8]

casa = int(input("Escolha onde jogar: "))
tabuleiro[casa] = X

# TODO: verificar se o jog acabou

