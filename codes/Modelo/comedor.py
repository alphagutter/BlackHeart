import persistent

class Comedor(persistent.Persistent):
    '''Es el objeto de el lugar en si, donde almacenamos la caja donde están los cajeros,
    la cocina donde están los cocinceros, a los clientes que vienen a interactuar, las consolas y los sofás'''
    def __init__(self, nombre, caja, clientes, consolas, zona_relax):
        self.nombre = nombre
        self.caja = caja
        self.fila = []                      #donde estan los clientes que quieren comer
        self.clientes = clientes            #array de clientes
        self.consolas = consolas            #array de consolas
        self.zona_relax = zona_relax        #array de sofás

