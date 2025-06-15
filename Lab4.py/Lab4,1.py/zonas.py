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