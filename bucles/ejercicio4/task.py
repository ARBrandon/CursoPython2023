inversion = int(input('¿Cantidad a invertir?'))
interes = int(input('¿Interés porcentual anual?'))
Años = int(input('¿Años?'))

for i in range(1, Años+1):
    inversion *= 1+interes/100
    print("Capital tras {} años: {}".format(i,round(inversion,2)))

