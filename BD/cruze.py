import datetime

# Clase con los valores del cruze o alerta para almacenarlos en la base de datos
class Cruze:

    #Método constructor para crear el cruze
    def __init__(self, objeto = None, fechaHora = None, alarma = None, distancia=None):

        #Objeto que se valida, ya sea si pasa peaton o automovil
        self._objeto = objeto

        #Fecha y hora en la que se realizo el cruze
        self._fechaHora = fechaHora

        #Se emitio alarma, en este caso es verdadero
        self._alarma = alarma

        #Distancia en la que se emitio la alarma
        self._distancia = distancia

    @property
    #Método de acceso para obtener el objeto
    def objeto(self):
        return self._objeto

    @property
    #Método de acceso para obtener la fecha y la hora
    def fechaHora(self):
        return self._fechaHora

    @property
    #Método de acceso para obtener si se emitio alarma
    def alarma(self):
        return self._alarma

    @property
    #Método de acceso para obtener la distancia
    def distancia(self):
        return self._distancia

    @objeto.setter
    #Método de acceso para asignar el objeto al cruze
    def objeto(self, objeto):
        self._objeto = objeto
    
    @fechaHora.setter
    #Método de acceso para asignar la fecha y hora al cruze
    def fechaHora(self, fechaHora):
        self._fechaHora = fechaHora

    @alarma.setter
    #Método de acceso para asignar si se emitio alarma o no
    def alarma(self, alarma):
        self._alarma = alarma

    @distancia.setter
    #Método de acceso para asignar la distancia en la que se emitio la alarma
    def distancia(self, distancia):
        self._distancia = distancia
    