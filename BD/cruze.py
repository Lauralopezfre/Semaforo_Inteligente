import datetime

class Cruce():

    def __init__(self, clave, objeto = None, fechaHora = None, alarma = None) -> None:

        self._clave = clave
        self._objeto = objeto
        self._fechaHora = fechaHora
        self._alarma = alarma

    @property
    def clave(self):
        return self._clave

    @property
    def objeto(self):
        return self._objeto

    @property
    def fechaHora(self):
        return self._fechaHora

    @property
    def alarma(self):
        return self._alarma

    @objeto.setter
    def objeto(self, objeto):
        self._objeto = objeto
    
    @fechaHora.setter
    def fechaHora(self, fechaHora):
        self._fechaHora = fechaHora

    @alarma.setter
    def alarma(self, alarma):
        self._alarma = alarma
    