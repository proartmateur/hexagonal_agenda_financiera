# Micro Agenda

## Objetivo

Practicar lo aprendido respecto a la arquitectura Hexagonal(Ports & Adapters)

El proyecto no implenta CQRS es meramente un intento por entender cómo construir
una solución altamente mantenible.

La solución cuenta con un cliente <Presentation Layer> que consume la solución.

El archivo principal(Entry Point) se encuentra en:

    client
        |
         –- entry.py

## Reglas de negocio

    - Usuario
    Como user_manager de la agenda...
    Necesito actualizar la cantidad de creditos que tiene un usuario.
    Los créditos pueden cambiar si el deposita dinero.
    
    - Usuario
    Como user_manager puedo consultar la información de uno o más usuarios.
    
    - Negocio
    Cuando un usuario tenga 1_000_000 o más de créditos
    se emitirá un registro de VIP
    
    Un usuario VIP obtiene un descuento de 1 créditos por cada cargo
    
    Cuando un usuario tenga 0 créditos se emitirá una notificación 
    de usuario que ya no puede seguir en el sistema
    
    Cada día le cuesta 10 créditos a un usuario su existencia en el sistema
    
    Todos los usuarios inician con 100 créditos gratuitos
    