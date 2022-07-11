# nome = input('Digite seu nome:')
# print('Prazer em te conhecer {:=^20}!'.format(nome))
n1 = int(input('Um valor: '))
n2 = int(input('Outro Valor: '))
# print('A soma vale: {}'.format(n1+n2))
s = n1+n2
m = n1*n2
d = n1/n2
di = n1//n2
e = n1**n2
print('A soma é: {}, O produto é: {}; a divisão é: {:.3f}'.format(s,m,d), end='. ')
print('a divisão Inteira é: {} e a potenciação é: {}'.format(di,e))