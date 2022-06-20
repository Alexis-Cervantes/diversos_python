num1=int(input('Digite um numero: '))
num2=int(input('Digite outro: '))
s=num1+num2
# 1ro modo: ===> print('A soma entre:',num1,'e',num2,'vale:',s)
# 2do modo: ===> print('A soma entre {} e {} vale {}'.format(num1, num2 , s))
# 3ro modo: 
print('A soma entre {0} e {1} vale {2}'.format(num1 , num2 , s))