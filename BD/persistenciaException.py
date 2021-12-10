#
# persistenciaException.py
#

class PersistenciaException(Exception):
    #Exception lanzada cuando ocurre un error en el mecanismo de persistencia
    #en el programa amante musica
    def __init__(self, msj):
        # Constructor de la clase. Inicializa los atributos de la clase
        super().__init__(msj)
        self.__msj = msj

    @property
    # Regresa el mensaje de error
    def msj(self):
        return self.__msj

    @property
    # Regresa la causa original del error
    def cause(self):
        return self.__cause__       

    # Regresa una cadena con una representacion amigable de una instancia de la clase
    def __str__(self):
        return (f'PersistenciaException: {self.__msj}, {self.__cause__}')

    def __repr__(self):
        # Regresa una cadena con una representacion unica de una instancia de la clase
        return (f'{self.__module__}.{self.__class__.__name__}: {self.__msj}, {self.__cause__}')


if __name__ == '__main__':

    try:
        # Se lanza una excepcion del tipo PersistenciaException
        raise PersistenciaException('Error en el mecanismo de persistencia')
    except PersistenciaException as q:
        print(f'Tipo de excepción atrapada:  {q.__class__}')
        print()
        print(f'Descripcion amigable de la excepcion: {q.__str__()}')
        print()
        print(f'Descripcion unica de la excepcion: {q.__repr__()}')
        print()
        print(f'Descripcion de la excepcion: {q}')
        print()
        print(f'Argumentos del constructor de la excepcion: {q.args}')
        print()
        print(f'Mensaje de error: {q.msj} ')
        print(f'Si es una excepcion encadenada, causa original de la excepcion: {q.__cause__}')
        print()
