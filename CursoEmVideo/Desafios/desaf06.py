print('==== Desafio 06 ===')
# Crie um algoritmo que leia um numero e mostre o seu dobro, triplo e sua raiz quadrada.
import math
num = int(input('Digite um numero: '))
print('O dobro de {} é: {}'.format(num, (num*2)))
print('O triplo de {} é: {}'.format(num, (num*3)))
# print('A raiz quadrada de {} é: {:.2f}'.format(num, num**(1/2)))
print('A raiz quadrada de {} é: {}'.format(num, math.sqrt(num)))