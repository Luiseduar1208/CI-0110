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