from model import suma, resta, multiplicacion, division


def sumar_controller(a, b):
    try:
        return suma(a, b)
    except Exception as e:
        return f"Error en la suma: {str(e)}"


def restar_controller(a, b):
    try:
        return resta(a, b)
    except Exception as e:
        return f"Error en la resta: {str(e)}"


def multiplicar_controller(a, b):
    try:
        return multiplicacion(a, b)
    except Exception as e:
        return f"Error en la multiplicación: {str(e)}"


def dividir_controller(a, b):
    try:
        return division(a, b)
    except Exception as e:
        return f"Error en la división: {str(e)}"
