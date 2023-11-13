from Modelo.comedor import *
from Modelo.estado_animo import *
from Modelo.interactuables import *
from Modelo.persona import *

from Controlador.mecanicas import *

from Vista.VistaTexto import *


import transaction
from instancias import *
from database import *

#instanciamos el comedor
el_comedor = instanciar_objetos_comedor()

#llamamos a la base de datos
database = Database()
database.root.comedor = el_comedor

# guardamos los cambios hechos
transaction.commit()

comedor_recuperado = database.root.comedor

estados = instanciar_objetos_controlador()

juego = Mecanicas(0,0,comedor_recuperado, estados[0], estados[1])

vista = Vista(juego)

vista.inicio()
opcion = vista.obtener_respuesta()

if opcion == 'N':
    print('Gracias!!!')
else:
    while not juego.fin_de_juego:

        juego.aumentar_dia()

        vista.numero_dia()

        while juego.turno_del_dia < 7:

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
            
            juego.verificar_personas()


            


        vista.terminar_dia()

    vista.final_juego()


database.close()
        