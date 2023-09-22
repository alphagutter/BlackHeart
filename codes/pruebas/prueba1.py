# Clase base Jugable
class Jugable:
    def jugar(self):
        pass

# Clase Cliente que hereda de Jugable
class Cliente(Jugable):
    def jugar(self):
        print("El cliente está jugando")

# Clase Cajero que hereda de Jugable
class Cajero(Jugable):
    def jugar(self, consola):
        print(f"El cajero está jugando en la consola {consola}")

# Clase Consola que hereda de Jugable
class Consola(Jugable):
    def jugar(self):
        print("La consola está siendo utilizada")

# Función para interactuar con un objeto Jugable
def interactuar(jugable):
    jugable.jugar()

# Ejemplo de uso
cliente = Cliente()
cajero = Cajero()
consola = Consola()

interactuar(cliente)
interactuar(cajero)
interactuar(consola)
