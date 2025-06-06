"""Ejercicio 15- Actividad 4 ENTREGABLE
ALGORITMO:
1. archivo <-- abrir archivo
2. cuantos <-- 0
3. sumatoria <-- 0
4. menor <-- 0
5. mayor <-- 0

6. while not end of file (eof)
    6.1 numero <-- leer el archivo 
    6.2 cuantos <-- cuantos + 1
    6.3 sumatoria <-- sumatoria + numero
    6.4 if cuantos = 1 then
        6.4.1 menor  = numero
        6.4.2 mayor = numero 
    6.5 else 
        6.5.1 if numero < menor then
            6.5.1.1 menor = numero
        6.5.2 else 
            6.5.2.1 if numero > mayor then
            6.5.2.1 mayor = numero
7. sumatoria/cuantos
8. print <-- Cant num, promedio sumatoria, mayor y menor 
9. archivo <-- cerrar 
"""
#Abrir archivo
archivo = open(r"C:\Users\c5f958\Documents\Ejercicio 15-4 Archivo A.txt")
#Declaraciones
cuantos = 0
sumatoria = 0
menor = 0
mayor = 0

#En orden de que no se acabe el archivo
for numero in archivo:
    #Contador y suma de numeros
    cuantos += 1 
    sumatoria += int(numero)
    if cuantos == 1:
        #Comparador mayor - menor 
        mayor = numero 
        menor = numero 
    else:
        if numero < menor:
            menor = numero 
        else: 
            if numero > mayor:
                mmayor = numero 
promedio = sumatoria/cuantos

#Impresion de valores
print(f"El promedio de los numeros es: {promedio} ")
print(f"La cantidad de numeros es: {cuantos}")
print(f"La sumatoria de los numeros es: {sumatoria}")
print(f"El numero mayor es: {mayor}")
print(f"El numero menor es: {menor}")

archivo.close()
