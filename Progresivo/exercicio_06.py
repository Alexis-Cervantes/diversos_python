# 3. Faça um Programa que leia três números inteiros e mostre o maior deles.
v1 = int(input("Digite primeiro valor: "))
v2 = int(input("Digite segundo valor: "))
v3 = int(input("Digite terceiro valor: "))

maior = v1

if v2 > maior:
    maior = v2
if v3 > maior:
    maior = v3

print(f'O maior é: {maior}')
