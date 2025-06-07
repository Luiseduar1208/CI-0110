"""Ejercicio 13- Actividad 3
texto <-- solicitar al usuario
lista <-- palbras_del_texto
tamaño_lista <--tam_lista()
print <-- Indicar tamaño de lista
indice <-- pedir al usuario
if indice <= tamaño then
    print <-- lista[indice]
else print <-- "Índice invalido"
"""
texto = input("Digite su texto:")
lista = texto.split()
tam = len(lista)
print(f"La lista tiene un tamaño de {tam}")
indice = int(input("Digite el indice deseado:"))
if indice <= tam:
    print(lista[indice - 1])
else:
    print("Digite un numero dentro de los valores")