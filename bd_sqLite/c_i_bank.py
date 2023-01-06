import sqlite3 # fonte: Banco de dados SQLite com Python (Eletronica e programação)

# INSERINDO DADOS MA TABELA MEDIANTE VARIAVEIS
nome = 'Olga'
idade = 77
email = 'olgita@gmail.com'

# CRIA BANCO DE DADOS
banco = sqlite3.connect('bank.db')

# INSTANCIAR PARA ONDE APONTA O BD
cursor = banco.cursor()

# CRIA TABELA NO BD:
""" cursor.execute("CREATE TABLE pessoas(nome text, idade integer, email text)") """

# INSIRE DADOS NA TABELA:
""" cursor.execute("INSERT INTO pessoas VALUES('"+nome+"', "+str(idade)+", '"+email+"')") """

# SUBSTITUIR VALOR
cursor.execute("UPDATE pessoas SET nome = 'IncaDigital' WHERE idade = 48 ")

# APLICA AS INSERÇÕES MA TABELA:
banco.commit()

# VER OS DADOS INSERIDOS NO BD VIA TERMINAL
""" cursor.execute("SELECT * FROM pessoas")
print(cursor.fetchall()) """

