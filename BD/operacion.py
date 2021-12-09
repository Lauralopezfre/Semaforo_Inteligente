import datetime
from cruze import Cruze
from cruzesBD import CruzesBD
from persistenciaBD import PersistenciaBD
from persistenciaException import PersistenciaException


persistencia = PersistenciaBD()

print()
print('Guardar registro')

print()

try:
    cruze = Cruze('Peaton', datetime.datetime(2021, 3, 24), True)
    persistencia.agregarCruze(cruze)
except PersistenciaException as pe:
    print(pe.msj)
    print(pe.cause)

print()
print('Obtener registro')

lista = []
try:
    
    lista = persistencia.consultarCruze()
    for c in lista:
        print(c)
        cruzeObjeto = Cruze(*c)
        print(cruzeObjeto.objeto)

except PersistenciaException as pe:
    print(pe.msj)
    print(pe.cause)
    
