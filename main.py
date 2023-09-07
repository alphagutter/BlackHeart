from clasestotales import *
import random

def crear_trabajadores():
    i=0
    '''Acá creamos los trabajadores de forma genérica'''
    while i<2:
        el_comedor.agregar_trabajador(Cajero(f'Cajero{i+1}', 0))
        el_comedor.agregar_trabajador(Cocinero(f'Cocinero{i+1}', 0))
        i += 1

#prueba de crear 20 clientes
def crear_clientes():
    '''Creamos los 20 clientes con distintas emociones y estado inicial'''
    for i in range(1, 21):
        nombre = "Cliente" + str(i)
        entusiasmo = 0
        estado_animo = ''
        hambre = random.choice([True, False])

        cliente = Cliente(nombre, entusiasmo, estado_animo, hambre)

        el_comedor.clientes.append(cliente)
#        print(cliente.hambre)

#implementar comidas
comidas = ["Lasagna", "Caviar", "Papas Fritas", "Lengua a la vinagreta", "Guiso de Mondongo", "Café con tostadas"]
#implementar emociones
"""Enojado = 1, Deprimido = 2, Triste = 3, Apático = 4, Feliz = 5, Eufórico = 6, Incierto = random(invisble)
"""
estados_de_animo = ["Feliz", "Triste", "Apático", "Enojado", "Deprimido", "Incierto", "Eufórico"]

nombres_consolas = ["Playstation 2", "PSX", "Xbox", "Atari", "Sega Genesis"]


el_comedor = Comedor("SuperComedor")
crear_trabajadores()
crear_clientes()
el_comedor.agregar_personas()

def jugar_consola():
    pass
def comer_comida():
    pass
def descansar_sofa():
    pass
def recorrer_pasillos():
    pass
def limpiar_pasillos():
    pass

for personas in el_comedor.total_accionable:
    print(str(personas.nombre))

#simple ejemplo de mi posible polimorfismo de turnos(version de caracteres)

turno1 = [Cajero("CajeroPrueba", 0), Cliente("Cliente", 0, 5, True), Consola("Playstation")]

#se coloca en un for a los objetos cajero, cliente y consola
for accionable in turno1:
    #si el objeto es cajero, se utiliza la sobreescritura de la clase jugar en cliente
    #para usar el objeto consola que hay en la lista, y a la vez modificarlo
    if isinstance(accionable, Cliente):
        turno1[2].disponible = accionable.jugar(turno1[2])
        break
    else: 
        accionable.jugar()
