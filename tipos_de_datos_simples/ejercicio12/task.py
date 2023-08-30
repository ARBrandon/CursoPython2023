pan=float(input("Introduce el número de barras vendidas que no son frescas:"))

desc=0.6
prec=3.49
resul=pan*prec*(1-desc)

print("El coste de una barra fresca es ₡" + str(prec))
print("El descuento sobre una barra no fresca es " + str(desc*100) + "%")
print("El coste final a pagar es ₡" + str(round(resul, 2)))