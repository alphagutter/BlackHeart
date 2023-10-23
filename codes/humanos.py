from abc import ABC, abstractmethod
from interactuables import *
import random

class Accionable:
    '''pequeña clase abstracta, donde definimos 2 clases a utilizar en distintos tipos, por el que ocurre el simple polimorfismo'''
    @abstractmethod
    def jugar():
        pass
    
    @abstractmethod
    def descansar():
        pass




class Cajero(Accionable):
    '''Es el empleado con el que interactuan los clientes, pueden limpiar, atender a los clientes, entre otras cosas'''
    def __init__(self, nombre, barra_cansancio):
        self.nombre = nombre
        self.barra_cansancio = barra_cansancio
        self.disponible = [True, None, 0]        #pos 0: si está disponible o no, 1: La accion que realiza, 2: la cantidad de turnos que la realiza
    def __str__(self):
        return (f'Cajero: {self.nombre}, '
                f'Nivel de cansancio: {self.barra_cansancio}, '
                f'disponible: {self.disponible}')

    #implementar mejor con el objeto sofa
    def descansar(self):
        if self.barra_cansancio == 0:
            print('El cajero está completamente descansado')
        elif self.barra_cansancio > 10:
            self.barra_cansancio -= 1
            print('El cajero está punto de colapsar')
        else: 
            self.barra_cansancio -= 1

    def limpiar(self):
        pass

    def sugerir_accion(self, cliente, accion_sugerida):

        if accion_sugerida == 1:
            accion_sugerida = 'Comer'
        elif accion_sugerida == 2:
            accion_sugerida = 'Descansar'
        elif accion_sugerida == 3:
            accion_sugerida = 'Jugar en la consola'

        print(f'El cajero sugiere al cliente {cliente.nombre}: {accion_sugerida}')
        return accion_sugerida
        

    def atender_fila(self, fila, menu):
        '''El cajero entra en la caja, le pasamos la fila de clientes y el menú para entregar la comida'''
        
        
        if len(fila) == 0:
            self.disponible = False
            #aunque no haya clientes en la fila, se queda en la caja
            return('No hay nadie en la fila para atender')
        else:
            if self.disponible == False:
                #si el cajero está ocupado, no puede atender la fila, se muestra si está jugando o descansando
                print(f'{self.nombre} no puede atender en la fila, está {self.disponible[1]}')
            else:
                #de forma random se le da una comida al cliente
                comida_entregada = random.choice(menu)
                #el cliente almacena la comida en su repertorio
                fila[0].hambre[1] = comida_entregada
                cliente_atendido = fila.pop(0)
                return(f' A {cliente_atendido.nombre} se le entregó {comida_entregada.nombre}')

                

    def jugar(self, Consola):
        '''La barra de cansancio disminuye cuando el cajero juega'''
        if not self.disponible:
            if Consola.disponible == False:
                print('Esa consola no está disponible')
            else:
                if self.disponible == False or self.barra_cansancio < 0:
                    if self.barra_cansancio > 0:    
                        Consola.jugar()
                        self.barra_cansancio -= 1
                        self.disponible = True
                    elif self.barra_cansancio == 0:
                        Consola.jugar()
                        print('El cajero ya está desestresado, podés sacarlo de la consola')
                    else:
                        print('El cajero está muy revitalizado, no jugará en un tiempo')
                else:
                    print('El cajero está disponible')
        




class Cliente(Accionable):
    '''Los clientes son el objeto que más interactúa con otros objetos, sus estados cuando se crean son randomizados'''
    def __init__(self, nombre, entusiasmo, estado_animo, hambre):
        self.nombre = nombre
        self.entusiasmo = entusiasmo
        self.estado_animo = estado_animo
        self.hambre = hambre  #pos 0: si se levanta o no con hambre, 1: la comida que tiene en mano
        self.disponible = [True, None, None, 0]        #pos 0: si está disponible o no, 1: La accion que realiza, 2: objeto que está usando, 3: la cantidad de turnos que la realiza 
        self.en_el_local = False

    def __str__(self):
        return (f'{self.nombre}, '
                f'Entusiasmo: {self.entusiasmo}, '
                f'Estado de ánimo: {self.estado_animo.get("Nombre")}, '
                f'disponible: {self.disponible}, '
                f'Hambre: {self.hambre}'
                f'En el local: {self.en_el_local}'
                )

    #implementar con el objeto sofa
    def descansar(self, Sofa):
        pass



    #implementar con el objeto consola
    def jugar(self, Consola):
        '''La consola '''        
        if self.disponible[0] == False:
            if self.disponible[1] != 'jugando':
                print(f'El cliente no puede jugar, está {self.disponible[1]}')
            else:
                Consola.jugar(self)
        else:
            print(f'{self.nombre} jugará a la consola {Consola.nombre}')
            Consola.jugar(self)

    def desjugar(self):
        '''Desconectamos el vínculo entre jugador y consola'''
        self.disponible = [True, None, None, 0]        #pos 0: si está disponible o no, 1: La accion que realiza, 2: objeto que está usando, 3: la cantidad de turnos que la realiza 

        self.disponible[0] = True
        self.disponible[1] = None

        self.disponible[2].desjugar()
        self.disponible[2] = None

        self.disponible[3] = 0
        

    #implementar con el objeto comida y objeto mesa
    def comer(self):
        pass

    #implementar con la fila de la caja
    def entrar_fila(self, fila):
        fila.append(self)