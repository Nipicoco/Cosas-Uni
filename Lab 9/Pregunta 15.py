#Descripcion: Genera una función que recibe como parámetro una matriz, la función debe retornar un indice que indica cual es la fila que posee la suma mas alta. La matriz debe ser de n*m donde n y m se deben solicitar al usuario, la matriz sera rellenada con numero enteros aleatorios entre -10 hasta 10 (-10 y 10 están incluidos). Mostrar por pantalla el indice de la fila con suma mas alta y la matriz.
#Entradas: cantidad de filas y columnas.
#Salidas: matriz con los valores ingresados.
from random import randint

filas = int(input("Ingrese la cantidad de filas: "))

columnas = int(input("Ingrese la cantidad de columnas: "))

lista = [[0] * columnas for i in range(filas)]

for i in range (len(lista)):
    x = list(lista[i])
    for j in range(len(x)):
        num1  = randint(-10,10)
        x[j] = num1
    lista[i] = x
for y in range(len(lista)):
    for x in range(len(lista[y])):
      print (lista[y][x], end = (" "))
    print()


def filas(matriz):
    sumaf = []
    suma = 0
    y = 0
    for i in range(len(matriz)):
        fila = list(matriz[i])
        sumaf.append(fila)
    for j in range(len(sumaf)):
        d = sum(sumaf[j])
        if d > suma:
            suma = d
    return suma
print(filas(lista))