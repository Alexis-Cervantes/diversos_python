""" Criando uma pequena aplicação com Banco de dados - https://www.devmedia.com.br/tkinter-interfaces-graficas-em-python/33956 """
from tkinter import *
from tkinter import Tk, StringVar, ttk
from tkinter import messagebox
from tkinter import filedialog as fd
# Importando PILLOW
from PIL import Image, ImageTk
# Importando TKcalendar
from tkcalendar import Calendar, DateEntry
from datetime import date
# Importando View
from view import *
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

# CRIANDO FUNÇÕES
global tree
def inserir():
    global imagem, imagem_string, l_imagem 

    nome = e_nome.get()
    sala_area = e_sala_area.get()
    descricao = e_descricao.get()
    marca_modelo = e_marca_modelo.get()
    calendar = e_calendar.get()
    valor_compra = e_valor_compra.get()
    numero_serie = e_numero_serie.get()
    imagem = imagem_string

    lista_inserir = [nome, sala_area, descricao, marca_modelo, calendar, valor_compra, numero_serie, imagem]

    for i in lista_inserir:
        if i == '':
            messagebox.showerror('Erro', 'Preencha todos os canpos')
            return 
    inserir_form(lista_inserir)

    messagebox.showinfo('Sucesso', 'Os dados foram inseridos com sucesso')

    e_nome.delete(0, 'end')
    e_sala_area.delete(0, 'end')
    e_descricao.delete(0, 'end')
    e_marca_modelo.delete(0, 'end')
    e_calendar.delete(0, 'end')
    e_valor_compra.delete(0, 'end')
    e_numero_serie.delete(0, 'end')

    mostrar()

# Função atualizar
def atualizar():
    global imagem, imagem_string, l_imagem
    try:
        treev_dados = tree.focus()
        treev_dicionario = tree.item(treev_dados)
        treev_lista = treev_dicionario['values']

        valor = treev_lista[0] 

        e_nome.delete(0, 'end')
        e_sala_area.delete(0, 'end')
        e_descricao.delete(0, 'end')
        e_marca_modelo.delete(0, 'end')
        e_calendar.delete(0, 'end')
        e_valor_compra.delete(0, 'end')
        e_numero_serie.delete(0, 'end')

        id = int(treev_lista[0])
        e_nome.insert(0, treev_lista[1])
        e_sala_area.insert(0, treev_lista[2])
        e_descricao.insert(0, treev_lista[3])
        e_marca_modelo.insert(0, treev_lista[4])
        e_calendar.insert(0, treev_lista[5])
        e_valor_compra.insert(0, treev_lista[6])
        e_numero_serie.insert(0, treev_lista[7])
        imagem_string = treev_lista[8]

        def update():
            global imagem, imagem_string, l_imagem 
            nome = e_nome.get()
            sala_area = e_sala_area.get()
            descricao = e_descricao.get()
            marca_modelo = e_marca_modelo.get()
            calendar = e_calendar.get()
            valor_compra = e_valor_compra.get()
            numero_serie = e_numero_serie.get()
            imagem = imagem_string

            if imagem == '':
                imagem = e_numero_serie.insert(0, treev_lista[7])

            lista_atualizar = [nome, sala_area, descricao, marca_modelo, calendar, valor_compra, numero_serie, imagem, id]

            for i in lista_atualizar:
                if i == '':
                    messagebox.showerror('Erro', 'Preencha todos os canpos')
                    return 
            atualizar_(lista_atualizar)
            messagebox.showinfo('Sucesso', 'Os dados foram atualizados com sucesso')

            e_nome.delete(0, 'end')
            e_sala_area.delete(0, 'end')
            e_descricao.delete(0, 'end')
            e_marca_modelo.delete(0, 'end')
            e_calendar.delete(0, 'end')
            e_valor_compra.delete(0, 'end')
            e_numero_serie.delete(0, 'end')

            b_confirmar.destroy()

            mostrar()

        b_confirmar = Button(frameMedio, command=update, width=13, text='Confirmar'.upper(), overrelief=RIDGE, font=('Ivy 8 bold'), bg=co2, fg=co1)
        b_confirmar.place(x=330, y=185)

    except IndexError:
        messagebox.showerror('Erro', 'Seleciona um dos dados tabela')
        return 

# Função deletar
def deletar():
    try:
        treev_dados = tree.focus()
        treev_dicionario = tree.item(treev_dados)
        treev_lista = treev_dicionario['values']
        valor = treev_lista[0] 

        deletar_form([valor])
        
        messagebox.showinfo('Sucesso', 'Os dados foram deletados com sucesso')

        mostrar()

    except IndexError:
        messagebox.showerror('Erro', 'Seleciona um dos dados tabela')
      
# Função pata escolher imagem
global imagem, imagem_string, l_imagem 

def escolher_imagem():
    global imagem, imagem_string, l_imagem 

    imagem = fd.askopenfilename()
    imagem_string = imagem

    # ABRIENDO IMAGEM
    imagem = Image.open(imagem)
    imagem = imagem.resize((170, 170))
    imagem = ImageTk.PhotoImage(imagem)

    l_imagem = Label(frameMedio, image=imagem, bg=co1, fg=co4)
    l_imagem.place(x=700, y=10)

