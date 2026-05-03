from model import suma, resta, multiplicacion, division

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
            print(f"Resultado: {a} + {b} = {suma(a, b)}")
        elif opcion == "2":
            print(f"Resultado: {a} - {b} = {resta(a, b)}")
        elif opcion == "3":
            print(f"Resultado: {a} × {b} = {multiplicacion(a, b)}")
        elif opcion == "4":
            try:
                print(f"Resultado: {a} ÷ {b} = {division(a, b)}")
            except ValueError as e:
                print(f"Error: {e}")

if __name__ == "__main__":
    main()
