"""
tipo_cambio <-- solicitar al usuario el tipo de cambio
importar <-- Modulo
lista_zonas <-- Modulo.zonas()
precios_finales <-- Modulo.precio_final(tipo_cambio)
lista_semestre <-- Modulo.semestres()

suma_I_semestre <-- 0
for i in range(len(lista_semestre)):
    if lista_semestre[i] == "I Semestre":
        suma_I_semestre += precios_finales[i]
print <-- "Suma de valores del I Semestre:", suma_I_semestre

suma_II_semestre <-- 0
for i in range(len(lista_semestre)):
    if lista_semestre[i] == "II Semestre":
        suma_II_semestre += precios_finales[i]
print <-- "Suma de valores del II Semestre:", suma_II_semestre

suma_zona_central <-- 0
for i in range(len(lista_zonas)):
    if lista_zonas[i] == "Zona Central":
        suma_zona_central += precios_finales[i]
print <-- "Suma de valores de la Zona Central:", suma_zona_central

suma_zona_sur <-- 0
for i in range(len(lista_zonas)):
    if lista_zonas[i] == "Zona Sur":
        suma_zona_sur += precios_finales[i]
print <-- "Suma de valores de la Zona Sur:", suma_zona_sur

suma_zona_norte <-- 0
for i in range(len(lista_zonas)):
    if lista_zonas[i] == "Zona Norte":
        suma_zona_norte += precios_finales[i]
print <-- "Suma de valores de la Zona Norte:", suma_zona_norte
"""

tipo_cambio = float(input("Ingrese el tipo de cambio: "))

import Modulo as m
lista_zonas = m.zonas()
precios_finales = m.precio_final(tipo_cambio)
lista_semestre = m.semestres()

suma_I_semestre = 0
for i in range(len(lista_semestre)):
    if lista_semestre[i] == "I Semestre":
        suma_I_semestre += precios_finales[i]

print("Suma de valores del I Semestre:", suma_I_semestre)

suma_II_semestre = 0
for i in range(len(lista_semestre)):
    if lista_semestre[i] == "II Semestre":
        suma_II_semestre += precios_finales[i]

print("Suma de valores del II Semestre:", suma_II_semestre)

suma_zona_central = 0
for i in range(len(lista_zonas)):
    if lista_zonas[i] == "Zona Central":
        suma_zona_central += precios_finales[i]
print("Suma de valores de la Zona Central:", suma_zona_central)

suma_zona_sur = 0
for i in range(len(lista_zonas)):
    if lista_zonas[i] == "Zona Sur":
        suma_zona_sur += precios_finales[i] 
print("Suma de valores de la Zona Sur:", suma_zona_sur)

suma_zona_norte = 0
for i in range(len(lista_zonas)):
    if lista_zonas[i] == "Zona Norte":
        suma_zona_norte += precios_finales[i]
print("Suma de valores de la Zona Norte:", suma_zona_norte)

suma_total = suma_I_semestre + suma_II_semestre + suma_zona_central + suma_zona_sur + suma_zona_norte
print("Suma total de todos los valores:", suma_total)