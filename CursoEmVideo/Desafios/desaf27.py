print('==== Desafio 27====')
'''Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o ultimo nome separadamente:
exe: alexis cervantes 
primeri: alexis
ultimo: cervantes'''
n = str(input('Digite seu nome: ')).strip()
nome = n.split()
print(f'Primer nome: {nome[0]}')
print(f'ultimo nome: {nome[len(nome) - 1]}')
