asignaturas={}
Matematicas = int(input("Ingrese el valor del crédito para Matemáticas"))
Fisica = int(input("Ingrese el valor del crédito para Física"))
Quimica = int(input("Ingrese el valor del crédito para Química"))
asignaturas = {'Matemáticas': Matematicas, 'Física': Fisica, 'Química': Quimica}
creditos = [asignaturas.values()]
print('Matemáticas',"tiene", asignaturas.get('Matemáticas'),"créditos")
print('Física',"tiene", asignaturas.get('Física'),"créditos")
print('Química',"tiene", asignaturas.get('Química'),"créditos")
print("Número total de créditos del curso:",Matematicas+Fisica+Quimica)