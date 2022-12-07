from tkinter import *
'''Interface basica - Recibiendo datos del usuario - Usando biblioteca tkinter - fuente: "https://www.devmedia.com.br/tkinter-interfaces-graficas-em-python/33956"'''
class Aplicacion:
    def __init__(self, master=None):
        
        self.fuente1 = ('Arial', '10')
       
        self.cont1 = Frame(master) # Estilo Contenedor 1
        self.cont1['pady'] = 10 
        self.cont1.pack()
       
        self.cont2 = Frame(master) # Estilo Contenedor 2
        self.cont2['padx'] = 20
        self.cont2.pack()
       
        self.cont3 = Frame(master) # Estilo Contenedor 3
        self.cont3['padx'] = 20
        self.cont3.pack()
        
        self.cont4 = Frame(master) # Estilo Contenedor 4
        self.cont4['padx'] = 20
        self.cont4.pack()
        
        self.titulo = Label(self.cont1, text='Datos de Usuario') # Estilo Titulo corresponde al Contenedor 1 
        self.titulo['font'] = ('Arial', '10', 'bold')
        self.titulo.pack()
        
        self.nombretiqueta = Label(self.cont2, text='Nombre:', font=self.fuente1)# Creando el nombre de la etiqueta 'Nombre'
        self.nombretiqueta.pack(side=LEFT)
      
        self.nombre = Entry(self.cont2)  # Creando el input de la etiqueta "nombre" con la clase "Entry"
        self.nombre['width'] = 30
        self.nombre['font'] = self.fuente1
        self.nombre.pack(side=LEFT)
        
        self.clavetiqueta = Label(self.cont3, text='Password:', font=self.fuente1) # Creando el nombre de la etiqueta del password con el nombre 'Clave'
        self.clavetiqueta.pack(side=LEFT)
        
        self.clave = Entry(self.cont3) # Creando el input de la etiqueta "clave" con la clase "Entry"
        self.clave['width'] = 30
        self.clave['font'] = self.fuente1
        self.clave['show'] = '*'
        self.clave.pack(side=LEFT)
        
        self.boton = Button(self.cont4) # Creando el Boton con el nombre de 'Enviar" y al mismo tiempo verificando el password con la funcion 'verificarClave'
        self.boton['text'] = 'Enviar'
        self.boton['font'] = ('Calibri', '8')
        self.boton['width'] = 12
        self.boton['command'] = self.verificaClave
        self.boton.pack()
        
        self.msg = Label(self.cont4, text='', font=self.fuente1) # Creando el mensage que saldra despues de validar nombre y clave
        self.msg.pack()
    
    def verificaClave(self): # Function/Metodo "Verificar Password"
        usuario = self.nombre.get()
        password = self.clave.get()
        if usuario == 'Alexis' and password == '608248':
            self.msg['text'] = 'Verificado!!!'
        else:
            self.msg['text'] = 'Error en la verificación!!!'
raiz = Tk() # Instaciamos la clase "Tk()" a travez de la variavel "raiz". A clase Tk() permite que los widget sean usados en la aplicacion.
Aplicacion(raiz) # Pasamos como parametro la variavel "raiz", al metodo constructor de la clase Aplicacion; 
raiz.mainloop() # Llamamos el metodo raiz.mainloop para exibir la vetana en la panatalla
