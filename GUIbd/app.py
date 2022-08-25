from usuarios import Usuarios
from tkinter import *

class Aplicacion:

    def __init__(self, master = None):
        self.fuente1 = ('verdana', '8')

        self.cont1 = Frame(master)
        self.cont1['pady'] = 10
        self.cont1.pack()

        self.cont2 = Frame(master)
        self.cont2['padx'] = 20
        self.cont2['pady'] = 5
        self.cont2.pack()

        self.cont3 = Frame(master)
        self.cont3['padx'] = 20
        self.cont3['pady'] = 5
        self.cont3.pack()

        self.cont4 = Frame(master)
        self.cont4['padx'] = 20
        self.cont4['pady'] = 5
        self.cont4.pack()

        self.cont5 = Frame(master)
        self.cont5['padx'] = 20
        self.cont5['pady'] = 5
        self.cont5.pack()

        self.cont6 = Frame(master)
        self.cont6['padx'] = 20
        self.cont6['pady'] = 5
        self.cont6.pack()

        self.cont7 = Frame(master)
        self.cont7['padx'] = 20
        self.cont7['pady'] = 5
        self.cont7.pack()

        self.cont8 = Frame(master)
        self.cont8['padx'] = 20
        self.cont8['pady'] = 10
        self.cont8.pack()
        
        self.cont9 = Frame(master)
        self.cont9['pady'] = 15
        self.cont9.pack()

        self.etiquetatitulo = Label(self.cont1, text = 'Informe los Datos: ')
        self.etiquetatitulo['font'] = ('calibri', '12', 'bold')
        self.etiquetatitulo.pack()

        self.etiquetaidusuario = Label(self.cont2, text = 'idUsuario: ', font = self.fuente1, width = 10)
        self.etiquetaidusuario.pack(side = LEFT)

        self.txtidusuario = Entry(self.cont2)
        self.txtidusuario['width'] = 10
        self.txtidusuario['font'] = self.fuente1
        self.txtidusuario.pack(side = LEFT)

        self.botonBuscar = Button(self.cont2, text = 'Buscar', font = self.fuente1, width = 10)
        self.botonBuscar['command'] = self.buscarUsuario
        self.botonBuscar.pack(side = RIGHT)

        self.etiquetanombre = Label(self.cont3, text = 'Nombre: ', font = self.fuente1, width = 10)
        self.etiquetanombre.pack(side = LEFT)

        self.txtnombre = Entry(self.cont3)
        self.txtnombre['width'] = 25
        self.txtnombre['font'] = self.fuente1
        self.txtnombre.pack(side = LEFT)

        self.etiquetatelefono = Label(self.cont4, text = 'Telefono: ', font = self.fuente1, width = 10)
        self.etiquetatelefono.pack(side = LEFT)

        self.txtelefono = Entry(self.cont4)
        self.txtelefono['width'] = 25
        self.txtelefono['font'] = self.fuente1
        self.txtelefono.pack(side = LEFT)

        self.etiquetaemail = Label(self.cont5, text = 'E-mail', font = self.fuente1, width = 10)
        self.etiquetaemail.pack(side = LEFT)

        self.txtemail = Entry(self.cont5)
        self.txtemail['width'] = 25
        self.txtemail['font'] = self.fuente1
        self.txtemail.pack(side = LEFT)

        self.etiquetausuario = Label(self.cont6, text = 'Usuario: ', font = self.fuente1, width = 10)
        self.etiquetausuario.pack(side = LEFT)

        self.txtusuario = Entry(self.cont6)
        self.txtusuario['width'] = 25
        self.txtusuario['font'] = self.fuente1
        self.txtusuario.pack(side = LEFT)

        self.etiquepassword = Label(self.cont7, text = 'Password', font = self.fuente1, width = 10)
        self.etiquepassword.pack(side = LEFT)

        self.txtpsw = Entry(self.cont7)
        self.txtpsw['width'] = 25
        self.txtpsw['show'] = '*'
        self.txtpsw['font'] = self.fuente1
        self.txtpsw.pack(side = LEFT)

        self.botonAdicionar = Button(self.cont8, text = 'Adicionar', font = self.fuente1, width = 12)
        self.botonAdicionar['command'] = self.adicionarUsuario
        self.botonAdicionar.pack(side = LEFT)

        self.botonAlterar = Button(self.cont8, text='Alterar', font=self.fuente1, width = 12)
        self.botonAlterar['command'] = self.alterarUsuario
        self.botonAlterar.pack(side = LEFT)

        self.botonExcluir = Button(self.cont8, text='Excluir', font=self.fuente1, width = 12)
        self.botonExcluir['command'] = self.excluirUsuario
        self.botonExcluir.pack(side = LEFT)

        self.etiquetamsg = Label(self.cont9)
        self.etiquetamsg['font'] = ('verdana', '9', 'italic')
        self.etiquetamsg.pack()

    def adicionarUsuario(self):
        user = Usuarios()

        user.name = self.txtnombre.get()
        user.phone = self.txtelefono.get()
        user.mail = self.txtemail.get()
        user.user = self.txtusuario.get()
        user.password = self.txtpsw.get()

        self.etiquetamsg['text'] = user.agregarUsuario()

        self.txtidusuario.delete(0, END)
        self.txtnombre.delete(0, END)
        self.txtelefono.delete(0, END)
        self.txtemail.delete(0, END)
        self.txtusuario.delete(0, END)
        self.txtpsw.delete(0, END)

    def alterarUsuario(self):
        user = Usuarios()

        user.iduser = self.txtidusuario.get()
        user.name = self.txtnombre.get()
        user.phone = self.txtelefono.get()
        user.mail = self.txtemail.get()
        user.user = self.txtusuario.get()
        user.password = self.txtpsw.get()

        self.etiquetamsg['text'] = user.actualizarUsuario()

        self.txtidusuario.delete(0, END)
        self.txtnombre.delete(0, END)
        self.txtelefono.delete(0, END)
        self.txtemail.delete(0, END)
        self.txtusuario.delete(0, END)
        self.txtpsw.delete(0, END)
    
    def excluirUsuario(self):
        user = Usuarios()

        user.iduser = self.txtidusuario.get()

        self.etiquetamsg['text'] = user.borrarUsuario()

        self.txtidusuario.delete(0, END)
        self.txtnombre.delete(0, END)
        self.txtelefono.delete(0, END)
        self.txtemail.delete(0, END)
        self.txtusuario.delete(0, END)
        self.txtpsw.delete(0, END)
    
    def buscarUsuario(self):
        user = Usuarios()

        iDusuario = self.txtidusuario.get()

        self.etiquetamsg['text'] = user.seleccionarUsuario(iDusuario)

        self.txtidusuario.delete(0, END)
        self.txtidusuario.insert(INSERT, user.iduser)

        self.txtnombre.delete(0, END)
        self.txtnombre.insert(INSERT, user.name)

        self.txtelefono.delete(0, END)
        self.txtelefono.insert(INSERT, user.phone)

        self.txtemail.delete(0, END)
        self.txtemail.insert(INSERT, user.mail)

        self.txtusuario.delete(0, END)
        self.txtusuario.insert(INSERT, user.user)

        self.txtpsw.delete(0, END)
        self.txtpsw.insert(INSERT, user.password)
raiz = Tk()
Aplicacion(raiz)
raiz.mainloop()   