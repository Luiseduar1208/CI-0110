"""Ejerecicio 13- Actividad 1
AlGORITMO:
1. lista <-- []
2. i <-- 1
3. while i <= 10
    3.1 num aleatorio <-- generar numero aleatorio(1, 1000)
    3.2 lista <-- añadir num aleatorio
    3.3 i += 1
4 print(lista)
"""
#Importar librerias
import random as rn

#Declaraciones
lista = []
i = 1

#Generador de numeros
for i in range(10): #Va del 0 al 10
    num_aleatorio = rn.randint(1, 1000)
    lista.append(num_aleatorio)
for x in lista:
    print(x)

