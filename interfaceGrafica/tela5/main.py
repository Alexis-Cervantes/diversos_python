from tkinter import *
import time
maestra = Tk()
maestra.title('Portal del alumno 2021')
maestra.geometry('490x560+610+153')
maestra.iconbitmap(default='icon\\ico.ico')
maestra.resizable(width=1, height=1)

# Creando funciones
def nuevaVentana():
    maestra1 = Tk()
    maestra1.title('Nueva ventana creada')
    maestra1.geometry('490x560+400+153')
    
    time.sleep(0.3)
    maestra.destroy()
# Variables Globales
esconde_clave = StringVar()

# Importar imagenes
img_fondo = PhotoImage(file='img\\Fondo.png')
img_boton = PhotoImage(file='img\\Boton.png')

# Creando etiquetas
et_fondo = Label(maestra, image=img_fondo)
et_fondo.pack()

# Creacion de formularios de entrada
# Entrada ID Token
en_token = Entry(maestra, bd=2, font=('calibri', 15), justify=CENTER)
en_token.place(width=392, height=45, x=49, y=165)
# Entrada Email
en_email = Entry(maestra, bd=2, font=('calibri', 15), justify=CENTER)
en_email.place(width=392, height=45, x=49, y=278)
# Entrada Senha
en_senha = Entry(maestra, textvariable=esconde_clave, show='*',
                 bd=2, font=('calibri', 15), justify=CENTER)
en_senha.place(width=392, height=45, x=49, y=393)

# Criando Botones
bt_entrar = Button(maestra, bd=0, image=img_boton, command=nuevaVentana)
bt_entrar.place(width=116, height=62, x=202, y=478)

maestra.mainloop()
