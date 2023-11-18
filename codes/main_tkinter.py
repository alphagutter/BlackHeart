from Modelo.comedor import *
from Modelo.estado_animo import *
from Modelo.interactuables_tkinter import *
from Modelo.persona_tkinter import *

from Controlador.mecanicas_tkinter import *

from Vista.VistaTkinter import *


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

vista = VistaTkinter(juego)


juego.aumentar_dia()

vista.inicio()


while not juego.fin_de_juego:

    juego.aumentar_dia()

    while juego.turno_del_dia < 7:
        juego.avanzar_turno()

        if vista.ventana_principal == None:
            vista.crear_ventana_principal()
        
        juego.verificar_personas

    vista.terminar_dia()


vista.final_juego()

database.close()
        