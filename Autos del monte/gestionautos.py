def colores(lista):
    for color in lista:

        resultado = []

        for color in lista:
            if color not in resultado:
                resultado.append(color)

    return resultado
    
def autos_faltantes(otro_concesionario, lista_autos):
    resultado = []
    for auto in otro_concesionario:
        if auto not in lista_autos:
            resultado.append(auto)

    return resultado

def closure():
    def suma(a, b):
        return a + b
    return suma
print(closure())