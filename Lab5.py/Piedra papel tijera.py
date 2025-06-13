#Importar libreria
import random as rn 

#Opcion de la maquina 
opciones = ["Piedra", "Papel", "Tijera"]
Maquina = rn.choice(opciones)

#Opcion de juego
print("Esto es un juego de piedra, papel o tijera. Indique su respuesta con la primera letra en mayuscula:")
Usuario = input()

#Matchear resultados y buscar ganador
if Maquina == Usuario:
    print("Has quedado empate")
else:
    if Maquina == "Tijera":
        if Usuario == "Piedra":
            print("Has Ganado!")
        if Usuario == "Papel":
            print("Perdiste")

    if Maquina == "Piedra":
        if Usuario == "Papel":
            print("Has ganado!")
        if Usuario == "Tijera":
            print("Perdiste")
    if Maquina == "Papel":
        if Usuario == "Tijera":
            print("Has ganado!")
        if Usuario == "Piedra":
            print("Perdiste")
    else: 
        print("Asegurese de haber indicado la respuesta conforme a lo indicado en las instrucciones")
