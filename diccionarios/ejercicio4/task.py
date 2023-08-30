meses = {
    "enero": 1,
    "febrero": 2,
    "marzo": 3,
    "abril": 4,
    "mayo": 5,
    "junio": 6,
    "julio": 7,
    "agosto": 8,
    "septiembre": 9,
    "octubre": 10,
    "noviembre": 11,
    "diciembre": 12
}
fecha = input("Introduce una fecha en formato dd/mm/aaaa:")
fecha_list = fecha.split('/')
mes = fecha_list[1]
for clave, valor in meses.items():
    if valor == int(mes):
        nombre_mes = clave
print(fecha_list[0], "de", nombre_mes, "de", fecha_list[2])
