import random


def generar_numero_aleatorio(minimo, maximo):
    return random.randint(minimo, maximo)

def mostrar_menu():
    print("a.inicar juego\n"
          "b.salir del juego\n")

def main():
    a = input(mostrar_menu())
    minimo = int(input("elija un numero minimo: "))
    maximo = int(input("elija un numero maximo: "))
    gen_num = generar_numero_aleatorio(minimo,maximo)
    guess = False
    while guess == False:
        if a == "a":
            xd = int(input("adivine un numero: "))
            if xd == gen_num:
                print("adivinaste!")
                quit()
            elif xd >= gen_num:
                print("el numero es demasiado alto!")
                t = input("deseas continuar?\n"
                          "si\n"
                          "no\n")
                if t == "no":
                    guess = True
            else:
                print("el numero es demasiado bajo!!")
                t = input("deseas continuar?\n"
                          "si\n"
                          "no\n")
                if t == "no":
                    guess = True
        elif a == "b":
            quit()

if __name__ == "__main__":
    main()
