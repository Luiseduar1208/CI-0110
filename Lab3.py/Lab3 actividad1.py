"""EJERCICIO 15 - ACTIVIDAD 1
OBJETIVO: IDENTIFICAR CANTIDAD DE VECES QUE SALE LA PALABRA BEBIDA
ALGORITMO:
archivo <-- abrir
texto <-- cargar contenido del archivo
cuantas <-- funncion_contar("Bebidas", texto)
print <-- "se encontro", cuantas, "veces"
archivo <-- cerrar
"""
archivo = open(r"c:\Users\c5f958\Documents\Ejercicio 15-1 Archivo A.txt")
texto = archivo.read()
cuantas = texto.count("Bebidas")
print("La palabra aparece", cuantas, "veces.")
archivo.close()
