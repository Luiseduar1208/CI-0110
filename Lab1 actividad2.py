"""ALGORITMO
1. menor <-- Pedir al usuario
2. mayor <-- Pedir al usuario
3. numero <-- menor
4. cuantos 2 <-- 0
5. cuantos 3 <-- 0
6. cuantos 5 <-- 0
7. lista 2 <-- []
8. lista 3 <-- []
9. lista 5 <-- []
10. while numero <= mayor
    10.1 if numero MOD 2 = 0
        10.1.1 cuantos 2 <-- cuantos 2 + 1
        10.1.2 lista 2 <-- añadir el numero
    10.2 if numero MOD 3 = 0 
        10.2.1 cuantos 3 <-- cuantos 3 + 1
        10.2.2 lista 3 <-- añdir el numero
    10.3 if numero MOD 5 = 0 
        10.3.1 cuantos 5 <-- cuantos 3 + 1
        10.3.2 lista 5 <-- añdir el numero
    10.4 numero <-- numero + 1 
11. print <-- Cuantos y cuales valores son divisibles por 2
12. print <-- Cuantos y cuales valores son divisibles por 3
13. print <-- Cuantos y cuales valores son divisibles por 5
        """
menor = int(input("Digite el numero menor: "))
mayor = int(input("Digite el numero mayor: "))

cuantos_2, cuantos_3, cuantos_5 = 0, 0, 0
lista_2, lista_3, lista_5 = [], [], []

for numero in range(menor, mayor + 1):
    if numero % 2 == 0:
        cuantos_2 += 1
        lista_2.append(numero)
    if numero % 3 == 0:
        cuantos_3 += 1
        lista_3.append(numero)
    if numero % 5 == 0:
        cuantos_5 += 1
        lista_5.append(numero)
print("Hay", cuantos_2, "Divisibles por 2:", lista_2)
print()
print("Hay", cuantos_3, "Divisibles por 2:", lista_3)
print()
print("Hay", cuantos_5, "Divisibles por 2:", lista_5)