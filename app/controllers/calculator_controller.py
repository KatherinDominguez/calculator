from model import suma, resta, multiplicacion, division


def validar_numeros(a, b):
    """
    Valida que ambos valores sean números.

    Args:
        a (int | float): Primer valor.
        b (int | float): Segundo valor.

    Raises:
        ValueError: Si alguno de los valores no es numérico.
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Ambos valores deben ser números")


def sumar_controller(a, b):
    """
    Controlador para sumar dos números.
    """
    try:
        validar_numeros(a, b)
        return suma(a, b)
    except Exception as e:
        return f"Error en la suma: {str(e)}"


def restar_controller(a, b):
    """
    Controlador para restar dos números.
    """
    try:
        validar_numeros(a, b)
        return resta(a, b)
    except Exception as e:
        return f"Error en la resta: {str(e)}"


def multiplicar_controller(a, b):
    """
    Controlador para multiplicar dos números.
    """
    try:
        validar_numeros(a, b)
        return multiplicacion(a, b)
    except Exception as e:
        return f"Error en la multiplicación: {str(e)}"


def dividir_controller(a, b):
    """
    Controlador para dividir dos números.
    """
    try:
        validar_numeros(a, b)
        return division(a, b)
    except Exception as e:
        return f"Error en la división: {str(e)}"
