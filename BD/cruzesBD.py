#Se importan las librerias necesarias para el acceso a datos
import datetime
import mysql.connector
from BD.tabla import Tabla
from BD.cruze import Cruze
from BD.persistenciaException import PersistenciaException

#Clase que se encarga de hacer toda la interaccion con la tabla en la base de datos
class CruzesBD(Tabla):

    #Se inicializan las propiedades de la base de datos.
    def __init__(self, user, password, host, database, tablaCruzes):
        super().__init__(user, password, host, database)
        self.tablaCruzes = tablaCruzes
 
    #Método que se encarga de crear la consulta o query para guardar en la base de datos
    def agrega(self, cruze):

        #Consulta para ingresar una nueva cruze
        operacion = f"INSERT INTO {self.tablaCruzes}"
        operacion += f" (objeto, fechaHora, alarma, distancia) "
        operacion += f"VALUES ('{cruze.objeto}', "
        operacion += f"'{cruze.fechaHora}', "
        operacion += f"{cruze.alarma}, "
        operacion += f"{cruze.distancia})"        
        operacion += ";"

        #Se ingresa la operación en la base de datos
        try:
            super().actualiza(operacion)
        except mysql.connector.Error as e:
            raise PersistenciaException(f'Error: {self.msj_error(e)} en la tabla {self.tablaCruzes} de la base de datos {self.database}') from e

    #Método que se encarga de crear la consulta o query para obtener de la base de datos
    def obtener(self):

        #Consulta para obtener las cruzes
        operacion = f"SELECT * FROM accidentes.{self.tablaCruzes};"

        #Se ingresa la operación en la base de datos
        try:
            renglones = super().consulta(operacion)
        except mysql.connector.Error as e:
            raise PersistenciaException(f'Error: {self.msj_error(e)} en la tabla {self.tablaCruzes} de la base de datos {self.database}') from e

        return renglones