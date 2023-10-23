from main import *

#prueba si funciona mi fila de clientes frente a la caja--(funciona)


lista_cajeros = el_comedor.caja.cajeros
fila_clientes = el_comedor.caja.fila

fila_clientes = el_comedor.clientes

lista_cajeros[0].atender_fila(fila_clientes, menu)

for cajero in lista_cajeros:
    print(cajero.nombre)


#