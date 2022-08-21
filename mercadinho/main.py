'''Aqui vamos a cosntruir um programa que solcite a um usuario una lista de compras. O programa mostra lista de items'''
print('='*10, '"Mercadinho Todo dia"', '='*10)
print('Menu\n1) Lista\n2) Salir')
op1 = int(input('Escolha uma opção: '))
sacola = []
lista = ['Arroz', 'Azucar', 'Carne', 'Ovos']
if op1 == 1:
    print(lista)
    op2 = str(input('Escolha um produto: '))
    if 'Arroz' in lista: 
        print(op2)
    elif 'Azucar' in lista:
        print(op2)
else:
    print('Volte sempre...')
