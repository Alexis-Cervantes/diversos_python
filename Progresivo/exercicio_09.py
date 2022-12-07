# 6. Faça um Programa que leia três números e mostre-os em ordem decrescente.

n1 = int(input('Digite primeiro valor: '))
n2 = int(input('Digite segundo valor: '))
n3 = int(input('Digite terceiro valor: '))

print(f"Números na ordem digitada: {n1}, {n2}, {n3}")
# esquerda pra direita (Invertir a ordem do ultimo para seguda posição)
if n3 > n2:
    aux = n3
    n3 = n2
    n2 = aux
# esquerda pra direita (Invertir a ordem do segundo para primeira posição)
if n2 > n1:
    aux = n2
    n2 = n1
    n1 = aux
# esquerda pra direita (Voltamos a Invertir a ordem do terceiro para segunda posição)
if n3 > n2:
    aux = n3
    n3 = n2
    n2 = aux
print(f"Os numeros em ordem decrescente: {n1}, {n2}, {n3}") 


