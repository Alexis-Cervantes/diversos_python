from sys import displayhook
from tracemalloc import start
from pandas_datareader import data as web
import pandas as pd
import matplotlib.pyplot as plt

# Pegar cotações de um site
#cotacao_bovespa = web.DataReader('^BVSP', data_source='yahoo', start='01/01/2021', end='02/01/2021')
# displayhook(cotacao_bovespa)
# cotacao_bovespa['Adj Close'].plot(figsize=(15, 10))
# plt.show()

# cotacao_petr = web.DataReader('PETR4.SA', data_source='yahoo', start='01-01-2021', end='02-01-2021')
# displayhook(cotacao_petr)
# cotacao_petr['Adj Close'].plot(figsize=(15, 10))
# plt.show()

# Pegar cotações de uma tabela excel (Açoes de empresas)
tabela_empresas = pd.read_excel('Cotacoes/Empresas.xlsx')
displayhook(tabela_empresas)

for empresa in tabela_empresas['Empresas']:
    print(empresa)
    cotacao = web.DataReader(f'{empresa}.SA', data_source='yahoo', start='01-01-2021', end='02-01-2021')
    displayhook(cotacao)
    cotacao['Adj Close'].plot(figsize=(15, 10))
    plt.show()
