from abc import ABC, abstractmethod

class Accionable:
    '''pequeña clase abstracta, donde definimos 2 clases a utilizar en distintos tipos, por el que ocurre el simple polimorfismo'''
    @abstractmethod
    def jugar():
        pass
    
    @abstractmethod
    def descansar():
        pass

class Empleado(Accionable):
    '''Es la clase abstracta con la que definimos los empleados del local'''
    
    @abstractmethod
    def limpiar():
        pass




class Cajero(Empleado):
    '''Es el empleado con el que interactuan los clientes, pueden limpiar, atender a los clientes, entre otras cosas'''
    def __init__(self, nombre, barra_cansancio):
        self.nombre = nombre
        self.barra_cansancio = barra_cansancio
        self.ocupado = False

    def __str__(self):
        return (f'Cajero: {self.nombre}, '
                f'Nivel de cansancio: {self.barra_cansancio}, '
                f'Ocupado: {self.ocupado}')

    #implementar mejor con el objeto sofa
    def descansar(self):
        if self.barra_cansancio == 0:
            print('El cajero está completamente descansado')
        elif self.barra_cansancio > 10:
            self.barra_cansancio -= 1
            print('El cajero está punto de colapsar')
        else: 
            self.barra_cansancio -= 1

    def limpiar(self):
        pass

    def sugerir_accion(self, cliente, accion_sugerida):

        if accion_sugerida == 1:
            accion_sugerida = 'Comer'
        elif accion_sugerida == 2:
            accion_sugerida = 'Descansar'
        elif accion_sugerida == 3:
            accion_sugerida = 'Jugar en la consola'

        print(f'El cajero sugiere al cliente {cliente.nombre}: {accion_sugerida}')
        

    def atender_fila(self):
        pass

    def jugar(self, Consola):
        '''La barra de cansancio disminuye cuando el cajero juega'''
        




class Cocinero(Empleado):
    '''Es el empleado encargado de cocinar para los clientes, reciben los pedidos que les pasan los cajeros, de acuerdo 
    a su nivel de cansancio, es más rentable o no que cocinen ciertas comidas de seguido'''
    def __init__(self, nombre, barra_cansancio):
        self.nombre = nombre
        self.barra_cansancio = barra_cansancio
        self.pedidos = []    #implementar una lista enlazada
        self.ocupado = False

    def __str__(self):
        return (f'Cocinero: {self.nombre}, '
                f'Nivel de cansancio: {self.barra_cansancio}, '
                f'Ocupado: {self.ocupado}, '
                f'Lista de pedidos a realizar: {self.pedidos}')

    #seguir implementando
    def cocinar(self):
        for self.pedidos in self.pedidos:
            if(self.pedidos == None):
                print('no hay pedidos')
            else:
                pass

    def limpiar(self):
        pass

    def descansar(self):
        if self.barra_cansancio == 0:
            print('El cocinero está completamente descansado')
        elif self.barra_cansancio > 10:
            self.barra_cansancio -= 1
            print('El cocinero está punto de colapsar')
        else: 
            self.barra_cansancio -= 1 

    def entregar_comida(self):
        pass




class Cliente(Accionable):
    '''Los clientes son el objeto que más interactúa con otros objetos, sus estados cuando se crean son randomizados'''
    def __init__(self, nombre, entusiasmo, estado_animo, hambre):
        self.nombre = nombre
        self.entusiasmo = entusiasmo
        self.estado_animo = estado_animo
        self.hambre = hambre
        self.ocupado = False
        self.en_el_local = False

    def __str__(self):
        return (f'{self.nombre}, '
                f'Entusiasmo: {self.entusiasmo}, '
                f'Estado de ánimo: {self.estado_animo.get("Nombre")}, '
                f'Ocupado: {self.ocupado}, '
                f'Hambre: {self.hambre}'
                f'En el local: {self.en_el_local}'
                )

    #implementar con la matriz de mapa
    def recorrer(self):
        pass

    #implementar con el objeto sofa
    def descansar(self, Sofa):
        
        if not self.ocupado:

            #si el sofá está disponible, se podrá descansar
            if Sofa.disponible:
                
                Sofa.descansar(self)
                estado = self.estado_animo.get("Valor")

                #si está muy bajon, su animo aumenta de a poco
                if estado <= 3:
                    self.entusiasmo += 1
                    self.ocupado = True
                    print(f"Aumentó su animo de {estado-1} a {estado}")
                #si tiene buen ánimo, este varia de acuerdo a la comodidad que le proporciona el sofá
                elif estado > 3 and estado < 20:
                    self.entusiasmo += Sofa.nivel_comodidad 
                    self.ocupado = True
                    print(f"Aumentó su animo de {estado-1} a {estado}")
            else:
                #si no está disponible, mandará un mensaje desde la función descansar de sofa igualmente
                Sofa.descansar(self)
        else:
            #si está muy emocionado, no va a querer descansar
            print('Está eufórico, no descansará aunque le obliguen')
            



    #implementar con el objeto consola
    def jugar(self, Consola):
            
            if not self.ocupado:

                if Consola.disponible == False:
                    print('Esa consola no está disponible')
                else:
                    estado = self.estado_animo.get("Valor")
                    if estado < 3:
                        print('El cliente no jugará ni aunque le obliguen')
                    else: 
                        if estado >= 3 and estado < 6:
                            Consola.jugar()
                            print(f'El cliente {self.nombre} está jugando a la consola {Consola.nombre}')
                            self.entusiasmo += 1
                        else:
                            Consola.jugar()
                            print(f'El cliente {self.nombre} está jugando a la consola {Consola.nombre}')
                            self.entusiasmo += 2
            else:
                print('El cliente está ocupado haciendo algo más')


    #implementar con el objeto comida y objeto mesa
    def comer(self):
        pass

    #implementar con 
    def entrar_fila(self):
        pass