from main import *
import random

    #voy a hacer un while que verifique si van pasando los dias
    #por cada dia van a haber 7 turnos

#renombramiento de objetos para utilizarlos de forma más cómoda luego

lista_cajeros = el_comedor.caja.cajeros
fila_clientes = el_comedor.caja.fila


for dia in range(1,2):

    print(f'****Día {dia}**** \n')
    for ronda in range(1,8):
        print(f'--Turno {ronda} \n\n')

        '''Esto de abajo es para que se vaya sumando la cantidad de turnos que una persona está
        realizando una accion'''
        for cliente_now in el_comedor.clientes_en_local:
            if len(el_comedor.clientes_en_local) == 0 :
                continue
            else:
                estado_aleatorio = random.choice(estados_de_animo)
                cliente_now.estado_animo = estado_aleatorio
                cliente_now.disponible[3] =+1

                realizacion_acciones(cliente_now.disponible[1], cliente_now)







        #máximo 5 personas pueden entrar en el local
        clientes_a_ingresar = random.randint(1,5)
        for _ in range(clientes_a_ingresar):
            clientes_disponibles = [cliente for cliente in el_comedor.clientes if not cliente.en_el_local]
            if clientes_disponibles:
                cliente_nuevo = random.choice(clientes_disponibles)
                cliente_nuevo.en_el_local = True
                el_comedor.clientes_en_local.append(cliente_nuevo)

        print(f'Clientes en el comedor en esta ronda: {len(el_comedor.clientes_en_local)}')

        i = 0
        clientes_sugestionables = []
        clientes_disponibles = []
        print(f'Ánimos de los clientes ingresados: \n')
        while i < len(el_comedor.clientes_en_local):
            cliente_actual = el_comedor.clientes_en_local[i]
            estado = cliente_actual.estado_animo
            #verificamos el estado de animo que tiene el cliente
            #de acuerdo a ello va a hacer una u otra cosa
            ''' Valor 1 al 3: va a querer descansar nomás(verificar hambre)
                4 o 5: va a estar dispuesto a jugar(verificar entusiasmo)
                6: va a jugar, no importa qué(imposible descansar)
            '''
            print(f'El {cliente_actual.nombre} está {cliente_actual.estado_animo.get("Nombre")}')

            #se elige randómicamente si el cliente hará algo o no en el turno
            #si no hace nada, se le guarda en el espacio para que un cliente pueda recomendarle
            #hacer algo
            moneda = random.choice([True,False])
            if moneda == True:
                if cliente_actual.disponible[0] == False:
                    #si el cliente está ocupado, lo añadimos a la lista de clientes ocupados
                    #para imprimir luego qué están haciendo
                    clientes_disponibles.append(cliente_actual)
                else:
                    if estado.get('Valor') == 1:
                        #Estado: Enojado, Acciones disponibles: comer
                        accion = 1                        
                        realizacion_acciones(accion, cliente_actual)
                    elif estado.get('Valor') == 2:
                        #Estado: Apático, Acciones disponibles: comer, dormir      
                        accion = random.randint(1,2)
                        realizacion_acciones(accion, cliente_actual)
                    elif estado.get('Valor') == 3:
                        #Estado: Deprimido, Acciones disponibles: comer, dormir, jugar
                        accion = random.randint(1,3)
                        realizacion_acciones(accion, cliente_actual)
                    elif estado.get('Valor') == 4:
                        #Estado: Triste, Acciones disponibles: comer, dormir, jugar
                        accion = random.randint(1,3)
                        realizacion_acciones(accion, cliente_actual)
                    elif estado.get('Valor') == 5:
                        #Estado: Feliz, Acciones disponibles: comer, jugar
                        accion = random.choice([1,3])
                        realizacion_acciones(accion, cliente_actual)
                    elif estado.get('Valor') == 6:
                        #Estado: Eufórico, Acciones disponibles: jugar
                        accion = 3
                        realizacion_acciones(accion, cliente_actual)
            else:
                clientes_sugestionables.append(cliente_actual)
            i += 1
        
        
        for accionable in el_comedor.clientes_en_local:
            print(f'{accionable.nombre} está {accionable.disponible[1]}, entusiasmo: {accionable.entusiasmo}')
            if accionable.disponible[1] == 'jugando':
                print(accionable.disponible[2])
        print(f'\n\n')