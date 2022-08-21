from gettext import find


print('==== Desafio 22====')
'''Crie um programa que leia o nome completo de uma pessoa e mostre: 
1) O nome com todas as letras MAISCULAS...OK
2) O nome com todas as minusculas...ok
3) Quantas letras ao todo (sem considerar espaços)
4) Quantas letras tem o primeiro nome'''
nome = str(input('Digite seu nome: ')).strip()
print(f'Seu nome completo em "MAUISCULO" é: {nome.upper()}')
print(f'Seu nome completo em minusculo é: {nome.lower()}')
print('Seu nome têm {}: '.format(len(nome) - nome.count(' ')), 'letras. Sem contar espaçoes')
print(f'O primeiro nome têm {nome.find(' ')}')
