# 3.Crie um programa que verifique se uma letra digitada é "F" ou "M". 
# Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

print("Menu:\nF - Femenino\nM - Masculino\nSexo Inválido")

op = input("Digite uma opção do menu para validar: ").upper()

if op == 'F':
    print(f"Você digitou {op} - Femenino")
else: 
    if op == 'M':
        print(f"Você digitou {op} - Masculino")
    else:
        print("Sexo Invalido")