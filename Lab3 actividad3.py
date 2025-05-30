"""EJERCICIO 15 - ACTIVIDAD 2
crear archivo <-- "Ejercicio 15-3 Aleatorioss.txt"
i = 1
while i <= 10000
    numero <-- generar numero aleatorio(1, 6000000)
    numero <-- añadir al archivo
    i += 1
archivo <-- close
print <-- "Se generaron los numeros correctamente"
"""
archivo = open(r"C:\Users\c5f958\Documents\Ejercicio 15-3 Aleatorios.txt", "w")
import random as rn

i = 1
while i <= 10000:
    numero = rn.randint(1, 6000000)
    archivo.write(str(numero) + "\n")
    i += 1
archivo.close()
print("Se generaron los numeros correctamente!")

