import datetime
from BD.cruze import Cruze
from BD.cruzesBD import CruzesBD
from BD.persistenciaException import PersistenciaException

class PersistenciaBD:

    def __init__(self) -> None:
        self.__user = 'root'
        self.__password = '1234'
        self.__host = 'localhost'
        self.__database = 'accidentes'
        self.__tablaCruzes = 'cruze'

        self._catalogoCruzes = CruzesBD(self.__user, self.__password, self.__host, self.__database, self.__tablaCruzes)

    def agregarCruze(self, cruze):
        self._catalogoCruzes.agrega(cruze)

    def consultarCruze(self):
        
        return self._catalogoCruzes.obtener()
