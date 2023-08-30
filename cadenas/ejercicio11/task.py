pro=input("Introduce el nombre del producto:")
pre=float(input("Introduce el precio unitario:"))
uni=int(input("Introduce el número de unidades:"))
print("{pro}: {uni:1d} unidades x {pre:1.2f} = {total:1.2f}".format(pro=pro, uni=uni, pre=pre, total=uni*pre))