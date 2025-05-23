"""Ejercicio 13- Actividad 2
ALGORITMO:
1. texto_completo <-- Solicitar al usaurio
2. palabra <-- Solicitar al usuario
3. cuantas <-- funcion_cuantas(palabra)
4. cuantas <-- Print()
"""
texto = input("Digite el texto principal:\n")
palabra = input("indique la palabra por buscar:")
cuantas = texto.count(palabra)
print(f"La palabra {palabra} aparece {cuantas} veces")

