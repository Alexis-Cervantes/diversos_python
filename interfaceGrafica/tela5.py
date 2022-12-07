# Como Construir uma Ferramenta de Cadastro no Python: 'Hashtag Programação'
# 1) Importar as mi nhas bibliotecas
import tkinter as tk
from tkinter import ttk
import datetime as dt

lista_tipos = ['Galão', 'Caixa', 'Saco', "Unidade"]
lista_codigos = []
# 2) Criar Interface Graficas
ventana = tk.Tk()
# Criação da função:
def inserir_codigo():
     descricao = entrada_descricao.get()
     tipo = lista_suspensa_tipo_unidade.get()
     quant = entrada_quantidade_tipo_unidade.get()
     data_criacao = dt.datetime.now()
     data_criacao = data_criacao.strftime('%/%M/%Y %H:%M')
     codigo = len(lista_codigos)+1
     codigo_str = "COD - {}".format(codigo)
     lista_codigos.append((codigo_str, descricao, tipo, quant, data_criacao))

# titulo de la ventana
ventana.title("Herramienta de Cadastro de Materiais")
# Etiquetas y Entradas
etiqueta_descricao = tk.Label(text="Descrição de materiais")
etiqueta_descricao.grid(row=1, column=0,padx=10, pady=10, sticky='nswe', columnspan=4)

entrada_descricao = tk.Entry()
entrada_descricao.grid(row=2, column=0, padx=10, pady=10, sticky='nswe', columnspan=4)

etiqueta_tipo_unidade = tk.Label(text="Tipo da unidad do Material")
etiqueta_tipo_unidade.grid(row=3, column=0, padx=10, pady=10, sticky='nswe', columnspan=2)

lista_suspensa_tipo_unidade = ttk.Combobox(values=lista_tipos)
lista_suspensa_tipo_unidade.grid(row=3, column=2, padx=10, pady=10, sticky='nswe', columnspan=2)

etiqueta_quantidade_tipo_unidade = tk.Label(text="Quantidade na unidade de material")
etiqueta_quantidade_tipo_unidade.grid(row=4, column=0, padx=10, pady=10, sticky='nswe', columnspan=2)

entrada_quantidade_tipo_unidade = tk.Entry()
entrada_quantidade_tipo_unidade.grid(row=4, column=2, padx=10, pady=10, sticky='nswe', columnspan=2)

boton_criar_codigo = tk.Button(text='Criar Código', command=inserir_codigo)
boton_criar_codigo.grid(row=5, column=0, padx=10, pady=10, sticky='nswe', columnspan=4)

ventana.mainloop()
print(lista_codigos)
     