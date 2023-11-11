from Modelo.comedor import *
from Modelo.estado_animo import *
from Modelo.interactuables import *
from Modelo.persona import *

import random

#comidas que pueden comer los clientes, meramente estético los nombres
comidas = ["Lengua a la vinagreta", "Caviar", "Guiso de Mondongo", "Café con tostadas", "Lasagna", "Papas Fritas"]


class Mecanicas:
    def __init__(self, dias_transcurridos, turno_del_dia, comedor, tipos_estados):
        self.dias_transcurridos = dias_transcurridos
        self.turno_del_dia = turno_del_dia
        self.comedor = comedor
        self.clientes_del_dia = []
        self.clientes_moldeables = []
        self.clientes_nuevos = []
        self.tipos_estados = tipos_estados
        self.dia_actual = 0

        self.fin_de_juego = False

    def aumentar_dia(self):
        self.dias_transcurridos += 1

        if self.dias_transcurridos != self.dia_actual:
            self.turno_del_dia = 0
            self.dia_actual = self.dias_transcurridos
            self.clientes_del_dia.clear()
            self.clientes_nuevos.clear()
            self.reiniciar_estado_clientes()

            self.reiniciar_estado_cajeros()



        if self.dias_transcurridos > 15:
            self.fin_de_juego = True
        else:
            self.fin_de_juego = False

    def avanzar_turno(self):
        self.turno_del_dia += 1

        self.clientes_nuevos.clear()

        #realizamos las funciones que debe cumplirse cada día, como generar los clientes, o lanzar las monedas
        #para que realicen una u otra acción
        self.generar_clientes_turno()
        self.generar_estado_clientes()
        self.tirar_moneda()
        


    def generar_clientes_turno(self):
       #máximo 5 personas pueden entrar en el local
        clientes_a_ingresar = random.randint(1,3)
        print(f'Clientes nuevos en la ronda: {clientes_a_ingresar}')
        clientes_disponibles = [cliente for cliente in self.comedor.clientes if not cliente.en_el_local]
        seleccionados = random.sample(clientes_disponibles, min(clientes_a_ingresar, len(clientes_disponibles)))

        for cliente in seleccionados:
            cliente.en_el_local = True  # Marcamos como en el local
            self.clientes_nuevos.append(cliente)
            self.clientes_del_dia.append(cliente)

        print(f'Clientes en el comedor en esta ronda: {len(self.clientes_del_dia)}')


    def generar_estado_clientes(self):

        for cliente in self.clientes_nuevos:
            cliente.estado_animo = random.choice(self.tipos_estados)


    def tirar_moneda(self):
        '''Lanza una moneda que determina si el cliente va a realizar o no una acción por su cuenta.
        Si moneda == True, el jugador realiza una accion de acuerdo a su estado de ánimo,
        si moneda == False, entra en el array de clientes_moldeables, que serán atendidos
        por los cajeros cuando seleccionen sugerir_accion()'''
        for cliente in self.clientes_nuevos:
            moneda = random.choice([True,False])
            if moneda == True:

                if cliente.estado_animo == self.tipos_estados[0]:
                    #si el cliente está enojado
                    self.entrar_fila(cliente)
                elif cliente.estado_animo == self.tipos_estados[1]:
                    #si el cliente está triste
                    accion = random.choice(cliente.estado_animo.interactuables)

                    if accion == 0:
                        self.entrar_fila(cliente)
                    elif accion == 1:
                        self.descansar(cliente)
                    
                elif cliente.estado_animo == self.tipos_estados[2]:
                    #si el cliente está feliz
                    accion = random.choice(cliente.estado_animo.interactuables)

                    if accion == 0:
                        self.entrar_fila(cliente)
                    elif accion == 2:
                        self.jugar(cliente)
            else:
                self.clientes_moldeables.append(cliente)
            





    def atender_fila(self, cajero):
        '''El cajero le entrega una comida al cliente que está en frente de la fila'''

        #si en la fila no hay nadie, el cajero pierde su tiempo, y no puede hacer nada en ese turno
        if self.comedor.fila:
            clientes = self.comedor.fila
            comida = random.choice(comidas)

            cajero.atender_fila(clientes[0])

            clientes[0].objeto_utilizado = comida
            print(f'{cajero.nombre} entregó {comida} a {clientes[0].nombre}')

            self.comer(clientes[0])

            clientes.pop(0)

        else:
            print('No hay nadie en la fila')
        



    def sugerir_accion(self, cajero):
        '''El cajero le recomienda acciones a los clientes que están disponibles, se encuentran en el array de
        clientes moldeables (los clientes a los que la moneda les dio "False")'''

        #lista de clientes a expulsar
        clientes_a_expulsar = []
        clientes_atendidos = []

        if not self.clientes_moldeables:
            print('No hay clientes disponibles para sugerir')
        else:
            for cliente in self.clientes_moldeables:
                while True:
                    try:
                        print(f'¿Qué acción sugerirá {cajero.nombre} a {cliente.nombre} ?: \n'
                                    f'--0. Comer     \n'   
                                    f'--1. Descansar\n'  
                                    f'--2. Jugar')
                        opcion_cajero = int(input('> '))
                        if 0 <= opcion_cajero <= 2:

                            if opcion_cajero == 0:
                                cajero.sugerir_accion('comer')
                            elif opcion_cajero == 1:
                                cajero.sugerir_accion('descansar')
                            elif opcion_cajero ==2:
                                cajero.sugerir_accion('jugar')

                            break  # Salir del bucle si el valor es válido
                        else:
                            print("El número debe estar en el rango de 0 a 2. Inténtelo de nuevo.")
                    except ValueError:
                        print('Introduzca un valor válido.')

        #especificaciones de tipos de estados:
        #--enojado(0): solo quiere comer, si se le recomienda jugar, se retira del local, no se enoja si le recomiendan dormir
        #--triste(1): quiere comer o descansar, no se enoja si le recomiendan jugar
        #--feliz(2): quiere comer o jugar, no se enoja si le recomiendan jugar


                # Verificar si el cliente está enojado y la opción es jugar
                if cliente.estado_animo == self.tipos_estados[0]:

                    if opcion_cajero == 0:
                        self.entrar_fila(cliente)
                    elif opcion_cajero == 1:
                        print(f'El cliente no va a descansar')
                    elif opcion_cajero == 2:
                        clientes_a_expulsar.append(cliente)

                elif cliente.estado_animo == self.tipos_estados[1]:
                    
                    if opcion_cajero == 0:
                        self.entrar_fila(cliente)
                    elif opcion_cajero == 1:
                        self.descansar(cliente)
                    elif opcion_cajero == 2:
                        print(f'El cliente está muy triste para jugar')

                elif cliente.estado_animo == self.tipos_estados[2]:

                    if opcion_cajero == 0:
                        print(f'El cliente está muy feliz como para comer')
                    elif opcion_cajero == 1:
                        print(f'El cliente no va a descansar, está muy feliz para eso')
                    elif opcion_cajero == 2:
                        self.jugar(cliente)

                clientes_atendidos.append(cliente)

        self.clientes_moldeables = [cliente for cliente in self.clientes_moldeables if cliente not in clientes_atendidos]

        if clientes_a_expulsar is not None: self.expulsar_clientes(clientes_a_expulsar)
    

            

    def jugar(self, jugador):

        for consola in self.comedor.consolas:

            if consola.disponible == True:
                jugador.jugar(consola)
                consola.accion(jugador.nombre)
                return
            else:
                continue
            
        return(f'No hay consolas disponibles')
    

    def descansar(self, descansador):

        for sofa in self.comedor.zona_relax:

            if sofa.disponible == True:
                descansador.descansar(sofa)
                sofa.accion(descansador.nombre)
                return
            else:
                continue

        return(f'No hay sofás disponibles')
    
    def entrar_fila(self, cliente):
        '''Los clientes entrarán en la cola que se encuentra en el comedor, y serán atendidos por los cajeros en la función --atender_fila--'''
        self.comedor.fila.append(cliente)
        cliente.disponible = False

        print(f'{cliente.nombre} entró en la fila')




    def comer(self, cliente):
        '''Para las comidas no necesitamos que sean un objeto, ya que solo las usamos como String, y no como un objeto con su propia clase'''
        estado_cliente = 1


        #acá verificaremos el estado emocional del cliente, y de acuerdo a eso, lo sumaremos en su propia funcion de comer
        if isinstance(cliente.objeto_utilizado, str):
            #cliente enojado
            if cliente.estado_animo == self.tipos_estados[0]:
                #aquí le pasamos el estado predeterminado, ya que está enojado
                cliente.comer(estado_cliente)
                #cambiamos de enojado a triste
                cliente.estado_animo = self.tipos_estados[1]

            #cliente triste
            elif cliente.estado_animo == self.tipos_estados[1]:
                estado_cliente = 2
                cliente.comer(estado_cliente)

                #cambiamos de triste a feliz
                cliente.estado_animo = self.tipos_estados[2]

            #cliente feliz
            elif cliente.estado_animo == self.tipos_estados[2]:
                
                #no se cambia su estado de ánimo
                estado_cliente = 4
                cliente.comer(estado_cliente)

        else:
            return(f'{cliente.nombre} no tiene una comida en su inventario')




    def expulsar_clientes(self, clientes_a_expulsar):
        '''Expulsar a los clientes enojados de la lista de clientes moldeables'''
        for cliente in clientes_a_expulsar:
            self.clientes_moldeables.remove(cliente)
            self.clientes_del_dia.remove(cliente)
            print(f'El cliente {cliente.nombre} salió de la tienda, probablemente se enojó')

        clientes_a_expulsar.clear()
        
    def reiniciar_estado_clientes(self):
        for cliente in self.comedor.clientes:
                cliente.en_el_local = False
                cliente.estado_animo = None
                cliente.disponible = True


    def accion_realizada(self, persona):
        '''Acá conseguimos la acción que la persona realiza con el objeto que tiene en su inventario, aplica
        para cajeros o clientes'''
        objeto = persona.objeto_utilizado

        if isinstance(objeto, Consola):
            accion = 'jugando'
        elif isinstance(objeto, Sofa):
            accion = 'descansando'


        return(f'está {accion} con {objeto.nombre}')
    
    def verificar_clientes(self):

        if self.clientes_del_dia:

            for cliente in self.clientes_del_dia:
                if not cliente.disponible:
                    '''Verificamos si el cliente está con algún objeto en su inventario'''
                    if isinstance(cliente.objeto_utilizado, Consola):
                        cliente.jugar(cliente.objeto_utilizado)
                    elif isinstance(cliente.objeto_utilizado, Sofa):
                        cliente.descansar(cliente.objeto_utilizado)

                elif cliente.tiempo_ocupado >=3:
                    self.desaccionar(cliente)


    def reiniciar_estado_cajeros(self):

        for cajero in self.comedor.caja:
            cajero.barra_cansancio = 0
            self.desaccionar(cajero)


    def desaccionar(self, persona):
        
        if isinstance(persona.objeto_utilizado, Consola):
            persona.objeto_utilizado.des_accionar()
            persona.des_jugar()
        elif isinstance(persona.objeto_utilizado, Sofa):
            persona.objeto_utilizado.des_accionar()
            persona.des_descansar()
