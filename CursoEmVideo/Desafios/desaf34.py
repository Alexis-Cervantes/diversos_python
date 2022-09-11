print('==== Desafio 34====')
'''Escreva um programa que pergunte o salario de um fucnionario e calcule o valor do seu aumento. Para salarios supeiores a R$ 1.250,00, calcule 
um aumento de 10%. Para os infeiores ou iguais, o aumento é de 15%'''
sal = float(input('Digite seu salario: '))
if sal > 1250:
    aumento = sal + (sal*0.1)
    print(f'O salario informado é R$ {sal} reias. O novo salario após o aumento em 10% é de: R${aumento:,.2f} reais') 
else:
    print(f'O salario informado é R$ {sal} reais. O novo salario após o aumento em 15% é de: R${(sal + (sal*0.15)):,.2f} reais')

