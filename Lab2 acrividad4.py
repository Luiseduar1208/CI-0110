"""Ejercicio 13- Actividad 4 ENTREGABLE
ALGORITMO:
1. lista <-- []
2. i <-- 1
3. contador_intentos <-- 1.
4. while i <= 15
    4.1 num aleatorio <-- generar numero aleatorio(1, 100)
    4.2 lista <-- añadir num aleatorio
    4.3 i += 1
5. while contador_intentos <= 3
6. numero <-- solicitar al usuario
7. if numero pertenece a lista then
    7.1 print(ganador!)
    7.2 posicion <-- numero en que se encuentra en la lista
    7.3 print <-- su numero se encontraba en la posicion: posicion + 1
    7.4 break
8. else
    8.1 print <-- "Intenta de nuevo"
    8.2 contador de intentos <-- aumenta en 1 su valor
9. print <-- se ha quedado sin intentos, los numeros correctos eran:
10. print <-- lista
"""
#Importar librerias
import random as rn

#Declaraciones
lista = []
i = 1
contador_intentos = 1
#Generador de numeros
for i in range(15): 
    num_aleatorio = rn.randint(1, 100)
    lista.append(num_aleatorio)
#Match del numero del usuario con la lista
while contador_intentos <= 3:
    numero = int(input("Indique su numero:"))
    if numero in lista:
        print("ganador!")
        posicion = lista.index(numero)
        print("Su numero se encontraba en la posición:", posicion + 1)
        break
    else:
        print("Intenta de nuevo")
        contador_intentos += 1 
print("Los numeros correctos eran:")
for x in lista:
    print(x)
