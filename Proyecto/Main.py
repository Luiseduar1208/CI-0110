#Listas de almacenamiento de conteo de palabras
lista1 = []
lista2 = []
lista3 = []
lista4 = []
lista5 = []
lista6 = []
#Solicitud de palabras al usuario
cant_parrafos = 0
print("Para buscar las palabras tenga en cuenta que el programa es sensible a mayúsculas y minúsculas.")
print()
palabra1 = input("Ingrese la primera palabra: ")
palabra2 = input("Ingrese la segunda palabra: ")
palabra3 = input("Ingrese la tercera palabra: ")
palabra4 = input("Ingrese la cuarta palabra: ")
palabra5 = input("Ingrese la quinta palabra: ")
palabra6 = input("Ingrese la sexta palabra: ")

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

#Ordenamiento de los totales y determinacion del mayor para utilizarlo en los graficos
totales.sort(reverse=True)
mayor = totales[0]
