import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), 'app', 'view'))
sys.path.append(os.path.join(os.path.dirname(__file__), 'app', 'controllers'))

from calculator_controller import (
    sumar_controller,
    restar_controller,
    multiplicar_controller,
    dividir_controller
)

def mostrar_menu():
    print("\n===== Calculadora =====")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")
    print("=======================")

def pedir_numeros():
    a = float(input("Ingresa el primer número: "))
    b = float(input("Ingresa el segundo número: "))
    return a, b

def main():
    while True:
        mostrar_menu()
        opcion = input("Elige una opción (1-5): ").strip()

        if opcion == "5":
            print("¡Hasta luego!")
            break

        if opcion not in ("1", "2", "3", "4"):
            print("Opción no válida. Intenta de nuevo.")
            continue

        a, b = pedir_numeros()

        if opcion == "1":
            print(f"Resultado: {a} + {b} = {sumar_controller(a, b)}")
        elif opcion == "2":
            print(f"Resultado: {a} - {b} = {restar_controller(a, b)}")
        elif opcion == "3":
            print(f"Resultado: {a} × {b} = {multiplicar_controller(a, b)}")
        elif opcion == "4":
            print(f"Resultado: {a} ÷ {b} = {dividir_controller(a, b)}")

if __name__ == "__main__":
    main()