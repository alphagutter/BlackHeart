% Hechos que representan a las personas y sus estados de ánimo
persona(personaFeliz, feliz).
persona(personaTriste, triste).
persona(personaEnojada, enojado).

% Reglas de recomendación de acción a la hora de saber el ánimo de la persona
recomendar_accion(Persona, Accion):-
    persona(Persona, feliz),
    (Accion = jugar; Accion = comer).

recomendar_accion(Persona, Accion):-
    persona(Persona, triste),
    (Accion = comer; Accion = descansar).

recomendar_accion(Persona, Accion):-
    persona(Persona, enojado),
    Accion = comer.

% Función que determina la reacción de una persona a una acción que se le recomienda
reaccion_accion(Persona, Accion):-
    persona(Persona, EstadoAnimo),(
	
        (EstadoAnimo = feliz, (Accion = jugar; Accion = comer), write('La persona está feliz y acepta la recomendación.'));
        (EstadoAnimo = triste, (Accion = comer), write('La persona está triste pero acepta la recomendación.'));
		(EstadoAnimo) = triste, Accion \= descansar, write('Está muy triste, se quedará toda la noche durmiendo');
        (EstadoAnimo = enojado, Accion = comer, write('La persona está enojada pero acepta comer.'));
        (EstadoAnimo = enojado, Accion \= comer, write('La persona está enojada y se marcha del lugar.'))
    ).

% Ejemplos de consultas

% si la persona está feliz, estará feliz de aceptar la recomendacion de jugar
?- reaccion_accion(personaFeliz, jugar).

% si la persona está triste y le recomendamos descansar, dormirá toda la noche
?- reaccion_accion(personaTriste, descansar).

% si la persona está enojada y le recomendamos jugar, se marchará del local
?- reaccion_accion(personaEnojada, jugar).

% si la persona está enojada y le recomendamos comer, si comerá
?- reaccion_accion(personaEnojada, comer).
