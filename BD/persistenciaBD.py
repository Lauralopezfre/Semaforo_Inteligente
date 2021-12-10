#Se importan las librerias necesarias para el acceso a datos
import datetime
from BD.cruze import Cruze
from BD.cruzesBD import CruzesBD
from BD.persistenciaException import PersistenciaException

#Clase que se encarga de acceder o conectar a la base de datos.
class PersistenciaBD:

    #Se inicializan las propiedades de la base de datos
    def __init__(self) -> None:
        self.__user = 'root'
        self.__password = '1234'
        self.__host = 'localhost'
        self.__database = 'accidentes'
        self.__tablaCruzes = 'cruze'

        #Se conecta con la base de datos.
        self._catalogoCruzes = CruzesBD(self.__user, self.__password, self.__host, self.__database, self.__tablaCruzes)

    #Método que se encarga de agregar a la base de datos el cruze registrados
    def agregarCruze(self, cruze):
        self._catalogoCruzes.agrega(cruze)

    #Método que se encarga de consultar todos los cruzes registrados
    def consultarCruze(self):
        return self._catalogoCruzes.obtener()
