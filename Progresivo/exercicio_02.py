# 2.Faça um script que peça um valor e mostre na tela se o valor é positivo ou negativo

v = int(input("Digite um valor inteiro: "))

if v > 0:
    print(f"O valor {v} é POSITIVO")
else:
    if v == 0:
        print(f"O valor é {v}")
    else:
        print(f"O valor {v} é NEGATIVO")