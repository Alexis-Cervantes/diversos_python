from math import sqrt, pow, hypot
print('==== Desafio 17 ====')
'''Escreva um programa que leia o comprimento de um cateto oposto e do cateto adjacente de um triangulo rectangulo, calcule e mostre o comprimento da hipotenusa'''
b = float(input('Digite o valor do cateto oposto: '))
c = float(input('Digite o valor do cateto adjacente: '))
# a = sqrt(pow(b, 2) + pow(c, 2))
a = hypot(b, c)
print(f'O valor da hipotenusa é: {a:.2f}')