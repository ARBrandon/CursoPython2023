pisos = [{'año': 2000, 'metros': 100, 'habitaciones': 3, 'garaje': True, 'zona': 'A'},
         {'año': 2012, 'metros': 60, 'habitaciones': 2, 'garaje': True, 'zona': 'B'},
         {'año': 1980, 'metros': 120, 'habitaciones': 4, 'garaje': False, 'zona': 'A'},
         {'año': 2005, 'metros': 75, 'habitaciones': 3, 'garaje': True, 'zona': 'B'},
         {'año': 2015, 'metros': 90, 'habitaciones': 2, 'garaje': False, 'zona': 'A'}]


def añadir_precio(piso):
# TODO


def busca_piso(pisos, presupuesto):
    def filtro(piso):
        """
        Esta función debe filtar el diccionario por el presupuesto
        :param piso:
        :return: diccionario filtado
        """
# TODO
    """
    Primero debemos agregar el precio a los pisos y luego filtrar los.
    Finalmente retornar una lista con todos los diccionarios filtrados.
    """
# TODO


print(busca_piso(pisos, 100000))
# resultado esperado
# [
# {'año': 1980, 'metros': 120, 'habitaciones': 4, 'garaje': False, 'zona': 'A', 'precio': 84000.0},
# {'año': 2015, 'metros': 90, 'habitaciones': 2, 'garaje': False, 'zona': 'A', 'precio': 95000.0}
# ]

print(busca_piso(pisos, 900000))
# resultado esperado
# [{'año': 2000, 'metros': 100, 'habitaciones': 3, 'garaje': True, 'zona': 'A', 'precio': 104000.0},
# {'año': 2012, 'metros': 60, 'habitaciones': 2, 'garaje': True, 'zona': 'B', 'precio': 117300.0},
# {'año': 1980, 'metros': 120, 'habitaciones': 4, 'garaje': False, 'zona': 'A', 'precio': 84000.0},
# {'año': 2005, 'metros': 75, 'habitaciones': 3, 'garaje': True, 'zona': 'B', 'precio': 133875.0},
# {'año': 2015, 'metros': 90, 'habitaciones': 2, 'garaje': False, 'zona': 'A', 'precio': 95000.0}
# ]
