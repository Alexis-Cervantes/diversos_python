import requests
from tkinter import *

def extraerCotizaciones():
    solicitud = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")

    requisicao_dic = solicitud.json()

    cotizacion_dolar = requisicao_dic['USDBRL']['bid']
    cotizacion_euro = requisicao_dic['EURBRL']['bid']
    cotizacion_btc = requisicao_dic['BTCBRL']['bid']

    texto = f'''
    Dólar: {cotizacion_dolar}
    Euro: {cotizacion_euro}
    BTC: {cotizacion_btc}'''

    et_infoCotizaciones['text'] = texto
    # print(texto) --- Imprime la informacion de la variable texto
# extraerCotizaciones() ---> Inicialmente usado para llamar a la Funcion.
ventana = Tk()

ventana.title('Cotización Actual de Monedas')
ventana.geometry('320x400')

et_TxtInformativo = Label(ventana, text='Clique en el boton para ver las cotizaciones de monedas')
et_TxtInformativo.grid(column=0, row=0, padx=10, pady=10)

bt_TxtInformativo = Button(ventana, text='Buscar cotizaciones Dólar - Euro - BTC', command=extraerCotizaciones)
bt_TxtInformativo.grid(column=0, row=1, padx=10, pady=10)

et_infoCotizaciones = Label(ventana, text='')
et_infoCotizaciones.grid(column=0, row=2, padx=10, pady=10)

ventana.mainloop()