# função para ver imagem
def ver_imagem():
    global imagem, imagem_string, l_imagem

    treev_dados = tree.focus()
    treev_dicionario = tree.item(treev_dados)
    treev_lista = treev_dicionario['values']

    valor = [int(treev_lista[0])]

    iten = ver_item(valor)
    imagem = iten[0][8]

    # ABRIENDO IMAGEM
    imagem = Image.open(imagem)
    imagem = imagem.resize((170, 170))
    imagem = ImageTk.PhotoImage(imagem)

    l_imagem = Label(frameMedio, image=imagem, bg=co1, fg=co4)
    l_imagem.place(x=700, y=10)

# FRAMES CIMA
# ABRIENDO IMAGEM
logo_img = Image.open('inventario/imgs/logo.png')
logo_img = logo_img.resize((45, 45))
logo_img = ImageTk.PhotoImage(logo_img)

app_logo = Label(frameCima, image=logo_img, text='Inventario Doméstico', width=900, compound=LEFT, relief=RAISED, anchor=NW, font=('Verdana 20 bold'), bg=co1, fg=co4)
app_logo.place(x=0, y=0)

# FRAMES MEIO
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

# CRIANDO BOTÕES
# Botão carregar
l_carregar_img = Label(frameMedio, text='Imagem do item', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_carregar_img.place(x=10, y=220)
b_carregar_img = Button(frameMedio, command=escolher_imagem, width=29, text='Carregar'.upper(), compound=CENTER, anchor=CENTER, overrelief=RIDGE, font=('Ivy 8'), bg=co1, fg=co0)
b_carregar_img.place(x=130, y=221)

# botão inserir
img_add = Image.open('inventario/imgs/add.png')
img_add = img_add.resize((20,20))
img_add = ImageTk.PhotoImage(img_add)
b_inserir = Button(frameMedio, command=inserir, image=img_add, width=95, text='  Adicionar'.upper(), compound=LEFT, anchor=NW, overrelief=RIDGE, font=('Ivy 8'), bg=co1, fg=co0)
b_inserir.place(x=330, y=10)

# Botão Atualizar:
img_update = Image.open('inventario/imgs/update.png')
img_update = img_update.resize((20, 20))
img_update = ImageTk.PhotoImage(img_update)
b_update = Button(frameMedio, command=atualizar, image=img_update, width=95, text='  Atualizar'.upper(), compound=LEFT, anchor=NW, overrelief=RIDGE, font=('Ivy 8'), bg=co1, fg=co0)
b_update.place(x=330, y=50)

# Botão deletar
img_delete = Image.open('inventario/imgs/delete.png')
img_delete = img_delete.resize((20, 20))
img_delete = ImageTk.PhotoImage(img_delete)
b_delete = Button(frameMedio, command=deletar,image=img_delete, width=95, text='  Deletar'.upper(), compound=LEFT, anchor=NW, overrelief=RIDGE, font=('Ivy 8'), bg=co1, fg=co0)
b_delete.place(x=330, y=90)

# Ver Imagem
img_item = Image.open('inventario/imgs/item.png')
img_item = img_item.resize((20, 20))
img_item = ImageTk.PhotoImage(img_item)
b_item = Button(frameMedio, command=ver_imagem, image=img_item, width=95, text='  Item'.upper(), compound=LEFT, anchor=NW, overrelief=RIDGE, font=('Ivy 8'), bg=co1, fg=co0)
b_item.place(x=330, y=221)

# Etiquetas "quantidades totais e valores"
l_total = Label(frameMedio, text='', width=14, height=2, anchor=CENTER, font=('Ivy 17 bold'), bg=co7, fg=co1)
l_total.place(x=450, y=17)
l_total_ = Label(frameMedio, text='   Valor total de todos os itens  ', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co7, fg=co1)
l_total_.place(x=450, y=12)

l_qtd = Label(frameMedio, text='', width=14,  height=2, pady=5, anchor=CENTER, font=('Ivy 17 bold'), bg=co7, fg=co1)
l_qtd.place(x=450, y=90)
l_qtd_ = Label(frameMedio, text='   Quantidade total de itens   ', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co7, fg=co1)
l_qtd_.place(x=450, y=92)

# CODIGO DA TABELA JÁ ESCRITO
def mostrar():
    global tree
    # creating a treeview with dual scrollbars
    tabela_head = ['#Item','Nome',  'Sala/Área','Descrição', 'Marca/Modelo', 'Data da compra','Valor da compra', 'Número de série']

    lista_itens = ver_form()

    tree = ttk.Treeview(frameBaixo, selectmode="extended",columns=tabela_head, show="headings")

    # vertical scrollbar
    vsb = ttk.Scrollbar(frameBaixo, orient="vertical", command=tree.yview)

    # horizontal scrollbar
    hsb = ttk.Scrollbar(frameBaixo, orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree.grid(column=0, row=0, sticky='nsew')
    vsb.grid(column=1, row=0, sticky='ns')
    hsb.grid(column=0, row=1, sticky='ew')
    frameBaixo.grid_rowconfigure(0, weight=12)

    hd=["center","center","center","center","center","center","center", 'center']
    h=[40,150,100,160,130,100,100, 100]
    n=0

    for col in tabela_head:
        tree.heading(col, text=col.title(), anchor=CENTER)
        # adjust the column's width to the header string
        tree.column(col, width=h[n],anchor=hd[n])
        n+=1

    # inserindo os itens dentro da tabela
    for item in lista_itens:
        tree.insert('', 'end', values=item)

    quantidade = [8888,88]

    for iten in lista_itens:
        quantidade.append(iten[6])

    Total_valor = sum(quantidade)
    Total_itens = len(quantidade)

    l_total['text'] = 'R$ {:,.2f}'.format(Total_valor)
    l_qtd['text'] = Total_itens

mostrar()

janela.mainloop()
