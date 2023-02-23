f = open('alumnos2.txt', 'a')
f.write('{}Hola Mundo!'.format('\n'))
f.write('{}Nuevo Hola Mundo!'.format('\n'))
# alumnos = f.read()
# print(alumnos)
# f.seek(0)
# alumnos2 = f.read()
# print(alumnos2)

# alumnos = f.readline()
# print(alumnos)
# for alumno in alumnos:
#     print(alumno, end='')

f.close()
