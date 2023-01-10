""" fonte: Eletronica e programação - Yputube - Curso de Pyqt5"""
import sys                                                                  
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QToolTip, QLabel, QLineEdit
from PyQt5 import QtGui
class Ventana(QMainWindow):
    def __init__(self):
        super().__init__ ()

        self.arriba = 100
        self.izquierda = 100
        self.anchura = 800
        self.altura = 600
        self.titulo = "Primera Ventana"

        # Creando caja de texto:
        self.caja_texto = QLineEdit(self)
        self.caja_texto.move(25, 20)
        self.caja_texto.resize(220, 40)

        # CRIANDO BOTONES
        # Ventada 1
        boton1 = QPushButton('Botão 1', self)
        boton1.move(150, 200) # Posição na janela (altura(vetical) e largura(horizontal) em pixeis)    
        boton1.resize(150, 80) # Altura e Largura do Botão
        boton1.setStyleSheet('QPushButton {background-color: #0FB328; font: bold; font-size: 20px}') # Carateristica do botçao 
        boton1.clicked.connect(self.boton1_click)

        # Boton texto
        boton_caja_txt = QPushButton('Enviar Texto', self)
        boton_caja_txt.move(550, 200) # Posição na janela (altura(vetical) e largura(horizontal) em pixeis)    
        boton_caja_txt.resize(150, 80) # Altura e Largura do Botão
        boton_caja_txt.setStyleSheet('QPushButton {background-color: #0FB328; font: bold; font-size: 20px}') # Carateristica do botçao 
        boton_caja_txt.clicked.connect(self.mostrar_texto)
        
        # Ventana 2
        boton2 = QPushButton('Botão 2', self)
        boton2.move(350, 200) # Posicion ventana principal (horizontal - izq a der) e (vertical - arriba a bajo) em pixeis)    
        boton2.resize(150, 80) # Altura e Largura do Botão
        boton2.setStyleSheet('QPushButton {background-color: red; font: bold; font-size: 20px}') # Carateristica do botçao 
        boton2.clicked.connect(self.boton2_click)
        
        # Creabdo Etiquetas (Labels)
        self.etiqueta1 = QLabel(self)
        self.etiqueta1.move(50, 100)
        self.etiqueta1.resize(260, 50) #(Largura , altura)
        self.etiqueta1.setStyleSheet('QLabel {font: bold; font-size: 30px}')
        self.etiqueta1.setText('Aprete un boton!!')

        # Creabdo Etiquetas caja texto (Labels)
        self.etiqueta_caja_txt = QLabel(self)
        self.etiqueta_caja_txt.move(450, 100)
        self.etiqueta_caja_txt.setStyleSheet('QLabel {font: bold; font-size: 30px}')
        self.etiqueta_caja_txt.resize(260, 50) #(Largura , altura)
        self.etiqueta_caja_txt.setText('Digitou: ')

        # Trabajando com imagenes
        self.carro = QLabel(self)
        self.carro. move(50, 400)
        self.carro.setPixmap(QtGui.QPixmap('Qt_designer/carro2.png'))
        self.carro.resize(400, 200)

        # LLAMANDO VENTANA PRNCIPAL
        self.cargarVentana()
    
    # Funcion que define dimensiones de la ventana principal
    def cargarVentana(self):
        self.setGeometry(self.izquierda, self.arriba, self.anchura, self.altura)
        self.setWindowTitle(self.titulo)
        self.show()

    # Funcion que define las carateristicas del boton 1.
    def boton1_click(self):
        """ print('O boton 1 fue Clicado!!!') """
        self.etiqueta1.setText('Foi selccionado o carro 1')
        self.etiqueta1.setStyleSheet('QLabel {font: bold; font-size: 25px; color: green}')
        self.carro.setPixmap(QtGui.QPixmap('Qt_designer/carro1.png'))

    def mostrar_texto(self):
        contenido = self.caja_texto.text()
        self.etiqueta_caja_txt.setText('Digitou: '+ contenido)
        
    # Funcion que define las carateristicas del boton 2.
    def boton2_click(self):
        """ print('O boton 2 fue Clicado!!!') """
        self.etiqueta1.setText('Foi selecionado o carro 2')
        self.etiqueta1.setStyleSheet('QLabel {font: bold; font-size: 25px; color: red}')
        self.carro.setPixmap(QtGui.QPixmap('Qt_designer/carro2.png'))

app = QApplication(sys.argv)
v = Ventana()
sys.exit(app.exec_())

