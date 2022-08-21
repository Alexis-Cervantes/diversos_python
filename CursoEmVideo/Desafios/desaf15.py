print('==== Desafio 15 ====')
'''Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$ 0,15 por Km rodado.'''
kms = float(input('Diga quantos kms o carro percorreu: '))
dias = int(input("Informe a quantidade de dias utilizados: "))
preco = dias*60 + kms*0.15
print(f'O preço a pagar é de: R${preco}')

