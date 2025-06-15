"""Ejercicio 16- Unica Actividad - ENTREGABLE
conversion <-- Import
semestres <-- Import
Zonas <-- Import
listas <-- Import
Solicitar el tipo de cambio
conversion <-- conversion(tipo_cambio) #Se añade el tipo de cambio como parametro
for i in range del largo de semanas 
    imprimir <-- semestre, zona, importe convertido
"""
#Importe de modulos
import conversion
import zonas
import semestres
import listas 
meses, tiendas, importes, descuentos = listas.listas() 

#Solicitar el tipo de cambio
tipo_cambio = float(input("Indique el tipo de cambio: "))

#Cambio de nombres
sem = semestres.semestres()
zon = zonas.zonas()
conv = conversion.conversion(tipo_cambio) #Se añade el tipo de cambio como parametro 

#Impresion de los valores en orden
for i in range(len(sem)): #len de sem como valor generico para la impresion 
    print(f"Semestre: {sem[i]}, Zona: {zon[i]}, Importe Convertido y desc. aplicado: {float(conv[i]) - (float(conv[i]) * float(descuentos[i]))}") #Se resta el descuento al importe convertido
#Se imprime el resultado final con descuento aplicado
#Fin del programa