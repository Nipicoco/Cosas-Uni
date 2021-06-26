#Descripcion: Genera una matriz de N x M con numeros random(positivos y negativos)
#Entradas: columnas,filas
#Salidas: matriz
from random import randint as r
a = int(input("Columnas: "))
l = int(input("Filas: "))
m = []
print('La matriz sin reemplazar negativos es la siguiente: \n')
for k in range(0,l):
        list = []
        for j in range(0,a):
            rand = r(-100,100)
            list.append(rand)
        m.append(list)
for e in range(len(m)):
    for p in range(len(m[e])):
        print(m[e][p],end=" ")
    print()
for n in range(len(m)):
    for i in range(len(m[n])):
        if m[n][i] <= 0:
            m[n][i] = 0
("")                
print("La matriz reemplazando negativos quedaria: \n")
for e in range(len(m)):
    for p in range(len(m[e])):
        print(m[e][p],end=" ")
    print()

