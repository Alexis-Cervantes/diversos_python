print('==== Desafio 26====')
'''Faça um programa que leia uma frase pelo teclado e mostre: 
1) Quantas vezes aparace a letra 'A'
2) Em que posição ela aparece a primeira vez
3) Em que posição ela aparece a ultima vez'''
frase = str(input('Digite a frase: ')).lower().strip()
la = frase.count('a')
lap = frase.find('a')+1 
lau = frase.rfind('a')+1
print(f'A letra "A" aparace: {la} vezes')
print(f'A letra "A" aparace na {lap} posicion')
print(f'A letra "A" aparace na {lau} posicion')

