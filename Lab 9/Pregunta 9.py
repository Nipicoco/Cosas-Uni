#Descripcion: Genera una matriz de 5x5 con números aleatorios, luego columna por medio asignar 0 a los valores, finalmente mostrar por pantalla la matriz.
#Entrada: no hay parametros de entrada
#Salida: matriz 5x5
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
n11 = randint(0, 100)
n12 = randint(0, 100)
n13 = randint(0, 100)
n14 = randint(0, 100)
n15 = randint(0, 100)

lista=[ [n1,0,n2,0,n3], [n4,0,n5,0,n6], [n7,0,n8,0,n9], [n10,0,n11,0,n12], [n13,0,n14,0,n15] ]#la lista contiene los 0 insertados manualmente
a=lista
for y in range(len(a)):
    for x in range(len(a[y])):
        print(a[y][x],end=("  ")) 
    print() 