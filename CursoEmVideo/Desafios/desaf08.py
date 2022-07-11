print('==== Desafio 08 ===')
# Escreva um programa que leia o valor en metros e o exiba convertida em cm e mm.
valor = int(input('Digite um valor: '))
valorcm = valor*100
valormm = valor*1000
print('{} Metros convertido a Centimetros é: {} cm, e convertido em Milimetros é {} mm'.format(valor, valorcm, valormm))