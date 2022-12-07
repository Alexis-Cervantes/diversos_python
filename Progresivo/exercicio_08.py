# 5. Faça um programa que pede dois inteiro e armazene em duas variáveis. Em seguida, troque o valor das variáveis e exiba na tela

valor1 = int(input('Digite 1er Valor: '))
valor2 = int(input('Digite 2do Valor: '))

print(f"\nprimer valor: {valor1}")
print(f"segundo valor: {valor2}")
print('\nInvirtindo valores')

aux = valor2
valor2 = valor1
valor1 = aux

print(f"\nPrimer valor: {valor1}")
print(f"segudo valor: {valor2}")
