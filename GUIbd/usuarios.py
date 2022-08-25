from tokenize import blank_re
from turtle import back
from banco import Banco

class Usuarios(object):

    def __init__(self, idusuario = 0, nombre = '', telefono = '', email = '', usuario = '', clave = ''):
        self.informacion = {}
        self.iduser = idusuario
        self.name = nombre
        self.phone = telefono
        self.mail = email
        self.user = usuario
        self.password = clave

    def agregarUsuario(self):
        
        bank = Banco()
        try:
            c = bank.conexion.cursor()

            c.execute("insert into usuarios (nombre, telefono, email, usuario, clave) values ('" + self.name + "', '" + self.phone + "', '" + self.mail + "', '" + self.user + "', '" + self.password + "')")

            bank.conexion.commit()
            c.close()

            return 'Usuario agregado con exito!'
        except:
            return 'Ocurrio un error al intentar agregar usuario!'

    def actualizarUsuario(self):
        
        bank = Banco()
        try:
            c = bank.conexion.cursor()

            c.execute("update usuarios set nombre = '" + self.name + "', telefono = '" + self.phone + "', email = '" + self.mail + "', usuario = '" + self.user + "' clave = '" + self.password + "' where idusuario = " + self.iduser +" ")

            bank.conexion.commit()
            c.close()

            return "Usuario actualizado con exito!"
        except:
            return "Ocurrio un error al intentar altera usuario!"
        
    def borrarUsuario(self):

        bank = Banco()
        try:
            c = bank.conexion.cursor()

            c.execute("delete from usuarios where idusuario = " + self.iduser + " ")

            bank.conexion.commit()
            c.close()

            return "Usuario excluido con exito!"
        except:
            return "Ocurrio un error al intentar excluir usuario!"

    def seleccionarUsuario(self, idusuario):

        bank = Banco()
        try:
            c = bank.conexion.cursor()

            c.execute("select * from usurios where idusuario = " + idusuario + " ")

            for linha in c:
                self.iduser = linha[0]
                self.name = linha[1]
                self.phone = linha[2]
                self.mail = linha[3]
                self.user = linha[4]
                self.password = linha[5]
            
            c.close()

            return "Busqueda realizada con exito!"
        except:
            return "Ocurrio un error al intentar buscar usuario!"