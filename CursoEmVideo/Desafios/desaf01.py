print('==== Desafio 01 ====')
''' Crie um script python que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas de acordo com o valor digitado '''
nome = input('Qual é seu nome?: ')
# declarando variavel ---> saludo = ('Prazer em te conhecer!!')
# esto tambien funciona ---> print('Olá',nome,saludo)
print('É um prazer te conhecer {}!'.format(nome))        