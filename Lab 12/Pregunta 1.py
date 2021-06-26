#Descripcion: Genera una lista con 20 números random y luego ordenarlos utilizando el algoritmo de ordenamiento por selección, mostrar por pantalla los numeros antes y despues de ordenarlos.
#Entrada: no hay parametros de entrada
#Salida: selection sort
from random import randint as r
def S(matriz):
    n=len(matriz)
    for i in range(n):
        min=i

        for j in range(i+1, n):
            if (matriz[j] < matriz[min]):
                min=j
        
        t=matriz[i]
        matriz[i]=matriz[min]
        matriz[min]=t
        
    return matriz
matriz = [r(1,1000) for i in range (20)]
print("La lista antes de aplicar seleccion seria la siguiente:", matriz)
print("la lista despues de aplicar el metodo de selecciom seria:",S(matriz))