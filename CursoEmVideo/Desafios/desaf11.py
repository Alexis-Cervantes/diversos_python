print('==== Desafio 11 ===')
# Faça um programa que leia a largura e altura de uma parede em metros, calcule a sua área e a quantidade de tinta nesesaria para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m²                       
l = int(input('Digite a largura da parede: '))
a = int(input('Diggite a altura da parede: '))
area = l*a
tinta = 2
print('A área têm: {} m² e se necessita: {} litros para poder pintá-la!'.format(area,area/tinta))