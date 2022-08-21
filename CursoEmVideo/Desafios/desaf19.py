print('==== Desafio 19====')
'''Um professor quer sortear um dos seus 4 alunos para apagara o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido'''
from random import choice
a = str(input('Digite o nome do primer aluno: '))
b = str(input('Digite o nome do segubdo aluno: '))
c = str(input('Digite o nome do terceiro aluno: '))
d = str(input('Digite o nome do quarto aluno: '))
aluno = [a, b, c, d]
print(f'O aluno escolhido é: {choice(aluno)}')