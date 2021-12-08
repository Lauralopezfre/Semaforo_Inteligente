import datetime
import mysql.connector
from persistenciaException import PersistenciaException
from tabla import Tabla

class CruzesBD(Tabla):

    def __init__(self, user, password, host, database, tablaCruzes):
        super().__init__(user, password, host, database)
        self.tablaCruzes = tablaCruzes
 
    def agrega(self, cruze):

        operacion = f"INSERT INTO {self.tablaCruzes}"
        operacion += f" (objeto, fechaHora, alarma) "
        operacion += f"VALUES ('{cruze.objeto}', "
        operacion += f"'{cruze.fechaHora}', "
        operacion += f"{cruze.alarma})"       
        operacion += ";"

        try:
            super().actualiza(operacion)
        except mysql.connector.Error as e:
            raise PersistenciaException(f'Error: {self.msj_error(e)} en la tabla {self.tablaCruzes} de la base de datos {self.database}') from e