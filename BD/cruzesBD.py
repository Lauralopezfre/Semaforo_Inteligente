import datetime
import mysql.connector
from persistenciaException import PersistenciaException
from tabla import Tabla

class CruzesBD(Tabla):

    def __init__(self, user, password, host, database, tablaCruzes):
        super().__init__(user, password, host, database)
        self.tablaCruzes = tablaCruzes
 
    def agrega(self, cruze):

        operacion = f"INSERT {self.tablaCruzes}"
        operacion += f" SET objeto = '{cruze.objeto:s}'"
        operacion += f", fechaHora = '{cruze.fehcaHora:s}'"
        operacion += f", alarma = '{cruze.alarma:s}'"       
        operacion += ";"

        try:
            super().actualiza(operacion)
        except mysql.connector.Error as e:
            raise PersistenciaException(f'Error: {self.msj_error(e)} en la tabla {self.tablaCruzes} de la base de datos {self.database}') from e