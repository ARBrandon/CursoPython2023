edad = int(input("Introduce tu edad:"))
p_e = int
if edad < 4:
    p_e =0
elif edad >=4 and edad <= 18:
    p_e = 4
else:
    p_e=10
print("El precio de la entrada es",p_e,"colones")
