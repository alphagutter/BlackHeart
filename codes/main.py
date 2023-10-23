from interactuables import *
from lugar import *
from humanos import *
import random

def crear_personas():
    '''Creamos acá los objetos cajero, cocinero y cajero'''
    crear_trabajadores()
    crear_clientes()

def crear_trabajadores():
    '''Acá creamos los cajeros de forma genérica, tambien creamos una caja'''
    caja = Caja()
    for i in range(1,3):
            caja.cajeros.append(Cajero(f'Cajero{i}', 0))

    el_comedor.caja = caja
    

def crear_menu():

    menu = []

    for i in range(0, len(comidas)):
        comida = Comida(comidas[i], i)
        menu.append(comida)

    return menu      

def crear_clientes():
    '''Creamos los 20 clientes con distintas emociones y estado inicial'''
    for i in range(1, 21):
        #cuando creamos un cliente, le damos por defecto un estado de ánimo completamente aleatorio, 
        #esto irá cambiando de acuerdo al turno en el que estemos, su entusiasmo acumulado(o disminuido) 
        #por anteriores turnos se mantiene  
        estado_aleatorio = random.choice(estados_de_animo)

        nombre = "Cliente " + str(i)
        entusiasmo = 0
        estado_animo = {
        "Nombre": estado_aleatorio["Nombre"],
        "Valor": estado_aleatorio["Valor"]
    }   
        #elegimos randomicamente si tiene hambre, el segundo espacio es para almacenar la comida
        #que pueda tener
        hambre = [random.choice([True, False]), None]

        cliente = Cliente(nombre, entusiasmo, estado_animo, hambre)

        el_comedor.agregar_cliente(cliente)

def crear_consolas():
    '''Creamos aquí las consolas con las que los clientes y cajeros pueden jugar'''
    for i in range(len(nombres_consolas)):
        consola_nueva = Consola(nombres_consolas[i], True)

        el_comedor.agregar_consolas(consola_nueva)

def crear_sofas():
    '''Creamos los sofás donde los clientes pueden descansar'''

    for i in range(len(colores_sofas)):
        sofa_nuevo = Sofa(colores_sofas[i], i+1)
        el_comedor.agregar_sofas(sofa_nuevo)
        
def crear_mesas():
    pass


#comidas que pueden comer los clientes, meramente estético los nombres
comidas = ["Lengua a la vinagreta", "Caviar", "Guiso de Mondongo", "Café con tostadas", "Lasagna", "Papas Fritas"]


#Los estados de ánimo se le agregan a los clientes de manera aleatoria, con el paso de los días,
#el estado de animo de todos va cambiando, por lo que deben y quieren hacer otras cosas

'''Cada estado tiene características específicas:
    Enojado(Valor 1): Solo quiere comer, cuando come, cambia su estado a apático
    - Si es que un cajero le recomienda jugar videojuegos, sale de la tienda
    
    Apático(Valor 2): Quiere comer o dormir, cuando come cambia su estado a triste, cuando duerme
    se vuelve deprimido

    Deprimido(Valor 3): Quiere comer, dormir o jugar, si come o duerme se pone triste, si juega se pone 
    feliz

    Triste(Valor 4): Quiere comer, dormir o jugar, si come o duerme se pone feliz, si juega no cambia
    su estado

    Feliz(Valor 5): Quiere comer o jugar
    -si juega y su entusiasmo es más de 20, pasa de feliz a entusiasmado

    Eufórico(Valor 6):Solo quiere jugar
    -si le ofrecen dormir, sale de la tienda
    -si no hay consolas disponibles, sale de la tienda

    Incierto(Valor ?): Es un estado de ánimo que no se conoce, pero si tiene el valor y las propiedades
    de cualquiera de los valores del 1 al 6, si errás en la decisión, es una pena, es puro RNG
    

    '''
"""Enojado = 1, Apático = 2, Deprimido = 3, Triste = 4, Feliz = 5, Eufórico = 6, Incierto = random(invisble)"""
estados_de_animo = [{"Nombre": "Enojado", "Valor":1},
                    {"Nombre": "Apático", "Valor":2},
                    {"Nombre": "Deprimido", "Valor":3},
                    {"Nombre": "Triste", "Valor":4},
                    {"Nombre": "Feliz", "Valor": 5},
                    {"Nombre": "Eufórico", "Valor":6},
                    {"Nombre": "Incierto", "Valor":random.randint(1,6)}]



nombres_consolas = ["Playstation 2", "PSX", "Xbox", "Atari", "Sega Genesis"]

colores_sofas = ["Carmesi", "Purpura", "Aquamarine", "Negro", "Crema"]


el_comedor = Comedor("BlackHeart")

def realizacion_acciones(accion, persona):
    '''Acá elegimos la acción que randómicamente se elige que hará el cliente en el .py partida'''
    #1 = comer(entrar_fila), 2= dormir, 3= jugar
    
    if accion == 1 or accion == 'comiendo':
        comer_comida(persona)
    elif accion == 2 or accion == 'descansando':
        descansar_sofa(persona)
    elif accion == 3 or accion == 'jugando':
        jugar_consola(persona)
    else:
        print(f'{persona.nombre} no está haciendo nada')
        

crear_personas()
menu = crear_menu()

crear_consolas()
crear_sofas()
crear_mesas()




def jugar_consola(persona):
    #buscar si hay consolas disponibles primero

    #aqui verificamos si es que ya está jugando con alguna consola en específico,
    #para así no asignarle otra
    if persona.disponible[2] is not None:
        for consola_usada in el_comedor.consolas:
            if consola_usada.nombre == persona.disponible[2]:
                persona.jugar(consola_usada)
                return print('hola')

    #si es que el cliente no está jugando ya a alguna, le asignamos una consola random que esté disponible
    consola_a_jugar = None
    for consola in el_comedor.consolas:
        if consola.disponible == True:
            consola_a_jugar = consola
            break
    
    if consola_a_jugar is not None:
        persona.jugar(consola_a_jugar)
    else:
        print('No hay consolas disponibles')
        
def comer_comida(cliente):
    pass
def descansar_sofa(persona):
    pass


def controlar_cajeros(caja):
    
    print('Menú de cajeros de la ronda:')
    for cajero in caja:
        print(cajero.__str__)

    for cajero in caja:
        if cajero.ocupado == False:
            print(f'{cajero.nombre}: ')
            eleccion = int(input(f'1. Atender Fila \n'
                                 f'2. Sugerir acción a clientes \n'
                                 f'3. Jugar'))


    

