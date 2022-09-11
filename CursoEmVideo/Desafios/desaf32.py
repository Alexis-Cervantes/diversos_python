from datetime import date
print('==== Desafio 32====')
'''Faça um programa que leia um ano qualquer e mostre se ele é bissexto'''
year = int(input('Qual anor deseja analizar? Ou Coloque "0" se quer analizar ano atual: '))
if year == 0: 
   year = date.today().year
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:    
    print(f'O ano de {year} é BISSEXTO')
else:
    print(f'O ano {year} Não é BISSEXTO')
