info = {'nombre': 'none', 'edad': 'none', 'direccion': 'none', 'telefono': 'none'}
info['nombre'] = input("¿Cómo te llamas?")
info['edad'] = input("¿Cuántos años tienes?")
info['direccion'] = input("¿Cuál es tu dirección?")
info['telefono'] = input("¿Cuál es tu número de teléfono?")
print(info['nombre'], 'tiene', info['edad'], 'años, vive en', info['direccion'], 'y su número de teléfono es', info['telefono'])