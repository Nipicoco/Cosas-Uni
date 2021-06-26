# Descripción: crear una funcion la cual cuente cuantas veces se repite el numero 1 en una matriz 
# Entrada: el numero de filas y el numero de columnas 
# Salida: una matriz generada al azar y el numero de veces que aparece el numero 1


from random import randint

filas=(int(input("Ingrese la cantidad de filas: ")))

columnas=(int(input("Ingrese la cantidad de columnas: ")))

matriz = []
contadors=[]
for b in range(0,filas):
        lista = []
        for c in range(0,columnas):
            aA = randint(-10,10)
            lista.append(aA)
        matriz.append(lista)
        c=lista.count(1)
        contadors.append(c)

def count(contador):
    suma=0
    for i in contador:
            suma+=i
    return suma

a=matriz 

for y in range(len(a)):
    for x in range(len(a[y])):
        print(a[y][x],end=("  ")) 
    print() 



print("El numero 1 se repite:",count(contadors),"veces")