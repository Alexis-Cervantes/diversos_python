from random import randint
from time import sleep
print('==== Desafio 28====')
'''Escreva um programa que faça o computador "pensar" em um numero enteiro entre 0 e 5, e peça ao usuario tentar descobrir qual foi o numero escolhido
pelo computador. O programa devera escrever na tela se o usuario venceu ou perdeu'''
nr = int(input('Digite o numero: '))
numero = randint(0, 5)
print('Processando...')
sleep(3)
if nr == numero:
    print(f'Voce VENCEU!!! O computador processou o numero: {numero}')
else:
    print(f'Você PERDEU!!! O computador processado pela maquina foi: {numero}')

