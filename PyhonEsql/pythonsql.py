import pyodbc

dados_conexao = (
    "Driver = {SQL Server};"
    "Server = IncaDigitalReload;"
    "Database = PythonSQL;"
)
conexao = pyodbc.connect(dados_conexao)
print("Conexão bêm Sucesida")
