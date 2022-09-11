print('==== Desafio 29====')
'''Escreva um programa que leia a velocidadde de um carro. Se ele ultrapassar 80KM/h, mostre uma msg dizendo que ele foi multado. A multa vai custar R$ 7.00
por cada Km acima do limite'''
vel = float(input('Digite a velocidade atual do carro: '))
if  vel > 80:
    multa = (vel - 80) * 7 
    print(f'Você ultrapassou o limite permitido de velicidade em {vel - 80}, esta MULTADO com: {multa} ')
else: 
    print('Você esta dentro do limite perimido!!!')