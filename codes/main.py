from Modelo.comedor import *
from Modelo.estado_animo import *
from Modelo.interactuables import *
from Modelo.persona import *


from Controlador.mecanicas import *

from Vista.VistaTexto import *

#comer = 0, descansar = 1, jugar = 2

#Enojado = comer
#Triste = comer o descansar
#Feliz = descansar o jugar

cajero1 = Cajero("Cajero 1")
cajero2 = Cajero("Cajero 2")


# Crear 20 instancias de Cliente con nombres únicos del 1 al 20
clientes = [Cliente(f"Cliente{i}") for i in range(1, 21)]

# Imprimir los nombres de los clientes


consola1 = Consola('Playstation')
consola2 = Consola('Atari')
sofa1 = Sofa('Carmesi', 2)
sofa2  = Sofa('Violeta', 3)

caja = []
caja.append(cajero1), caja.append(cajero2)


consolas = [consola1, consola2]

sofas = [sofa1, sofa2]

el_comedor = Comedor('BlackHeart', caja, clientes, consolas, sofas)

enojado = EstadoAnimo(0, 'enojado', [0])
triste = EstadoAnimo(1, 'triste', [0,1])
feliz = EstadoAnimo(2, 'feliz', [0,2])

estados = [enojado, triste, feliz]

juego = Mecanicas(0,0,el_comedor, estados)

vista = Vista(juego)

vista.inicio()
opcion = vista.obtener_respuesta()

if opcion == 'N':
    print('Gracias!!!')
else:
    while not juego.fin_de_juego:

        juego.aumentar_dia()

        vista.numero_dia()

        juego.verificar_clientes()

        while juego.turno_del_dia < 4:

            juego.avanzar_turno()

            vista.numero_turno()

            opcion_turno = 0

            while opcion_turno <= 1:
                opcion_turno = vista.opcion_turno()

                if opcion_turno == 1:
                    vista.imprimir_clientes()
                elif opcion_turno == 2:
                    vista.opcion_cajeros()
                else:
                    continue

            


        vista.terminar_dia()

    vista.final_juego()



        