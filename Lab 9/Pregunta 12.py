#Descripcion: Genera una función que recibe como parámetro una matriz y un número entero que no debe ser menor a 0 y no mayor a la cantidad de columnas que posee la matriz,la función debe retornar la suma de la columna indicada con el segundo parámetro. La matriz debe ser de n*m donde n y m se deben solicitar al usuario, la matriz sera rellenada con numero enteros aleatorios entre -10 hasta 10 (-10 y 10 están incluidos). Mostrar por pantalla la suma final y la matriz.
#Entrada: Filas, columnas, fila a sumar
#Salida: suma

from random import randint

filas=(int(input("Ingrese la cantidad de filas: ")))

columnas=(int(input("Ingrese la cantidad de columnas: ")))

numero=(int(input("Ingrese un numero entero mayor a cero y menor a la cantidad de columnas: ")))

while numero <=0 or numero > filas:
    numero=(int(input("Ingrese un numero entero mayor a cero y menor a la cantidad de columnas: ")))

matriz = []
for b in range(0,filas):
        lista = []
        for c in range(0,columnas):
            Rr = randint(-10,10)
            lista.append(Rr)
        matriz.append(lista)

a=matriz 

for y in range(len(a)):
    for x in range(len(a[y])):
        print(a[y][x],end=("  ")) 
    print() 

def suma(matriz, columna):
    suma = 0
    for i in range(len(matriz)):
        fila = list(matriz[i])
        for x in range(len(fila)):
            if x == columna:
                suma += fila[x]
    return suma

print(suma(matriz,numero-1))