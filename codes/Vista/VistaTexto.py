class Vista:
    def __init__(self, controlador):
        self.controlador = controlador

    def inicio(self):
        print('BlackHeart')
        print('--Un comedor especial--')
        print('             Enamora a tus clientes, con el mundo de los videojuegos')


    def obtener_respuesta(self):
        respuesta = input("empezar?  'N' o 'Y': ")
        respuesta = respuesta.upper()  
        if respuesta == 'N' or respuesta == 'Y':
            return respuesta
        else:
            print("Respuesta inválida. Por favor, ingresa 'N' o 'Y'.")
            return self.obtener_respuesta()
        
    def numero_dia(self):
        
        print(f'Dia {self.controlador.dias_transcurridos}')

    def numero_turno(self):

        print(f'    Turno {self.controlador.turno_del_dia}')

    def opcion_turno(self):

        while True:

            try: 
                print(f'Opciones del turno: \n'
                            f'--1. Ver Clientes     \n'   
                            f'--2. Controlar Cajeros\n'  
                            f'--3. Terminar Turno')

                opcion = int(input('> '))

                if 1 <= opcion <= 3:
                    break
                else:
                    print("El número debe estar en el rango de 1 a 4. Inténtelo de nuevo.")
            except ValueError:
                print("Ingrese un número entero válido.")

        
        return opcion
    
    def imprimir_clientes(self):
        clientes = self.controlador.clientes_del_dia

        if clientes is not None:
            for cliente in clientes:

                if cliente.disponible:
                    disponibilidad = 'disponible'
                else:
                    disponibilidad = 'ocupado'



                #imprimimos la disponibilidad del cliente
                print(f'>>>>    El cliente {cliente.nombre} está {disponibilidad}')
                print(f'         Estado: {cliente.estado_animo.nombre}, entusiasmo: {cliente.entusiasmo}')
                
        else:
            print('No hay clientes nuevos\n\n')

    def opcion_cajeros(self):
        cajeros = self.controlador.comedor.caja

        while any(cajero.disponible for cajero in cajeros):

            for cajero in cajeros:

                if cajero.disponible:

                            print(f'Controla al cajero {cajero.nombre}: \n'
                                    f'--1. Ver estado del cajero        \n'
                                    f'--2. Atender Fila                 \n'
                                    f'--3. Sugerir Acción               \n'
                                    f'--4. Jugar                        \n'
                                    f'--5. Descansar                    \n')
                                    
                            opcion_cajero = int(input('> '))
                            if opcion_cajero == 1:
                                self.mostrar_estado_cajero(cajero)
                            elif opcion_cajero in [2, 3] and cajero.barra_cansancio >= 5:
                                print('El cajero está burnout, no quiere trabajar\n\n')
                            else:
                                if opcion_cajero == 2:
                                    self.controlador.atender_fila(cajero)
                                elif opcion_cajero == 3:
                                    self.controlador.sugerir_accion(cajero)
                                elif opcion_cajero == 4:
                                    self.controlador.jugar(cajero)
                                elif opcion_cajero == 5:
                                    self.controlador.descansar(cajero)
                elif not cajero.disponible:
                    try:
                        print(f'el cajero está ocupado, {self.controlador.accion_realizada(cajero)}\n')
                    except AttributeError as e:
                        print(f"Error: {e}")


    def terminar_dia(self):

            print(f'\n\n=== puse F para continuar... ===')

            opcion_usuario = input('> ')
            opcion_usuario.upper()

            if opcion_usuario == 'F' or opcion_usuario == 'f':
                return
            else:
                return self.terminar_dia()
            
    def final_juego(self):

        print(f'\n\n\n La partida ha terminado!!')

        clientes_fieles = []

        for cliente in self.controlador.comedor.clientes:

            if cliente.entusiasmo >= 5:

                clientes_fieles.append(cliente)

        print(f'******++++++******++++++*****++++++*****')
        print(f'Estos son los mejores clientes:')

        for cliente in clientes_fieles:

            print(f'{cliente.nombre}: {cliente.entusiasmo}')

        total_puntos = len(clientes_fieles)

        print(f'\n')
        print(f'******++++++******++++++*****++++++*****')
        
        print(f'Tu puntaje es de: {total_puntos}')
        print(f'Gracias por jugar! <3')

    def mostrar_estado_cajero(self, cajero):
        print(f'@@  Cajero: {cajero.nombre}'
              f'    cansancio: {cajero.barra_cansancio}')