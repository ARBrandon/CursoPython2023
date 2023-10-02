def suma(a, b):
    return a + b


def resta(a, b):
    return a - b


def multiplicacion(a, b):
    return a * b


def division(a, b):
    return a / b


def mostrar_menu():
    print("Menú de opciones")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")


def main():
    opcion = ""
    while opcion != "5":
        mostrar_menu()
        opcion = input("Seleccione una opción:")
        if opcion == "5":
            quit()
        a = int(input("Ingrese el primer número:"))
        b = int(input("Ingrese el segundo número:"))
        if opcion == "1":
            print("Resultado:", suma(a, b))
        elif opcion == "2":
            print("Resultado:", resta(a, b))
        elif opcion == "3":
            print("Resultado:", multiplicacion(a, b))
        elif opcion == "4":
            print("Resultado:", division(a, b))


if __name__ == "__main__":
    main()
