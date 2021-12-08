import datetime
from cruze import Cruze
from cruzesBD import CruzesBD
from persistenciaException import PersistenciaException

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