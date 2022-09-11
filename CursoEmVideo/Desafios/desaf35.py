print('==== Desafio 35====')
'''Desenvolva um programa que leia o comprimento de tres retas e diga ao usuario se eles podem ou não formar um triangulo'''
r1 = float(input('Digite o valor da 1era reta: '))
r2 = float(input('Digite o valor da 2do reta: '))
r3 = float(input('Digite o valor da 3er reta: '))
if r1 < (r2 + r3) and r2 < (r1 + r3) and r3 < (r1 + r2):
    print('Podem se formar um triangulo: ')
else:
    print('Não pode-se formar um triangulo')
