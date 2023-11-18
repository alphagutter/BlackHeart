from abc import ABC, abstractmethod
import persistent

class Persona(ABC, persistent.Persistent):
    '''pequeña clase abstracta, donde definimos 2 clases a utilizar en distintos tipos, los cajeros y los clientes'''
    def __init__(self, nombre):
        self.nombre = nombre
        self.disponible = True
        self.objeto_utilizado = None
        self.tiempo_ocupado = 0

    @abstractmethod
    def jugar():
        pass
    
    @abstractmethod
    def descansar():
        pass




class Cajero(Persona):
    '''Es el empleado con el que interactuan los clientes, pueden limpiar, atender a los clientes, entre otras cosas'''
    def __init__(self,nombre):
        super().__init__(nombre)
        self.barra_cansancio = 0

    def __str__(self):
        return (f'Cajero: {self.nombre}, '
                f'Nivel de cansancio: {self.barra_cansancio}, '
                f'disponible: {self.disponible}')


    def sugerir_accion(self, accion):
        '''El cajero sugiere una acción al cliente que esté en frente de la fila'''
        self.barra_cansancio += 1
        return(f'{self.nombre} sugiere {accion}')

        

    def atender_fila(self, cliente):
        '''El cajero entra en la caja, le pasamos la fila de clientes y el menú para entregar la comida'''
        self.barra_cansancio += 1
        return(f'El cajero atenderá a {cliente.nombre}')



    def descansar(self, sofa):
        '''Le pasamos el sofá en el que el cliente va a descansar, y aumentar su entusiasmo'''
        
        self.objeto_utilizado = sofa
        self.disponible = False
        self.barra_cansancio -= 2
        self.tiempo_ocupado += 1

        if self.barra_cansancio <= 0:
            return(f'@@  El cajero está descansando al pedo...')
        else:
            return(f'@@  {self.nombre} descansa a gusto')
        

    def des_descansar(self):
        self.objeto_utilizado = None
        self.disponible = True
        print(f'@@  {self.nombre} ya no descansa')
        self.tiempo_ocupado = 0
                

    def jugar(self, consola):
        '''Le pasamos la consola con la que el cajero va a jugar, y la guardamos para luego modificarla si
        queremos desconectarla'''
        self.objeto_utilizado = consola
        self.disponible = False
        self.barra_cansancio -= 1
        self.tiempo_ocupado += 1
        
        if self.tiempo_ocupado <= 1:
            return(f'{self.nombre} está jugando con {self.objeto_utilizado.nombre}')
        else:
            return(f'{self.nombre} sigue jugando')

    def des_jugar(self):
        self.objeto_utilizado = None
        self.disponible = True
        print(f'{self.nombre} ya no juega')
        self.tiempo_ocupado = 0




class Cliente(Persona):
    '''Los clientes son el objeto que más interactúa con otros objetos, sus estados cuando se crean son randomizados'''
    def __init__(self, nombre):
        super().__init__(nombre)
        self.entusiasmo = 0
        self.estado_animo = None
        self.en_el_local = False

    def __str__(self):
        return (f'{self.nombre}, '
                f'Entusiasmo: {self.entusiasmo}, '
                f'Estado de ánimo: {self.estado_animo.get("Nombre")}, '
                f'disponible: {self.disponible}, '
                )

    def descansar(self, sofa):
        '''Le pasamos el sofá en el que el cliente va a descansar, y aumentar su entusiasmo'''
        self.objeto_utilizado = sofa
        self.disponible = False
        self.entusiasmo += 1
        self.tiempo_ocupado += 1

        print(f'{self.nombre} está descansando en {self.objeto_utilizado.nombre}')

    def des_descansar(self):
        self.objeto_utilizado = None
        self.disponible = True
        print(f'{self.nombre} ya no descansa')
        self.tiempo_ocupado = 0



    def jugar(self, consola):
        '''Le pasamos la consola con la que el cliente va a jugar, y la guardamos para luego modificarla si
        queremos desconectarla'''
        self.objeto_utilizado = consola
        self.disponible = False
        self.entusiasmo += 3
        self.tiempo_ocupado += 1

        if self.tiempo_ocupado <= 1:
            print(f'{self.nombre} está jugando con {self.objeto_utilizado.nombre}')
        else:
            print(f'{self.nombre} sigue jugando')

    def des_jugar(self):
        self.objeto_utilizado = None
        self.disponible = True
        print(f'{self.nombre} ya no juega')
        self.tiempo_ocupado = 0


    #especificaciones de tipos de estados:
    #--enojado(0): solo quiere comer, si se le recomienda jugar, se retira del local, no se enoja si le recomiendan dormir
    #--triste(1): quiere comer o descansar, no se enoja si le recomiendan jugar
    #--feliz(2): quiere comer o jugar, no se enoja si le recomiendan jugar        

    def comer(self, nuevo_entusiasmo):
        '''Luego de que el cajero les pase la comida, los clientes pueden comerla, y así, cambiar su estado de ánimo'''
        self.entusiasmo += nuevo_entusiasmo

        print(f'{self.nombre} está comiendo {self.objeto_utilizado}')

        self.objeto_utilizado = None
        self.disponible = True
