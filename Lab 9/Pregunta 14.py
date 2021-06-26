#Descripcion: Genera una función que recibe como parámetro una matriz, la función debe retornar un indice que indica cual es la columna que posee la suma mas alta. La matriz debe ser de n*m donde n y m se deben solicitar al usuario, la matriz sera rellenada con numero enteros aleatorios entre -10 hasta 10 (-10 y 10 están incluidos). Mostrar por pantalla el indice de la columna con suma mas alta y la matriz.
#Entrada: cantidad de filas, columnas
#Salida: la lista con las sumas de cada columna, la matriz y el indice mas alto de las columnas
from random import randint
lista=[]
list=[]

def columnasum(matriz):
    indice=0
    lista=matriz[0]
    for i in range(1,len(matriz)):
        for j in range(0,len(matriz[i]),1):
            lista[j]+=matriz[i][j]

    for i in range(len(lista)):
        if(lista[i]>lista[indice]):
            indice=i
    return indice

filas=int(input("Ingrese la cantidad de filas: "))

columnas=int(input("Ingrese la cantidad de columnas: "))



for i in range(filas):
    lista.append(0)
for i in range(columnas):
    list.append(0)
                                            
matriz=[     [(randint(-10,10)) for x in list]   for x in lista]
print(matriz)


suma1=columnasum(matriz)
print("La columna ubicada en el indice",suma1,"contiene la suma mas alta")