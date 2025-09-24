def areaCuadrado(alto, ancho):
    return alto * ancho

def volumenCaja(alto,ancho, largo):
    return areaCuadrado(alto, ancho) * largo

print(volumenCaja(5,5,5))