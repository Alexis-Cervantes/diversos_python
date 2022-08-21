from calendar import HTMLCalendar
from cgitb import html
from email.message import Message
import pandas as pd
import win32com.client as win32
# Importar a base de dados
tabela_vendas = pd.read_excel('MiniCurso/Vendas.xlsx')
print('-'*45)
# visualizar a base de dados
# pd.set_option('display.max_columns', None)
# print(tabela_vendas)
# faturamento por loja
faturamento = tabela_vendas[['ID Loja', 'Valor Final']].groupby('ID Loja').sum()
print(faturamento)
print('-'*45)
# quantidade de produtos vendidos por loja
quantidade = tabela_vendas[['ID Loja', 'Quantidade']].groupby('ID Loja').sum()
print(quantidade)
print('-'*45)
# tiket medio por produto em cada loja
tiket_mediio = (faturamento['Valor Final'] / quantidade['Quantidade']).to_frame()
tiket_mediio = tiket_mediio.rename(columns={0: 'Tiket Medio'})
print(tiket_mediio)
# enviar ee-mail com e=o relatorio
outlook = win32.Dispatch('outlook.application')
mail = outlook.CreateItem(0)
mail.to = 'obonecoalex@gmail.com'
mail.Subject = 'Relatorio de vendas por Loja'
mail.HTMLBody = f'''
<p>Prezados:</p> 
<p>Segue Relatorio de vendas por cada loja...</p>
<p>Faturamento:</p>
{faturamento.to_html(formatters={'Valor Final': 'R${:,.2f}'.format})}

<p>Quantidade Vendida:</p>
{quantidade.to_html()}

<p>Ticket medio dos produto em cada Loja</p>
{tiket_mediio.to_html(formatters={'Tiket Medio': 'R${:,.2f}'.format})}

<p>Qualquer duvida estou a sua disposição...</p>

<p>Att.,</p>
<p>Alexis Cervantes</p>
'''
mail.Send()
print('e-mail enviado')