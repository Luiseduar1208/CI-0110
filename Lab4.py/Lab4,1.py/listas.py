"""    
archivo <-- abrir el archivo 
leer y descartar primera linea
meses = []
tiendas = []
importes = []
descuentos = []
while eof:
    leer linea
    split text <-- index
    meses <-- index0
    tiendas <-- index1
    importes <-- index2
    descuentos <-- index3
"""
def listas():
    with open(r"C:\Users\luied\Documents\Ejercicio 16-1.txt") as archivo:
        archivo.readline()

        meses = []
        tiendas = []
        importes = []
        descuentos = []

        for linea in archivo:
            index = linea.strip().split()
            meses.append(index[0])
            tiendas.append(index[1])
            importes.append(index[2])
            descuentos.append(index[3])
    return meses, tiendas, importes, descuentos 


