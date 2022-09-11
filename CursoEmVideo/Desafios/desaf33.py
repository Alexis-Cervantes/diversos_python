print('==== Desafio 33====')
'''Faça um programa que leia tres numeros e mostre qual é maior e qual é o menor'''
n1 = int(input('Digite 1er. número: '))
n2 = int(input('Digite 2do. número: '))
n3 = int(input('Digite 3er. número: '))
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n3:
    menor = n3 
print(f'O numero maior é: {maior}')
print(f'O numero menor é: {menor}')

