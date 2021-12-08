#
# persistenciaException.py
#

class PersistenciaException(Exception):
    ''' Exception lanzada cuando ocurre un error en el mecanismo de persistencia
        en el programa amante musica

        @utor: Manuel Domitsu Kono
    '''

    def __init__(self, msj):
        ''' Constructor de la clase. Inicializa los atributos de la clase

            @param msj Mensaje con la descripcion del error ocurrido
        '''
        super().__init__(msj)
        self.__msj = msj;

    @property
    def msj(self):
        ''' Regresa el mensaje de error 

            @returns El mensaje de error
        '''
        return self.__msj

    @property
    def cause(self):
        ''' Regresa la causa original del error

            @returns La causa original del error
        '''
        return self.__cause__       


    def __str__(self):
        ''' Regresa una cadena con una representacion amigable
            de una instancia de la clase

            @returns Una cadena con una representacion amigable
                de la instancia de la clase
        '''
        return (f'PersistenciaException: {self.__msj}, {self.__cause__}')

    def __repr__(self):
        ''' Regresa una cadena con una representacion unica 
            de una instancia de la clase

            @returns Una cadena con una representacion unica
                de la instancia de la clase
        '''
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
