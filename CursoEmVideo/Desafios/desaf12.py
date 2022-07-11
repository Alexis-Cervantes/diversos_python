print('==== Desafio 12 ===')
# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de dscto. 
p = float(input('Digite o valor do item: '))
novo = (p) - (p*0.05)
print('O valor inicial do item é de: R$ {:.2f}. O novo valor do produto com um desconto de 5 % é de: R$ {:.2f}'.format(p, novo))