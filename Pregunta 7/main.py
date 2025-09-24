def calcularIva(valor):
    iva = 1.19
    print("El valor antes de agregar iva es: ", valor)
    valor = valor* iva
    print("El valor después de agregar iva es: ", valor)
    return valor

print(calcularIva(3500))
