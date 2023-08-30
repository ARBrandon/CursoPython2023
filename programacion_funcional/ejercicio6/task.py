def grade(score):
    '''
    Función que devuelve la calificación correspondiente a una nota.
    Parámetros:
        score: Es un valor real entre 0 y 10.
    Devuelve:
        La calificación correspondiente a la nota score.

        Si es calificación es menor a 5 devuelve ´NR´ de nota reprobada
        Si es calificación es menor a 7 devuelve ´NA´ de nota aprobada
        Si es calificación es menor a 9 devuelve ´ND´ de nota destacada
        Si es calificación es menor a 10 devuelve ´NE´ de nota superior
        Cualquier otra calificación devuelve ´NM´ de nota maxima
    '''
# TODO


def apply_grade(scores):
    '''
    Función que recibe un diccionario de asignaturas y notas y devuelve otro con las asignaturas en mayúsculas y las calificaciones correspondientes a las notas.
    Parámetros:
        scores: Es un diccionario con pares asignatura:nota donde nota es un valor real entre 0 y 10.
    Devuelve
        Un diccionario con pares ASIGNATURA:calificación, donde calificación es la calificación correspondiente a la nota de la asignatura.
    '''
# TODO


print(apply_grade(
    {'Matemáticas': 6.5, 'Física': 5, 'Química': 3.4, 'Economía': 8.2, 'Historia': 9.7, 'Programación': 10}))
# resultado esperado {'MATEMÁTICAS': 'NA', 'FÍSICA': 'NA', 'QUÍMICA': 'NR', 'ECONOMÍA': 'ND', 'HISTORIA': 'NE', 'PROGRAMACIÓN': 'NM'}


print(apply_grade(
    {'Matemáticas': 8, 'Física': 5, 'Química': 2.4, 'Economía': 9.2, 'Historia': 9.7, 'Programación': 10}))
# resultado esperado {'MATEMÁTICAS': 'ND', 'FÍSICA': 'NA', 'QUÍMICA': 'NR', 'ECONOMÍA': 'NE', 'HISTORIA': 'NE', 'PROGRAMACIÓN': 'NM'}
