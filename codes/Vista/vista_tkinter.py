import tkinter as tk
from tkinter import simpledialog


def inicializar_ventana(self, ventana, weight, height):
        # Define el tamaño de la ventana
        ventana.geometry(f"{weight}x{height}")  # Anchura x Altura en píxeles

        # Otros elementos de tu interfaz gráfica aquí
        etiqueta = tk.Label(ventana, text="BlackHeart")
        etiqueta.pack()

class VistaTkinter:
    def __init__(self, controlador):
        self.controlador = controlador
        self.ventana_principal = None

    def mostrar_ventana_inicial(self):
        # Crear ventana emergente inicial
        ventana_inicial = tk.Tk()
        inicializar_ventana(self, ventana_inicial, 200, 150)
        ventana_inicial.title("Inicio")

        etiqueta = tk.Label(ventana_inicial, text="¿Empezar?")
        etiqueta.pack()

        boton_si = tk.Button(ventana_inicial, text="Sí", command=self.abrir_ventana_principal)
        boton_si.pack(side=tk.LEFT)

        boton_no = tk.Button(ventana_inicial, text="No", command=ventana_inicial.destroy)
        boton_no.pack(side=tk.RIGHT)

        ventana_inicial.mainloop()
        self.abrir_ventana_principal()

    def abrir_ventana_principal(self):
        self.ventana_principal = tk.Tk()
        inicializar_ventana(self, self.ventana_principal, 800, 600)  # Llamar a la función correcta
        self.ventana_principal.title("Ventana Principal")

        dia = tk.Label(self.ventana_principal, text=f'Día {self.controlador.dias_transcurridos}, ')
        dia.grid(row=0, column=0, sticky='nw')

        turno = tk.Label(self.ventana_principal, text=f'\t Turno {self.controlador.turno_del_dia}')
        turno.grid(row=1, column=0, sticky='w')


        clientes_en_el_local = tk.Label(self.ventana_principal, text='Clientes en el local')
        clientes_en_el_local.grid(row=0, column=0, sticky='ne')
        numero_clientes = tk.Label(self.ventana_principal, text=f'{len(self.controlador.clientes_del_dia)}')
        numero_clientes.grid(row=1, column=0, sticky='e')

        #agregar funcion de mostrar_ventana_clientes
        ver_clientes = tk.Button(self.ventana_principal, text='Ver Clientes', 
                                 command=self.mostrar_ventana_clientes())
        ver_clientes.grid(row=0, column=0)
        
        controlar_cajeros = tk.Button(self.ventana_principal, text='Controlar cajeros', 
                                      command=self.mostrar_ventana_control_cajeros())
        controlar_cajeros.grid(row=1, column=0)


        terminar_turno = tk.Button(self.ventana_principal, text='Terminar turno', 
                                   command=self.mostrar_ventana_terminar_turno())
        terminar_turno.grid(row=0, column=0, sticky='se')


        self.ventana_principal.mainloop()

    def mostrar_ventana_clientes(self):
        # Crear ventana de texto de clientes disponibles y ocupados
        # ...
        pass
    def mostrar_ventana_control_cajeros(self):
        # Crear ventana emergente para controlar cajeros
        # ...
        pass
    def mostrar_ventana_ver_estado_cajero(self, cajero):
        # Crear ventana de texto para ver el estado del cajero
        # ...
        pass
    def mostrar_ventana_atender_fila(self, cajero, cliente):
        # Crear ventana de texto para atender la fila
        # ...
        pass
    def mostrar_ventana_sugerir_accion(self, cajero, cliente):
        # Crear ventana de texto para sugerir acción
        # ...
        pass
    def mostrar_ventana_jugar(self, cajero, consola):
        # Crear ventana de texto para jugar
        # ...
        pass
    def mostrar_ventana_descansar(self, cajero, sofa):
        # Crear ventana de texto para descansar
        # ...
        pass
    def mostrar_ventana_terminar_turno(self):
        # Crear ventana de texto para terminar el turno
        # ...
        pass
