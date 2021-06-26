#Descripcion: Generar una lista del 1 hasta el 100000, solicitar un valor y mostrar por pantalla en que posicion de la lista se encuentra este, Usando el metodo binario y usando sort.
#Entrada: Numero a encontrar
#Salida: Numero dentro de la lista(posicion)
from random import randint
temp=(randint(0,10))
print ("la temperatura es:",temp)
if temp<=2 or temp>6:
    print("high")
else:
    print("low")