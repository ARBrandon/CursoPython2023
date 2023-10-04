def celsius_a_fahrenheit(celsius):
    return celsius*(9/5)+32


def kilometros_a_millas(kilometros):
    return kilometros/1.609344


def litros_a_galones(litros):
    return litros*0.264172


def mostrar_menu():
    print("Seleccione una opción:\n"
            "1.celsius a fahrenheit\n"
            "2.kilometros a litros\n"
            "3.liros a galones\n")



def main():
    opcion = ""
    while opcion <= "4":
        opcion = input(mostrar_menu())
        match opcion:
            case "1":
                celsius = int(input("cual es la temperatura en celsius: "))
                print("resultado:", celsius_a_fahrenheit(celsius))
            case "2":
                kilometros = int(input("cual es la distancia en kilometros: "))
                print("resultado:", kilometros_a_millas(kilometros))
            case "3":
                litros = int(input("cual es la cantidad en litros: "))
                print("resultado:", litros_a_galones(litros))
            case "4":
                quit()

if __name__ == "__main__":
    main()
