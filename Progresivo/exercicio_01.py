# 1.Faça um programa que peça dois números e imprima o maior deles.

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

if n1 > n2:
    print(f"O primeiro número é MAIOR: {n1} ")
else:
    if n1 == n2:
        print(f"Os dois númneros são iguais: {n1} {n2}")
    else: 
        print(f"O segundo número é MAIOR: {n2}")