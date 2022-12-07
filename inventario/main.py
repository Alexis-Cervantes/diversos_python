from tkinter import *
from tkinter import Tk, StringVar, ttk
from PIL import Image, ImageTk
from tkcalendar import Calendar, DateEntry
from datetime import date
# cores

co0 = "#2e2d2b" # preta
co1 = "#feffff" # branca
co2 = "#4fa882" # verde
co3 = "#38576b" # valor
co4 = "#403d3d" # letra
co5 = "#e06636" # - profit
co6 = "#038cfc" # azul
co7 = "#3fbfb9" # verde
co8 = "#263238" # + verde
co9 = "#e9edf5" # + verde

janela = Tk()
janela.title('')
janela.geometry('900x600')
janela.configure(background = co9)
janela.resizable(width = FALSE, height = FALSE)

style = ttk.Style(janela)
style.theme_use('clam')

# CRIANDO FRAMES
frameCima = Frame(janela, width=1043, height=50, bg=co1, relief=FLAT)
frameCima.grid(row=0, column=0)

frameMedio = Frame(janela, width=1043, height=303, bg=co1, pady=20, relief=FLAT)
frameMedio.grid(row=1,column=0, pady=1, padx=0, sticky=NSEW)

frameBaixo = Frame(janela, width=1043, height=300, bg=co1, relief=FLAT)
frameBaixo.grid(row=2, column=0, pady=0, padx=1, sticky=NSEW)

# Trabalhando no frame Cima ------
# ABRIENDO IMAGEM
app_img = Image.open('inventario/Logo_inventario.png')
app_img = app_img.resize((45, 45))
app_img = ImageTk.PhotoImage(app_img)

app_logo = Label(frameCima, image=app_img, text='Inventario Doméstico', width=900, compound=LEFT, relief=RAISED, anchor=NW, font=('Verdana 20 bold'), bg=co1, fg=co4)
app_logo.place(x=0, y=0)

# Trabalhando no frame meio ------
l_nome = Label(frameMedio, text='Nome', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_nome.place(x=10, y=10)
e_nome = Entry(frameMedio, width=30, justify="left", relief=SOLID)
e_nome.place(x=130, y=11)

l_sala_area = Label(frameMedio,text='Sala/Área', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_sala_area.place(x=10, y=40)
e_sala_area = Entry(frameMedio, width=30, justify="left", relief=SOLID)
e_sala_area.place(x=130, y=41)

l_descricao = Label(frameMedio, text='Descrição', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_descricao.place(x=10, y=70)
e_descricao = Entry(frameMedio, width=30, justify='left', relief=SOLID)
e_descricao.place(x=130, y=71)

l_marca_modelo = Label(frameMedio, text='Marca/Modelo', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_marca_modelo.place(x=10, y=100)
e_marca_modelo = Entry(frameMedio, width=30, justify='left', relief=SOLID)
e_marca_modelo.place(x=130, y=101) 

l_calendar = Label(frameMedio, text='Data da compra', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_calendar.place(x=10, y=130)
e_calendar = DateEntry(frameMedio, width=12, background='darkblue', bordewidth=2, year=2022)
e_calendar.place(x=130, y=131)

l_valor_compra = Label(frameMedio, text='Valor da compra', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_valor_compra.place(x=10, y=160)
e_valor_compra = Entry(frameMedio, width=30, justify='left', relief=SOLID)
e_valor_compra.place(x=130, y=161)

l_numero_serie = Label(frameMedio, text='Número de série', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_numero_serie.place(x=10, y=190)
e_numero_serie = Entry(frameMedio, width=30, justify='left', relief=SOLID)
e_numero_serie.place(x=130, y=191)

l_img = Label(frameMedio, text='Imagem do item', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_img.place(x=10, y=220)
b_img = Button(frameMedio,width=30, text='Carregar'.upper(), compound=CENTER, anchor=CENTER, overrelief=RIDGE, font=('Ivy 8'), bg=co1, fg=co0)
b_img.place(x=130, y=221)





janela.mainloop()
