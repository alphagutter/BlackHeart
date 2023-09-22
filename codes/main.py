from interactuables import *
from lugar import *
from humanos import *
import random

def crear_personas():
    '''Creamos acá los objetos cajero, cocinero y cajero'''
    crear_trabajadores()
    crear_clientes()

def crear_trabajadores():
    '''Acá creamos los trabajadores de forma genérica'''
    for i in range(1,3):
            el_comedor.agregar_trabajador(Cajero(f'Cajero{i}', 0))
            el_comedor.agregar_trabajador(Cocinero(f'Cocinero{i}', 0))


def crear_clientes():
    '''Creamos los 20 clientes con distintas emociones y estado inicial'''
    for i in range(1, 21):
        #cuando creamos un cliente, le damos por defecto un estado de ánimo completamente aleatorio, esto irá cambiando de acuerdo
        # al turno en el que estemos, su entusiasmo acumulado(o disminuido) por anteriores turnos se mantiene  
        estado_aleatorio = random.choice(estados_de_animo)

        nombre = "Cliente " + str(i)
        entusiasmo = 0
        estado_animo = {
        "Nombre": estado_aleatorio["Nombre"],
        "Valor": estado_aleatorio["Valor"]
    }
        hambre = random.choice([True, False])

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

#implementar comidas
comidas = ["Lasagna", "Caviar", "Papas Fritas", "Lengua a la vinagreta", "Guiso de Mondongo", "Café con tostadas"]
#implementar emociones
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

crear_personas()

crear_consolas()
crear_sofas()
crear_mesas()




def jugar_consola(cliente):
    #buscar si hay consolas disponibles primero
    for consola in el_comedor.consolas:
        if consola.disponible == True:
            consola_a_jugar = consola
            break
    
    if consola_a_jugar is not None:
        cliente.jugar(consola_a_jugar)
    else:
        print('No hay consolas disponibles')
        
def comer_comida(cliente):
    pass
def descansar_sofa(cliente):
    pass

def limpiar_pasillos(cliente):
    pass


#accion meramente para verificar si los objetos se crean de manera correcta
for accionable in el_comedor.zona_relax:
    pass  
    
#el_comedor.clientes[0].descansar(el_comedor.zona_relax[0])



    

