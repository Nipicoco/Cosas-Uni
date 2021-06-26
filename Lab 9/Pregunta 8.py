#Descripcion: Genera una matriz de 5x5 con números aleatorios, luego fila por medio asignar 0 a los valores, luego mostrar por pantalla
#Entrada: no hay parametros de entrada
#Salida: lista
from random import randint

n1 = randint(0, 100)
n2 = randint(0, 100)
n3 = randint(0, 100)
n4 = randint(0, 100)
n5 = randint(0, 100)
n6 = randint(0, 100)
n7 = randint(0, 100)
n8 = randint(0, 100)
n9 = randint(0, 100)
n10 = randint(0, 100)

lista=[ [0,0,0,0,0], [n1,n2,n3,n4,n5], [0,0,0,0,0], [n6,n7,n8,n9,n10], [0,0,0,0,0] ]#la lista contiene los 0 insertados manualmente
a=lista
for y in range(len(a)):
    for x in range(len(a[y])):
        print(a[y][x],end=("  ")) 
    print() 