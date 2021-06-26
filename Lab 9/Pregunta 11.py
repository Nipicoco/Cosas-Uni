import random

filas=(int(input("Ingrese la cantidad de filas: ")))
#Recibir la cantidad de filas
columnas=(int(input("Ingrese la cantidad de columnas: ")))
#Recibir la cantidad de columnas
entero=(int(input("Ingrese un numero entero mayor a cero y menor a la cantidad de filas: ")))
#Recibir el numero entero mayor a cero, menor a la cantidad de filas

while entero <=0 or entero > filas:
    numero=(int(input("Ingrese un numero entero mayor a cero y menor a la cantidad de filas: ")))

matriz = []
for b in range(0,filas):
        lista = []
        for c in range(0,columnas):
            Rr = random.randint(-10,10)
            lista.append(Rr)
        matriz.append(lista)

a=matriz 

for y in range(len(a)):
    for x in range(len(a[y])):
        print(a[y][x],end=("  ")) 
    print() 

def suma(matriz,filas):
    suma=0
    for i in range(len(matriz[filas])):
        suma+=matriz[filas][i]
    return suma

print(suma(matriz,entero-1))