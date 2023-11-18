from tkinter import *
from tkinter import messagebox

class VistaTkinter:
    def __init__(self, controlador):
        self.controlador = controlador

        self.ventana_introductoria = None
        self.ventana_principal = None
        self.ventana_cajero_actual = None
        self.ventana_sugerir_accion = None



    def inicio(self):  
        '''Ventana inicial, para inicializar o no el juego'''
        self.ventana_introductoria = Tk()
        self.ventana_introductoria.title('BlackHeart')
        self.ventana_introductoria.geometry('300x100')
        self.ventana_introductoria.resizable(0, 0)      
        
        Label(self.ventana_introductoria, text='Enamora a tus clientes, con el mundo de los videojuegos \n empezar?').grid(row=0, column=0, columnspan=2, pady=10)
        #si el jugador no presiona el boton_si, el juego no se abrirá y el estado de fin_del_juego se volverá true

        boton_si = Button(self.ventana_introductoria, text='Sí', command=self.cerrar_ventana_inicial)
        boton_si.grid(row=1, column=0, padx=10)

        boton_no = Button(self.ventana_introductoria, text='No', command=self.ventana_introductoria.destroy)
        boton_no.grid(row=1, column=1, padx=10)

        self.ventana_introductoria.mainloop()


    def cerrar_ventana_inicial(self):
        self.ventana_introductoria.destroy()
        self.crear_ventana_principal()

        

    def crear_ventana_principal(self):
        '''Plantilla para la ventana principal del juego'''
        self.ventana_principal = Tk()
        self.ventana_principal.title('BlackHeart')
        self.ventana_principal.geometry('800x600')
        self.ventana_principal.resizable(0, 0)

        self.actualizar_ventana_principal(self.ventana_principal)

        

    def crear_nueva_ventana(self, titulo, tamanho):
        window = Tk()
        window.title(titulo)
        window.geometry(tamanho)
        window.resizable(0, 0)

        return window

    def actualizar_ventana_principal(self):
        '''Verificará cada vez que entra aquí si el día varia'''

        dia_actual = self.numero_dia()

        dia = Label(self.ventana_principal, text = dia_actual)
        dia.grid(row=0, column=0)

        turno_actual = self.numero_turno()

        turno = Label(self.ventana_principal, text = turno_actual)
        turno.grid(row=1, column=0)

        clientes_local = f'Clientes del día: {len(self.controlador.clientes_del_dia)}'

        clientes = Label(self.ventana_principal, text = clientes_local)
        clientes.grid(row=0, column=4)


        ver_clientes = Button(self.ventana_principal, text='Ver clientes', command= self.ver_clientes)
        ver_clientes.grid()

        controlar_cajeros = Button(self.ventana_principal, text='Controlar cajeros', command = self.controlar_cajeros)
        controlar_cajeros.grid()

        terminar_turno = Button(self.ventana_principal, text='Terminar turno', command = self.terminar_turno)
        terminar_turno.grid()
        
    def numero_dia(self):
        
        return f'Dia {self.controlador.dias_transcurridos}'

    def numero_turno(self):

        return f'    Turno {self.controlador.turno_del_dia}'


    
    def ver_clientes(self):
        '''Ventana emergente para ver los clientes que están en el local'''
        
        window = self.crear_nueva_ventana('Lista de Clientes', '400x400')

        clientes = self.controlador.clientes_del_dia
        
        disponibles = 'Clientes disponibles: \n'
        ocupados = 'Clientes ocupados: \n'

        if clientes is not None:
            for cliente in clientes:
                if cliente:
                    disponibles += (f'Cliente: {cliente.nombre} \n Estado: {cliente.estado_animo.nombre}'
                                    f'Entusiasmo: {cliente.entusiasmo} ')
                    disponibles += '\n'
                else:
                    ocupados += (f'Cliente: {cliente.nombre} \n Estado: {cliente.estado_animo.nombre}'
                                    f'Entusiasmo: {cliente.entusiasmo} ')
                    ocupados += '\n'
                    

            clientes_disponibles = Label(window, text=disponibles)
            clientes_disponibles.grid(row=0,column=0)

            clientes_ocupados = Label(window, text=ocupados)
            clientes_ocupados.grid(row=1,column=0)

        else:
            clientes_vacio = Label(window, text='No hay clientes Nuevos')
            clientes_vacio.grid(row=0,column=0)

        



    def controlar_cajeros(self):
        '''Creamos una ventana por cajero, en la que tenemos la opción de ver sus estados, atender la fila
            de clientes hambrientos, sugerir una acción a los clientes libres, jugar a alguna consola, o descansar'''
        for cajero in self.controlador.comedor.caja:
            
            if cajero.disponible is False:
                messagebox.showinfo(f'el cajero está ocupado, {self.controlador.accion_realizada(cajero)}\n')
            else:

                self.ventana_cajero_actual = self.crear_nueva_ventana('Controlar Cajeros', '600x500')
                Label(self.ventana_cajero_actual, text=f'{cajero.nombre}: ').grid(row=0, column=0)

                

                ver_estado = Button(self.ventana_cajero_actual, text='Ver estado del cajero', command=lambda: self.ver_estado_cajero(cajero))
                ver_estado.grid(row=1, column=0)

                atender_fila = Button(self.ventana_cajero_actual, text='Atender la fila', command=lambda: self.atender_fila(cajero))
                atender_fila.grid(row=2, column=0)

                sugerir_accion_clientes = Button(self.ventana_cajero_actual, text='Sugerir una acción a los clientes', command = self.sugerir_accion)
                sugerir_accion_clientes.grid(row=3, column=0)

                jugar = Button(self.ventana_cajero_actual, text='Jugar', command=lambda: self.accion_cajero(cajero, 'jugar'))
                jugar.grid(row=4, column=0)

                descansar = Button(self.ventana_cajero_actual, text='Descansar', command=lambda: self.accion_cajero(cajero, 'descansar'))
                descansar.grid(row=5, column=0)

                self.ventana_cajero_actual.mainloop()

    def ver_estado_cajero(self, cajero):
        '''Sirve para ver en qué situación el cajero se encuentra'''
        window = self.crear_nueva_ventana(f'{cajero.nombre}', '300x150')

        estado_cajero = Label(window, text=(f'Cansancio: {cajero.barra_cansancio}'))
        estado_cajero.grid()
        

    def atender_fila(self, cajero):
        '''El cajero atiende a todos los clientes que están en la fila, esperando'''
        self.controlador.atender_fila(cajero)

        self.ventana_cajero_actual.destroy()


    def sugerir_accion(self, cajero):
        '''El cajero elegido sugerirá una acción a los clientes que estén disponibles para realizar una acción'''

        if not self.controlador.clientes_moldeables:
            messagebox.showerror('No hay clientes disponibles para sugerir')
            self.ventana_cajero_actual.destroy()
        else:
            for cliente in self.controlador.clientes_moldeables:

                self.ventana_sugerir_accion = self.crear_nueva_ventana('Sugerir acción', '500x350')
                sugerencia = Label(self.ventana_sugerir_accion, text=f'¿Qué acción sugerirá {cajero.nombre} a {cliente.nombre} ?:')
                sugerencia.grid(row=0,column=0)
                
                comer = Button(self.ventana_sugerir_accion, text='Comer', command=lambda: self.accion_cliente('comer',cliente))
                comer.grid(row=1, column=0)

                descansar = Button(self.ventana_sugerir_accion, text='Descansar', command=lambda: self.accion_cliente('descansar',cliente))
                descansar.grid(row=1, column=0)

                jugar = Button(self.ventana_sugerir_accion, text='Jugar', command=lambda: self.accion_cliente('jugar',cliente))
                jugar.grid(row=1, column=0)

                if cliente.disponible is False: self.controlador.clientes_atendidos.append(cliente)

        for cliente in self.controlador.clientes_atendidos:
            self.controlador.clientes_moldeables.remove(cliente)

        if self.controlador.clientes_a_expulsar:
            self.controlador.expulsar_clientes(self.controlador.clientes_a_expulsar)

    def accion_cliente(self, accion, cliente):
        '''Le pasamos la acción que realizará el cliente'''
        if accion == 'comer':
            self.controlador.comer(cliente)
            self.ventana_sugerir_accion.destroy()
        elif accion == 'descansar':
            self.controlador.descansar(cliente)
            self.ventana_sugerir_accion.destroy()
        elif accion == 'jugar':
            self.controlador.jugar(cliente)
            self.ventana_sugerir_accion.destroy()


    def accion_cajero(self, cajero, accion):
        '''De acuerdo a la elección que se haga del cajero, se hará una u otra cosa'''
        if accion == 'jugar':
            messagebox.showinfo(self.controlador.jugar(cajero))
        elif accion == 'descansar':
            messagebox.showinfo(self.controlador.descansar(cajero))

        self.ventana_cajero_actual.destroy()

    def terminar_turno(self):
        self.ventana_principal.destroy()

    

    def terminar_dia(self):
        self.controlador.aumentar_dia()
        self.ventana_principal.destroy()
            
            
    def final_juego(self):
        '''Se muestran los puntajes finales del juego'''
        if self.ventana_principal:
            self.ventana_principal.destroy()
        else:
            messagebox.showinfo('Gracias por participar!')

        window = self.crear_nueva_ventana('Fin del juego', '800x600')

        Label(window, text='tus mejores clientes: ').grid(row=0,column=0)

        clientes_fieles = []
        estados = ""

        for cliente in self.controlador.comedor.clientes:

            if cliente.entusiasmo >= 5:

                clientes_fieles.append(cliente)

        for cliente in clientes_fieles:

            estados += (f'{cliente.nombre}: {cliente.entusiasmo}')

        Label(window, text=estados).grid(row=1,column=0)

        total_puntos = len(clientes_fieles)

        Label(window, text=f'tu puntaje es de: {total_puntos}').grid(row=2, column=0)

        Label(window, text=f'gracias por jugar! <3').grid(row=3, column=0)