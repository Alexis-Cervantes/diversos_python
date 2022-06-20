print('==== Desafio 13 ===')
# Faça um algoritmo que leia o salario de um funcionario e mostre seu novo salario, com 15 % de aumento.
s = float(input('Digite o valor do seu salario: '))
aumento = (s)+(s*0.15)
print('Seu salario inicialmente era de R$ {}. Com o novo aumento ficaria em: R$ {}'.format(s, aumento))