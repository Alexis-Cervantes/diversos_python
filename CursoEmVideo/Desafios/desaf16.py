from math import trunc
print('==== Desafio 16 ====')
'''Escreva um programa que leia um numero real qualquer pelo teclado e monstre a sua porção inteira .'''
while True:
    num = float(input('Informe o valor: '))
    print(f'O valor digitado é: {num } e a sua porção inteira é {trunc(num)}.')
    preg = ' '
    preg = str(input('Desea continuar: [S/N]:')).strip().upper()
    if preg == 'N':
        print('programa acabou...')
        break 
