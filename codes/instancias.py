from Modelo.comedor import *
from Modelo.estado_animo import *
from Modelo.interactuables import *
from Modelo.persona import *

def instanciar_objetos_comedor():
    cajero1 = Cajero("Cajero 1")
    cajero2 = Cajero("Cajero 2")

    clientes = [Cliente(f"Cliente{i+1}") for i in range(20)]

    consolas = [
        Consola("PSx"),
        Consola("Atari"),
        Consola("Sega Saturn"),
        Consola("PlayStation 2"),
        Consola("GameCube"),
    ]

    sofas = [
        Sofa("Negro", 1),
        Sofa("Azul", 2),
        Sofa("Blanco", 3),
        Sofa("Rosa", 4),
        Sofa("Turquesa", 5),
    ]


    # Crear el comedor con los objetos instanciados
    comedor = Comedor("BlackHeart", [cajero1, cajero2], clientes, consolas, sofas)
    

    return comedor

def instanciar_objetos_controlador():
    enojado = EstadoAnimo(0, 'enojado', [0])
    triste = EstadoAnimo(1, 'triste', [0,1])
    feliz = EstadoAnimo(2, 'feliz', [0,2])    

    estados = [enojado, triste, feliz]

    #comidas que pueden comer los clientes, meramente estético los nombres
    comidas = ["Lengua a la vinagreta", "Caviar", "Guiso de Mondongo", "Café con tostadas", "Lasagna", "Papas Fritas"]

    para_controlador = [estados, comidas]

    return para_controlador