import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QToolTip

class Ventana(QMainWindow):
    def __init__(self):
        super().__init__ ()

        self.arriba = 100
        self.izquierda = 100
        self.anchura = 800
        self.altura = 600
        self.titulo = "Primera Ventana"

        # CRIANDO BOTONES
        # Ventada 1
        boton1 = QPushButton('Botão 1', self)
        boton1.move(150, 200) # Posição na janela (altura(vetical) e largura(horizontal) em pixeis)    
        boton1.resize(150, 80) # Altura e Largura do Botão
        boton1.setStyleSheet('QPushButton {background-color: #0FB328; font: bold; font-size: 20px}') # Carateristica do botçao 
        boton1.clicked.connect(self.boton1_click)
        
        # Ventana 2
        boton2 = QPushButton('Botão 2', self)
        boton2.move(400, 200) # Posição na janela (altura(vetical) e largura(horizontal) em pixeis)    
        boton2.resize(150, 80) # Altura e Largura do Botão
        boton2.setStyleSheet('QPushButton {background-color: #0FB328; font: bold; font-size: 20px}') # Carateristica do botçao 
        boton2.clicked.connect(self.boton2_click)
        
        # LLAMANDO A LA VENTANA
        self.cargarVentana()

    def cargarVentana(self):
        self.setGeometry(self.izquierda, self.arriba, self.anchura, self.altura)
        self.setWindowTitle(self.titulo)
        self.show()

    def boton1_click(self):
        print('O boton 1 fue Clicado!!!')

    def boton2_click(self):
        print('O boton 2 fue Clicado!!!')

app = QApplication(sys.argv)
v = Ventana()
sys.exit(app.exec_())

