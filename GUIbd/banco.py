# Importando modulo SQlite
import sqlite3

class Banco():
    # Creando el archivo de conexion con el bd
    def __init__(self):
        self.conexion = sqlite3.connect('banco.db')
        self.crearTabla()

    def crearTabla(self):
        c = self.conexion.cursor()

        c.execute("""create table if not exists usuarios (
                    idusuario integer primary key autoincrement ,
                    nombre text,
                    telefono text,
                    email text,
                    usuario text,
                    clave text)""")
        self.conexion.commit()
        c.close()