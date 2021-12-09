import datetime

class Cruze:

    def __init__(self, objeto = None, fechaHora = None, alarma = None, distancia=None):

        self._objeto = objeto
        self._fechaHora = fechaHora
        self._alarma = alarma
        self._distancia = distancia

    @property
    def objeto(self):
        return self._objeto

    @property
    def fechaHora(self):
        return self._fechaHora

    @property
    def alarma(self):
        return self._alarma

    @property
    def distancia(self):
        return self._distancia

    @objeto.setter
    def objeto(self, objeto):
        self._objeto = objeto
    
    @fechaHora.setter
    def fechaHora(self, fechaHora):
        self._fechaHora = fechaHora

    @alarma.setter
    def alarma(self, alarma):
        self._alarma = alarma

    @distancia.setter
    def distancia(self, distancia):
        self._distancia = distancia
    