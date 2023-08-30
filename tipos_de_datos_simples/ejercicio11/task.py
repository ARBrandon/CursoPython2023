i=float(input("Introduce la inversión inicial:"))
interes=0.04
b1=i*(1+interes)
print("Balance tras el primer año:",round(b1, 2))
b2=b1*(1+interes)
print("Balance tras el segundo año:",round(b2, 2))
b3=b2*(1+interes)
print("Balance tras el tercer año:",round(b3, 2))