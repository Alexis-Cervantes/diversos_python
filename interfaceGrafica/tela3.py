from tkinter import *
'''Interface basica - Usando biblioteca tkinter - fuente: "https://www.devmedia.com.br/tkinter-interfaces-graficas-em-python/33956"'''
class Aplicacion:
    # Codigo que crea el Layout
    def __init__(self, master=None):
        self.widget1 = Frame(master)
        self.widget1.pack()
        self.msg = Label(self.widget1, text='Primer Widget')
        self.msg['font'] = ('Calibri', '20', 'italic')
        self.msg.pack ()
        self.salir = Button(self.widget1)
        self.salir['text'] = 'Clique Aqui'
        self.salir['font'] = ('Calibri', '15')
        self.salir['width'] = 10
        # self.sair["command"] = self.widget1.quit
        self.salir['command'] = self.cambiarText # Modo 1: Pasar el command como atributo del widget. La funcion "cambiarText(self), solo nesecita "self" como parametro.
        # self.salir.bind('<Button-1>', self.cambiarText) --- # Modo 2: Metodo bind (inir). Referecia a la funcion "mudarText(self, event). Tiene que estar como parametros self e event
        self.salir.pack ()  # self.salir.pack (side=RIGHT) para posicionar el botão a lado derecho del widget1
    # Funcion que realiza el evento 
    def cambiarText(self):
        if self.msg['text'] == 'Primer Widget':
            self.msg['text'] = 'Estamos en "IF" pq el evento encontro la frase "Primeiro widget", haz clic de nuevo e veras lo que pasa!'
        else:
            self.msg['text'] = 'Estamos en el ELSE ahora pq el evento no encontro la frase "Primeiro widget", ahora el evento no saldra mas de aqui...GENIAL NO!!!'
raiz = Tk()
Aplicacion(raiz)
raiz.mainloop()