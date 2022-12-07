# 4. Faça um Programa que leia três números inteiros, em seguida mostre o maior e o menor deles.
v1 = int(input("Digite primeiro valor: "))
v2 = int(input("Digite segundo valor: "))
v3 = int(input("Digite terceiro valor: "))

maior = v1
if v2 > maior:
    maior = v2
if v3 > maior:
    maior = v3
print(f'O MAIOR é: {maior}')
menor = v1
if v2 < menor:
    menor = v2
if v3 < menor:
    menor = v3
print(f'O menor é: {menor}')