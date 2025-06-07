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