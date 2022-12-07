# Importando bibliotecas
import sqlite3 as lite
# Instanciar a biblioteca lite em variavel 'con' e logo e conectar nosso banco de dados
con = lite.connect('dados.bd')  
# Criando tabela
with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE inventorio (id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, local TEXT, descricao TEXT, marca TEXT, data_da_compra DATE, valor_da_compra DECIMAL, serie TEXT, imagem TEXT)")
        