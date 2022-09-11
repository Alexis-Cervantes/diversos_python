print('==== Desafio 31====')
'''Desenvolva um programa que pergunte a distancia de uma viagem em Km. Calcule o preço da passagem, cobrando R$ 0.50 por Km para viagens de até 200 Km e
R$ 0.45 para viagens mais longos  '''
dist = float(input('Digite a distancia a percorrer: '))
if dist <= 200:
    print(f'A distancia esta dentro dos 200 Km de distancia. O valor da passagem é de: {dist * 0.5 }')
else:
    print(f'A distancia ultrapassa os 200 Km de distancia. O valor da passagem é de: {dist * 0.45}')

