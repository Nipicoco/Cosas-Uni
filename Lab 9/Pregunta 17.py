#Descripcion: Genera una función que recibe como parámetro una matriz, la función debe retornar un tupla que en indica la posición de fila y columna donde encuentra el numero mas bajo que existe en la matriz. La matriz debe ser de n*m donde n y m se deben solicitar al usuario, la matriz sera rellenada con numero enteros aleatorios entre -10 hasta 10 (-10 y 10 están incluidos). Finalmente mostrar por pantalla la tupla, el valor mas bajo y la matriz generada
#Entrada: filas, columnas
#Salida: numero menor dentro de la matriz
from random import randint
filas=(int(input("Ingrese la cantidad de filas: ")))
columnas=(int(input("Ingrese la cantidad de columnas: ")))

matriz = []
menore=[]
for b in range(0,filas):
        lista = []
        for c in range(0,columnas):
            Rr = randint(-10,10)
            lista.append(Rr)
            menore.append(Rr)
        matriz.append(lista)
a=matriz 

for y in range(len(a)):
    for x in range(len(a[y])):
        print(a[y][x],end=("  ")) 
    print()
    
def menor(valor):
    menor=valor[10]
    for i in range(1,len(valor)):
        if valor[i]<menor:
            menor=valor[i]
    return menor

e=menor(menore)
print("El numero menor dentro de la matriz es:",e)
for y in range(len(a)):
    for x in range(len(a[y])):
        if a[y][x]==e:
            print("El numero",e,"se encuentra en la fila",[y+1],",columna",[x+1])
            print("tupla",[y+1],[x+1])