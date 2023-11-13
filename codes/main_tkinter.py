from Modelo.comedor import *
from Modelo.estado_animo import *
from Modelo.interactuables import *
from Modelo.persona import *

from Controlador.mecanicas_tkinter import *

from Vista.vista_tkinter import *


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

vista.mostrar_ventana_inicial()