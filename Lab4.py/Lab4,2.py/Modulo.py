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

"""
listas <-- import(meses, tiendas, importes, descuentos)
lista_semestres <-- []
for mes in meses:
    if mes = enero, febrero, marzo, abril, mayo, junio then 
        mes <-- I Semestre in lista semestre 
    else
        mes <-- II Semestre in lista semestre
"""
def semestres():
    import listas 
    meses, tiendas, importes, descuentos = listas.listas()
    lista_semestre = []
    for mes in meses:
        if mes in ["ENERO", "FEBRERO", "MARZO", "ABRIL", "MAYO", "JUNIO"]:
            lista_semestre.append("I Semestre")
        else:
            lista_semestre.append("II Semestre")
    return lista_semestre

""" 
listas <-- import(meses, tiendas, importes, descuentos)
conversiones <-- []
tipo de cambio usuario <-- parametro 
para cada importe en importes:
    valor <-- importe(en valor numero decimal) * tipo de cambio 
    devuelve valor 
"""
def conversion(tipo_cambio):
    import listas
    meses, tiendas, importes, descuentos = listas.listas()
    conversiones = []
    for importe in importes:
        valor = float(importe) * tipo_cambio
        conversiones.append(valor)
    return conversiones

"""
listas <-- import(meses, tiendas, importes, descuentos)
meses, tiendas, importes, descuentos = listas.listas()
precio_final(tipo_cambio)
precios_finales = []
por el largo de importees:
    valor importe <-- float(importes[i]) * tipo_cambio
    valor descuento <-- float(descuentos[i])
    precio_final <-- valor importe - (valor importe * valor descuento / 100)
    precios_finales.append(precio_final)
"""
def precio_final(tipo_cambio):
    import listas
    meses, tiendas, importes, descuentos = listas.listas()
    precios_finales = []
    for i in range(len(importes)):
        valor_importe = float(importes[i]) * tipo_cambio
        valor_descuento = float(descuentos[i])
        precio_final = valor_importe - (valor_importe * valor_descuento / 100)
        precios_finales.append(precio_final)
    return precios_finales

"""
listas <-- import(meses, tiendas, importes, descuentos)
lista_zonas <-- []
for tienda in tiendas:
    if tienda = 1,2,3,4:
        tienda <-- añadir a lista_zonas as "Zona Central"
    elif tienda = 5,6:
        tienda <-- añadir a lista_zonas as "Zona Sur"
    else:
        tienda <-- añadir a lista_zonas as "Zona Norte"
lista_zonas <-- return 
"""
def zonas():
    import listas
    meses, tiendas, importes, descuentos = listas.listas()
    lista_zonas = []
    for tienda in tiendas:
        if tienda in ["1", "2", "3", "4"]:
            lista_zonas.append("Zona Central")
        elif tienda in ["5", "6"]:
            lista_zonas.append("Zona Sur")
        else:
            lista_zonas.append("Zona Norte")
    return lista_zonas
