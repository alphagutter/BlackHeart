from abc import ABC, abstractmethod
import persistent

class Interactuables(ABC, persistent.Persistent):
    '''Son los objetos que modifican los estados de las personas'''
    def __init__(self):
        self.id_accion = None
        self.disponible = True
        self.ocupante = None

    @abstractmethod
    def accion():
        pass

    def des_accionar(self):
        self.disponible = True
        self.ocupante = None


class Consola(Interactuables):
    '''Las consolas con las que los clientes/cajeros pueden jugar, cambian su disponibilidad si alguno las está usando, 
    cambian los estados de las personas'''
    def __init__(self, nombre):
        self.nombre = nombre
        super().__init__()
        #id para controlar en mecanicas 
        self.id_accion = 0

    def __str__(self):
        return (
            f'Nombre: {self.nombre}, '
            f'Disponible: {self.disponible}, '
            f'Jugador: {self.ocupante}, '
        )


    def accion(self, nombre):
        '''Se le pasa el nombre del jugador que jugará a la consola, y cambia su disponibilidad'''
        self.ocupante = nombre
        self.disponible = False
        return(f'{self.ocupante} está jugando a la consola {self.nombre}')



class Sofa(Interactuables):
    '''Las personas pueden descansar en el sofá, de acuerdo al atributo que tengan, cambia una u otra cosa'''
    def __init__(self, nombre, nivel_comodidad):
        self.nombre = nombre
        self.nivel_comodidad = nivel_comodidad
        super().__init__()
        #id para controlar en mecanicas 
        self.id_accion = 1


    def __str__(self):
        return(
            f'Color: {self.color}, '
            f'Nivel de comodidad: {self.nivel_comodidad}, '
            f'Disponible: {self.disponible}, '
            f'Ocupante: {self.ocupante}'
        )
        

    def accion(self,nombre):
        '''Recibe el nombre de la persona que va a descansar, y luego la guarda en sus atributos'''
        self.ocupante = nombre
        self.disponible = False
        return(f'{self.ocupante} está descansando en el sofá {self.nombre}')
