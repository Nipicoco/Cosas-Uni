#Descripcion:Genere una matriz de N x M donde N es el numero de estudiantes que existen en el curso de Programación I (N se debe solicitar al usuario) y M es el numero de tareas que se han realizado durante el año (M se debe solicitar al usuario).
#Entrada: estudiantes, tareas
#Salida: cantidad repro, apro y media
from random import uniform as u
ap = 0
re = 0
matriz = []
pro = []
e = int(input("Ingresar numero de estudiantes en la clase:"))
t = int(input("Ingresar numero de tareas: "))
for x in range(0,e):
  list = []
  for y in range(0, t):
    aleatorio = u(1.0,7.0)
    list.append(aleatorio)
  matriz.append(list)
  print (list)
for z in range(0, e):
    Suma = 0
    p = []
    for b in range(0, t):
        Suma += matriz[z][b]
    Promedio = Suma/t
    if Promedio >= 4.0:
        ap += 1
    elif Promedio < 4.0:
         re += 1
    print ("El promedio del alumno", (z+1), "es:", Promedio)
def m(lista):
    mitad = len(lista) // 2
    lista.sort()
    if not len(lista) % 2:
        return (lista[mitad - 1] + lista[mitad]) / 2.0
    return lista[mitad]
print ("La cantidad de alumnos aprobados es:", ap)
print ("La cantidad de alumnos reprobados es:", re)
print ("La mitad de estos promedios seria: ", m(list))