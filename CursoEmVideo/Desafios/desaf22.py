from gettext import find

print('==== Desafio 22====')
'''Crie um programa que leia o nome completo de uma pessoa e mostre: 
1) O nome com todas as letras MAISCULAS...OK
2) O nome com todas as minusculas...ok
3) Quantas letras ao todo (sem considerar espaços)
4) Quantas letras tem o primeiro nome'''
nome = str(input('Digite seu nome: ')).strip()
print(f'Su nombre completo en "MAIUSCULO" é: {nome.upper()}')
print(f'Su nombre completo en minusculo é: {nome.lower()}')
print(f'Su nombre têm: {len(nome) - nome.count(" ")} letras sin contar con lo espacios en blanco')
print(f'El primer nombre tiene: {nome.find(" ")}')
