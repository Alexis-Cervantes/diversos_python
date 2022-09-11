print('==== Desafio 23====')
'''Faça um programa que leia um numero de 0 a 9999 e mostre na tela cada um dos digitos separados
ejemplo: digitr 1974
unidades = 4
decenas = 7
centena = 9
milhares 1'''
num = int(input('Digite um numero entre "0" e "9999": '))
uni = (num // 1) % 10
dec = (num // 10) % 10
cen = (num // 100) % 10
mil = (num // 1000) % 10
print(f'{int(uni)} : Unidades')
print(f'{int(dec)} : Decenas')
print(f'{int(cen)} : Centenas')
print(f'{int(mil)} : Millar')