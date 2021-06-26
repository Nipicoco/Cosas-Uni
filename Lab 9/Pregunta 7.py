#Descripcion: Calcular y mostrar por pantalla la suma de todos los números una matriz 10 x 10 generada con números enteros aleatorios.
#Entrada: no existen parametros de entrada.
#Salida: matriz 10x10
from random import randint
n1 = [randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100)]
n2 = [randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100)]
n3 = [randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100)]
n4 = [randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100)]
n5 = [randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100)]
n6 = [randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100)]
n7 = [randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100)]
n8 = [randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100)]
n9 = [randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100)]
n10 = [randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100)]

matriz = [n1,n2,n3,n4,n5,n6,n7,n8,n9,n10]
print("La matriz seria: \n")
for y in range(len(matriz)):
    for x in range(len(matriz[y])):
        print(matriz[y][x],end=("  "))
    print()


s1 = (sum(n1))
s2 = (sum(n2))
s3 = (sum(n3))
s4 = (sum(n4))
s5 = (sum(n5))
s6 = (sum(n6))
s7 = (sum(n7))
s8 = (sum(n8))
s9 = (sum(n9))
s10 = (sum(n10))


total = (s1 + s2 + s3 + s4 + s5 + s6 + s7 + s8 + s9 + s10)

print("\nLa suma de todos los numeros presentes en la matriz seria: ",total)