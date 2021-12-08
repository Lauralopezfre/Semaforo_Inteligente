import datetime
from cruze import Cruze
from cruzesBD import CruzesBD
from persistenciaBD import PersistenciaBD
from persistenciaException import PersistenciaException


persistencia = PersistenciaBD()

print()
print('Movimientos al catálogo de géneros')

print()
cruze = Cruze('Peaton', datetime.datetime(2021, 3, 24), True)