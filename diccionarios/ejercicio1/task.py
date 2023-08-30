D = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
divisa = input("Introduce una divisa:")
if divisa == "Euro":
    print(D['Euro'])
elif divisa == "Dollar":
    print(D['Dollar'])
elif divisa == "Yen":
    print(D['Yen'])
else:
    print("La divisa no está.")