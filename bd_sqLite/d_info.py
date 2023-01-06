import sqlite3 # fonte: Banco de dados SQLite com Python (Eletronica e programação)
try:
    # CRIA BANCO DE DADOS
    banco = sqlite3.connect('bank.db')

    # INSTANCIAR PARA ONDE APONTA O BD
    cursor = banco.cursor()

    # INSIRE DADOS NA TABELA:
    cursor.execute("DELETE from pessoas WHERE nome = 'alexis'")

    # APLICA AS INSERÇÕES MA TABELA:
    banco.commit()

    # FECHAR O BD
    banco.close()
    print('Os dados foram removidos com sucesso!!!')

except sqlite3.Error as erro:
    print("Erro ao excluir: ", erro)
