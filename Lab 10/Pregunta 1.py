#Descripcion: Generar una lista del 1 hasta el 100000, solicitar un valor y mostrar por pantalla en que posicion de la lista se encuentra este.
#Entrada: numero a encontrar
#Salida: posicion del numero en la lista
from random import randint
numeros=[]
for x in range(0, 10000):
    n=randint(1,100001)
    numeros.append(n)
numero=int(input("Ingrese el numero que desea buscar: "))
r = 0
if numero in numeros:
    while numeros[r] != numero:
        r += 1
        if numeros[r] == numero:
            print("en la lista, el numero {} se encuentra en la posicion {}".format(numero, (r+1)))
else: 
    print("El numero no se encuentra dentro de la lista")