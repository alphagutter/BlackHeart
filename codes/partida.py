from main import *
import random

    #voy a hacer un while que verifique si van pasando los dias
    #por cada dia van a haber 7 turnos
dias = [False] * 30

for dia, estado in enumerate(dias):

    print(f'Día {dia+1}')
    j=0
    while j < 7:
        print(f'Turno {j+1}')
        #máximo 5 personas pueden entrar en el local
        cuantos_nuevos = random.randint(1,5)
        nuevos = []
        # Selecciona aleatoriamente clientes desde la lista "clientes"
        clientes_seleccionados = random.sample(el_comedor.clientes, cuantos_nuevos)
        #metemos a los clientes elegidos randómicamente, le cambiamos el atributo de que están en el local a True
        nuevos = clientes_seleccionados
        for cliente in nuevos:
            el_comedor.personas_en_el_local(cliente, True)
        
        i = 0
        while i < len(el_comedor.clientes_en_local):
            cliente_actual = el_comedor.clientes_en_local[i]
            #verificamos el estado de animo que tiene el cliente
            #de acuerdo a ello va a hacer una u otra cosa
            ''' Valor 1 al 3: va a querer descansar nomás(verificar hambre)
                4 o 5: va a estar dispuesto a jugar(verificar entusiasmo)
                6: va a jugar, no importa qué(imposible descansar)
            '''
            print('----------------')
            print(f'El {cliente_actual.nombre} está {cliente_actual.estado_animo.get("Nombre")} \n')
            hacer_algo = random.choice([True,False])
            if hacer_algo == True:
                if cliente_actual.estado_animo['Valor'] <= 3:
                        descansar_sofa(cliente_actual)
                        comer_comida(cliente_actual)                     
                elif cliente_actual.estado_animo['Valor'] == (4 or 5):
                    comer_comida(cliente_actual)
                    jugar_consola(cliente_actual)
                elif cliente_actual.estado_animo['Valor'] == 6:
                    
                    jugar_consola(cliente_actual)
                else:
                    print('El cliente tiene un estado de ánimo no verificable')
            else:
                accion_sugerida = int(input(f'Sugerir accion: \n'
                                            f'1. Comer \n'
                                            f'2. Descansar \n'
                                            f'3. Jugar Consola \n' 
                                            f'>')
                                        )
                el_comedor.caja[0].sugerir_accion(cliente_actual, accion_sugerida)
            i += 1
        
        j+=1