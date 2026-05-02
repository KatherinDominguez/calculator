def suma(a, b):
    """
    Devuelve la suma de dos números (a + b).
    """
    return a + b

def resta(a, b):
    """
    Devuelve la resta de dos números (a - b).
    """
    return a - b

def multiplicacion(a, b):
    """
    Devuelve la multiplicación de dos números (a * b).
    """
    return a * b

def division(a, b):
    """
    Devuelve la división de dos números (a / b).
    """
    if b == 0:
        raise ValueError("No se puede dividir entre cero")
    return a / b
