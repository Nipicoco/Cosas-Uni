#Descripcion: Genera una función que recibe como parámetro una matriz, la función debe retornar un tupla que en indica la posición de fila y columna donde encuentra el numero mas alto que existe en la matriz. La matriz debe ser de n*m donde n y m se deben solicitar al usuario, la matriz sera rellenada con numero enteros aleatorios entre -10 hasta 10 (-10 y 10 están incluidos). Finalmente mostrar por pantalla la tupla, el valor mas alto y la matriz generada
#Entradas: filas, columnas
#Salidas: numero mayor valor, tupla(coordenadas)
from random import randint
def mayor(matriz):
    mayor=0
    for i in range(len(matriz)):
        for j in range(0,len(matriz[i]),1):
            if(matriz[i][j]>mayor):
                mayor=matriz[i][j]
                tupla=(i,j)
    print("El numero de mayor valor dentro de la matriz es:",mayor,"en la tupla",tupla,".")
    return tupla



filas=int(input("Ingrese la cantidad de filas: "))

columnas=int(input("Ingrese la cantidad de columnas: "))

lista1=[]

lista2=[]

for i in range(filas):
    lista1.append(0)
for i in range(columnas):
    lista2.append(0)

matriz=[     [(randint(-10,10)) for x in lista2]   for x in lista1]
print(matriz)


mayor1=mayor(matriz)
print(mayor1)