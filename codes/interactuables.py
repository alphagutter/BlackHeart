from abc import ABC, abstractmethod
from humanos import *

class Sofa:
    '''Objeto con el que los objetos que heredan de "Accionable" pueden descansar'''
    def __init__(self, color, nivel_comodidad):
        self.color = color
        self.nivel_comodidad = nivel_comodidad
        self.disponible = True
        self.ocupante = None

    def __str__(self):
        return(
            f'Color: {self.color}, '
            f'Nivel de comodidad: {self.nivel_comodidad}, '
            f'Disponible: {self.disponible}, '
            f'Ocupante: {self.ocupante}'
        )
        

    def descansar(self, ocupante):
        if self.disponible:
            self.disponible = False
            self.ocupante = ocupante
            print(f"{ocupante.nombre} está descansando en el sofa de color {self.color}")

        else:
            print(f"el sofá de color {self.color} no está disponible")

class Consola:
    '''Las consolas con las que los clientes/cajeros pueden jugar, cambian su disponibilidad si alguno las está usando, cambian los estados de las personas'''
    def __init__(self, nombre, disponible = True):
        self.nombre = nombre
        self.disponible = disponible
        self.ocupante = None

    def __str__(self):
        return (
            f'Nombre: {self.nombre}, '
            f'Disponible: {self.disponible}, '
            f'Jugador: {self.ocupante}, '
        )


    #el print es distinto si la consola está en uso o no
    def jugar(self, jugador):
        if self.disponible == False:

            if self.ocupante == jugador.nombre:
                if hasattr(jugador, 'barra_cansancio'):
                    jugador.barra_cansancio =- 1
                elif hasattr(jugador, 'entusiasmo'):
                    jugador.entusiasmo =+ 1
            else:
                print(f'La consola{self.nombre} está ocupada')
        else:
            self.disponible = False
            self.ocupante = jugador.nombre
            jugador.disponible[0] = False
            jugador.disponible[1] = 'jugando'
            jugador.disponible[2] = self.nombre
            if hasattr(jugador, 'barra_cansancio'):
                jugador.barra_cansancio =- 1
            elif hasattr(jugador, 'entusiasmo'):
                jugador.entusiasmo =+ 1

    def desjugar(self):

        self.disponible = True
        self.ocupante = None


class Comida:
    '''Las comidas cambian el estado de hambre de los clientes'''
    def __init__(self, nombre, nivel_sabor):
        self.nombre = nombre
        self.nivel_sabor = nivel_sabor

    def comer(self):
        pass


class Mesa:
    '''Las mesas son utilizadas por los clientes cuando comen, cambian su disponibilidad cuando algún cliente las usa'''
    def __init__(self, numero_mesa):
        self.numero_mesa = numero_mesa
        self.disponible = True
        self.ocupante = None

    def __str__(self):
        return(
            f'Numero de mesa: {self.numero_mesa}, '
            f'Disponible: {True}, '
            f'Ocupante: {self.ocupante}'
        )

    def sentarse(self):
        if(self.disponible == False):
            print('la mesa está ocupada')
        else:
            print(f'El cliente está sentado en la mesa {self.numero_mesa}')