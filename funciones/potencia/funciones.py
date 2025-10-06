from .multiplicacion.funciones import multiplicar

def potencia(a, b):
    if b == 0:
        return 1
    elif a == 0:
        return 0
    elif b == 1:
        return a
    else:
        pot = a
        for x in range(2, b + 1):
            pot = multiplicar(pot, a)
        return pot
