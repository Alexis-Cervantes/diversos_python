# nome = input('Digite seu nome:')
# print('Prazer em te conhecer {:=^20}!'.format(nome))
n1 = int(input('Um vaalor: '))
n2 = int(input('Outro Valor: '))
# print('A soma vale: {}'.format(n1+n2))
s = n1+n2
m = n1*n2
d = n1/n2
di = n1//n2
e = n1**n2
print('A Soma é {}, O produto é {} e divisão é {:.3f}'.format(s,m,d), end=' ')
print('Divisão Inteira {} e potencia é {}'.format(di,e))