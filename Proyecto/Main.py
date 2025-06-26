#Listas de almacenamiento de conteo de palabras
lista1 = []
lista2 = []
lista3 = []
lista4 = []
lista5 = []
lista6 = []
#Solicitud de palabras al usuario

import string

cant_parrafos = 0
print("Para buscar las palabras tenga en cuenta que el programa es sensible a mayúsculas y minúsculas. \n")
palabra1 = input("Ingrese la primera palabra: ").strip().strip(string.punctuation)
palabra2 = input("Ingrese la segunda palabra: ").strip().strip(string.punctuation)
palabra3 = input("Ingrese la tercera palabra: ").strip().strip(string.punctuation)
palabra4 = input("Ingrese la cuarta palabra: ").strip().strip(string.punctuation)
palabra5 = input("Ingrese la quinta palabra: ").strip().strip(string.punctuation)
palabra6 = input("Ingrese la sexta palabra: ").strip().strip(string.punctuation)

with open(r"C:\Users\luied\Documents\TextoCompleto.txt") as archivo: #Apertura del archivo

    for linea in archivo: #Recorrido del archivo parrafo por parrafo

        palabras = linea.strip().split() #Division de parrafos en lista de palabras

        # Conteo de palabras en cada parrafo y almacenamiento en listas
        cuantas1 = palabras.count(palabra1)
        lista1.append(cuantas1)

        cuantas2 = palabras.count(palabra2)
        lista2.append(cuantas2)

        cuantas3 = palabras.count(palabra3)
        lista3.append(cuantas3)

        cuantas4 = palabras.count(palabra4)
        lista4.append(cuantas4)

        cuantas5 = palabras.count(palabra5)
        lista5.append(cuantas5)

        cuantas6 = palabras.count(palabra6)
        lista6.append(cuantas6)

        cant_parrafos += 1

#Suma de las palabras encontradas en cada lista
totalp1 = sum(lista1)
totalp2 = sum(lista2)
totalp3 = sum(lista3)
totalp4 = sum(lista4)
totalp5 = sum(lista5)
totalp6 = sum(lista6)

totales = [totalp1, totalp2, totalp3, totalp4, totalp5, totalp6]

#Determinacion del mayor de cada lista
mayor_lista1 = max(lista1)
mayor_lista2 = max(lista2)
mayor_lista3 = max(lista3)
mayor_lista4 = max(lista4)
mayor_lista5 = max(lista5)
mayor_lista6 = max(lista6)

menor_lista1 = min(lista1)
menor_lista2 = min(lista2)
menor_lista3 = min(lista3)
menor_lista4 = min(lista4)
menor_lista5 = min(lista5)
menor_lista6 = min(lista6)

#Ordenamiento de los totales y determinacion del mayor para utilizarlo en los graficos
totales.sort(reverse=True)
mayor = totales[0]

#Realizacion de gráficas
#Importar numpy para los graficos
import matplotlib.pyplot as plt
import numpy as np
 
#Font del titulo general 
font1 = {'family': 'serif', 'color': 'gray', 'fontsize': 'x-large', 'fontweight': 'bold'}

#Mostrar los graficos
x = np.array(list(range(1,cant_parrafos+1)))
y = np.array(lista1)
ax1 = plt.subplot(2,3,1)
plt.title(palabra1, color= 'b')
plt.plot(x,y,'b')

x = np.array(list(range(1,cant_parrafos+1)))
y = np.array(lista2)
plt.subplot(2,3,2, sharey= ax1)
plt.title(palabra2, color= 'r')
plt.plot(x,y,'r')

x = np.array(list(range(1,cant_parrafos+1)))
y = np.array(lista3)
plt.subplot(2,3,3, sharey= ax1)
plt.title(palabra3, color= 'y')
plt.plot(x,y,'y')

x = np.array(list(range(1,cant_parrafos+1)))
y = np.array(lista4)
plt.subplot(2,3,4, sharey= ax1)
plt.title(palabra4, color= 'g')
plt.plot(x,y,'g')

x = np.array(list(range(1,cant_parrafos+1)))
y = np.array(lista5)
plt.subplot(2,3,5, sharey= ax1)
plt.title(palabra5, color= 'c')
plt.plot(x,y,'c')

x = np.array(list(range(1,cant_parrafos+1)))
y = np.array(lista6)
plt.subplot(2,3,6, sharey= ax1)
plt.title(palabra6, color= 'm')
plt.plot(x,y,'m')

# plt.tight_layout()
plt.suptitle("Ocurrencias de palabras por parrafo", fontdict = font1)
plt.show()


decision_usuario = input("Si desea descargar los resultados en un archivo de texto indique S o s: \n").lower()

from statistics import mean, median, mode

if decision_usuario == 's':
    with open(r"C:\Users\luied\Documents\Estadisticas.txt", "w") as resultados:
        resultados.write(f"""ESTADISTICAS DE PALABRAS
Palabra 1: {palabra1}
Total de ocurrencias: {totalp1}
MAXIMA cantidad de ocurrencias: {mayor_lista1}
MININMA cantidad de ocurrencias: {menor_lista1}
Media de ocurrencias: {mean(lista1)}
Mediana de ocurrencias: {median(lista1)}
 Modo de ocurrencias: {mode(lista1)}

Palabra 2: {palabra2}
Total de ocurrencias: {totalp2}
MAXIMA cantidad de ocurrencias: {mayor_lista2}
MININMA cantidad de ocurrencias: {menor_lista2}
Media de ocurrencias: {mean(lista2)}
Mediana de ocurrencias: {median(lista2)}
Modo de ocurrencias: {mode(lista2)}

Palabra 3: {palabra3}
Total de ocurrencias: {totalp3}
MAXIMA cantidad de ocurrencias: {mayor_lista3}
MININMA cantidad de ocurrencias: {menor_lista3}
Media de ocurrencias: {mean(lista3)}
Mediana de ocurrencias: {median(lista3)}
Modo de ocurrencias: {mode(lista3)}

Palabra 4: {palabra4}
Total de ocurrencias: {totalp4}
MAXIMA cantidad de ocurrencias: {mayor_lista4}
MININMA cantidad de ocurrencias: {menor_lista4}
Media de ocurrencias: {mean(lista4)}
Mediana de ocurrencias: {median(lista4)}
Modo de ocurrencias: {mode(lista4)}

Palabra 5: {palabra5}
Total de ocurrencias: {totalp5}
MAXIMA cantidad de ocurrencias: {mayor_lista5}
MININMA cantidad de ocurrencias: {menor_lista5}
Media de ocurrencias: {mean(lista5)}
Mediana de ocurrencias: {median(lista5)}
Modo de ocurrencias: {mode(lista5)}

Palabra 6: {palabra6}
Total de ocurrencias: {totalp6}
MAXIMA cantidad de ocurrencias: {mayor_lista6}
MININMA cantidad de ocurrencias: {menor_lista6}
Media de ocurrencias: {mean(lista6)}
Mediana de ocurrencias: {median(lista6)}
Modo de ocurrencias: {mode(lista6)}
""")
    print("Los resultados fueron guardados exitosamente en 'Estadisticas.txt'.")
else:
    print("No se guardaron los resultados en un archivo de texto.")