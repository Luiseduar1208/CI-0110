"""EJERCICIO 15 - ACTIVIDAD 2
archivo1 <-- abrir archivo 1
archivo2 <-- abrir archivo 2
texto1 <-- cargar contenido archivo1
texto2 <-- cargar contenido archivo2
if texto1 == texto2 then:
    print <-- son iguales
else 
    print <--son diferentes
"""
archivo1 = open(r"C:\Users\c5f958\Documents\Ejercicio 15-2 Archivo A.txt")
archivo2 = open(r"C:\Users\c5f958\Documents\Ejercicio 15-2 Archivo B.txt")

texto1 = archivo1.read()
texto2 = archivo2.read()
if texto1 == texto2:
    print("Son iguales")
else:
    print("Son diferentes") 
archivo1.close()
archivo2.close()
