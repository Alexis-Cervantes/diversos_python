from email.policy import default
from PySimpleGUI import PySimpleGUI as sg

class PantallaPython:
    # Criando el Metodo Construtor
    def __init__ (self):
        # sg.theme_previewer() --- para previsualizar los temas disponibles
        # theme_name_list = sg.theme_list() --- para obter lista de temas
        # print(theme_name_list) --- segunda parate para obtener lista de temas
        sg.theme('Dark Blue 16')
        # Contrução do Layot
        estructura = [
            [sg.Text('Nombre:', size=(6,0)), sg.Input(size=(15,0), key='name')],
            [sg.Text('Edad:', size=(6,0)), sg.Input(size=(15,0), key='age')],
            [sg.Text('¿Cuál proveedores de e-mail son aceptados?')],
            [sg.Checkbox('Gmail', key='gmail'), sg.Checkbox('Outlook', key='outlook'), sg.Checkbox('Yahoo', key='yahoo')],
            [sg.Text('Acepta Cartão:')],
            [sg.Radio('Si', 'Tarjetas', key='aceptaTarjetas'), sg.Radio('No', 'Tarjetas', key='noAceptaTarjetas')],
            [sg.Text('Velocidad de Envio:')],
            [sg.Slider(range=(0, 255), default_value=0, orientation='h', size=(15, 20), key='sliderVelocidad')],
            [sg.Button('Enviar Datos')],
            [sg.Output(size=(30,20))]
        ]
        # Contrução de uma janela
        self.ventana = sg.Window('Datos de Usuario').layout(estructura)
    # Creando el Metodo iniciar
    def Iniciar(self):
        # inicialmente colocamos esta funcion - print(self.values)
        # Para mantener a ventana abierta colocamos un 'While True' y delante de todo el codido lo siguiente:
        while True:
            # Extração dos dados
            self.button, self.values = self.ventana.Read()
            nombre = self.values['name']
            edad = self.values['age']
            acepta_gmail = self.values['gmail']
            acepta_outlook = self.values['outlook']
            acepta_yahoo = self.values['yahoo']
            acepta_tarjeta = self.values['aceptaTarjetas']
            no_acepta_tarjeta = self.values['noAceptaTarjetas']
            velocidad_scrip = self.values['sliderVelocidad']
            print(f'Nombre: {nombre}')
            print(f'Edad: {edad}')
            print(f'Acepta Gmail: {acepta_gmail}')
            print(f'Acepta Outlook: {acepta_outlook}')
            print(f'Acepta Yahoo: {acepta_yahoo}')
            print(f'Acepta Tarjetas: {acepta_tarjeta}')
            print(f'No acepta Tarjetas: {no_acepta_tarjeta}')
            print(f'Velocidad Scrip: {velocidad_scrip}')
# instanciando objetos y Llamando el metodo o funcion Iniciar
pantalla = PantallaPython()
pantalla.Iniciar()