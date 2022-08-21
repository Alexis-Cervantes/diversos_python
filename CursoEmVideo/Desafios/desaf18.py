from bs4 import Tag


from math import sin, cos, tan, radians, fabs
print('==== Desafio 18====')
'''Escreva um programa que leia um angulo qualquer e monstre na tela o valor seno, coseno e tangente desse angulo'''
angulo = float(input('Digite o valor do angulo: '))
seno = sin(radians(angulo))
coseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print(f'O Seno de {str(angulo)}° é iagual a: {seno:.2f}.\nO Coseno de {fabs(angulo)}° é igaul a: {coseno:.2f}.\nA tangente de {fabs(angulo)}° é igual a: {tangente:.2f}.')
