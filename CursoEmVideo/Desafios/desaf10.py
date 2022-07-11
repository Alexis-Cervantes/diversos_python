print('==== Desafio 10 ===')
# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dolares ela pode comprar. Considere US$ 1.00 = R$ 3.27
d = float(input('Diga o valor do dinheiro que vc têm: '))
cambio = 3.27
print('Com R$ {:.2f} Você pode comprar US$ {:.2f}'.format(d, d/cambio))