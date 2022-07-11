print('==== Desafio 11 ===')
# Faça um programa que leia a largura e altura de uma parede em metros, calcule a sua área e a quantidade de tinta nesesaria para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m².                       
l = float(input('Digite a largura da parede: '))
a = float(input('Diggite a altura da parede: '))
area = l*a
tinta = 2
print('A área da parede é de: {:.2f} m². E você necessita de: {:.2f} litros de tinta para poder pintá-la!'.format(area,area/tinta))