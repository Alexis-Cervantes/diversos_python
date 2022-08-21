print('==== Desafio 20====')
'''O mesmo professor do desafio anterior quer sortear a orden de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos 4 alunos e mostre a orden sorteada'''
from random import shuffle
a = str(input('Primeiro aluno: '))
b = str(input('Segundo aluno: '))
c = str(input('Terceiro aluno: '))
d = str(input('Quarto aluno: '))
aluno = [a, b, c, d]
shuffle(aluno)
print(f'A ordem da lista é: {aluno}')