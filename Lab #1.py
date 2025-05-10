"""Ejercicio #11 -Actividad 4
ALGORITMO:
1. primera tabla <-- Solicitar al usuario
2. ultima tabla <-- Solicitar al usuario
3. while primera tabla <= ultima tabla 
    3.1 numero <-- 1 
    3.2 while numero <= 12 
        3.2.1 resultado <-- primera tabla x numero 
        3.2.2 print(primera tabla, "X", numero, "=", resultado) 
        3.2.3 numero <-- numero += 1
    3.3 siguiente tabla <-- primera tabla += 1       
"""
# Solicitar al usuario las tablas de multiplicar
primera_tabla = int(input("Indique la primera tabla:"))
ultima_tabla = int(input("Ahora indique la tabla de finalización:"))

# Crear todas las tablas
while primera_tabla <= ultima_tabla: #Inicio y final de la iteracion
    print("Tabla del", primera_tabla) #Se indica el numero de la tabla a desplegar
    numero = 1 #Numeros a multiplicar por los indicados por el usuario
    while numero <= 12: #Se multiplicara hasta 12 
        resultado = primera_tabla * numero #Resultado de cada una de las lineas de las tablas
        print(primera_tabla, "X", numero, "=", resultado) #
        numero += 1 #Se pasa a realizar la siguiente multiplicacion y se vuelve a hacer el bucle
    primera_tabla += 1 #Siguiente tabla
    print() #Crear un pequeño espacio entre tablas 

