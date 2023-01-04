# Importando bibliotecas
import sqlite3 as lite
# Instanciar a biblioteca lite em variavel 'con' e logo e conectar nosso banco de dados.
con = lite.connect('dados.bd')

# ---------------- INSERIR DADOS EM TABELA-------------------------- 
def inserir_form(i):
    with con:
        # Instanciamos a variavel 'con' fazendo o curso Apontar para o banco criado.
        cur = con.cursor()
        query = "INSERT INTO inventorio (nome, local, descricao, marca, data_da_compra, valor_da_compra, serie, imagem) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
        cur.execute(query, i)

# -----------------ATUALIZAR DADOS EM TABELA:------------------------
def atualizar_(i):
    with con:
        # Instanciamos a variavel 'con' fazendo o curso Apontar para o banco criado.
        cur = con.cursor()
        query = "UPDATE inventorio SET nome=?, local=?, descricao=?, marca=?, data_da_compra=?, valor_da_compra=?, serie=?, imagem=? WHERE id=?"
        cur.execute(query, i)

# -------------------DELETAR DADOS DA TABELA:------------------------
#deletar_dados = str(2)
def deletar_form(i):
    with con:
        # Instanciamos a variavel 'con' fazendo o curso Apontar para o banco criado
        cur = con.cursor()
        query = "DELETE FROM inventorio WHERE id=?"
        cur.execute(query, i)

# -------------------VER DADOS EM TABELA: 
#(Antes de consultar deve comentar a Inserção de dados).
def ver_form():
    ver_dados = []
    with con:
        # Instanciamos a variavel 'con' fazendo o curso Apontar para o banco criado
        cur = con.cursor()
        query = "SELECT * FROM inventorio"
        cur.execute(query)

        rows = cur.fetchall()
        for row in rows:
            ver_dados.append(row)
#print(ver_dados)
    return ver_dados

# -------------------VER DADOS INDIVIDUALMENTE: 
def ver_item(id):
    ver_dados_individual = []
    with con:
        # Instanciamos a variavel 'con' fazendo o curso Apontar para o banco criado
        cur = con.cursor()
        query = "SELECT * FROM inventorio WHERE id=?"
        cur.execute(query, id)

        rows = cur.fetchall()
        for row in rows:
            ver_dados_individual.append(row)
            
    return ver_dados_individual
