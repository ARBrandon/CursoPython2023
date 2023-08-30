puntuacion = float(input('Introduce tu puntuación:'))
nivel = str
monto = (puntuacion*2400)+2400
if puntuacion == 0.0:
    nivel = 'Inaceptable'
    print('Tu nivel de rendimiento es',nivel)
    print("Te corresponde cobrar",monto,"colones")
elif puntuacion == 0.4:
    nivel = "Aceptable"
    print('Tu nivel de rendimiento es',nivel)
    print("Te corresponde cobrar",monto,"colones")
elif puntuacion >= 0.6:
    nivel = "Meritorio"
    print('Tu nivel de rendimiento es',nivel)
    print("Te corresponde cobrar",monto,"colones")
else:
    print("Esta puntuación no es válida")