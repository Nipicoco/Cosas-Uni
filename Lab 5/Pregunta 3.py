from random import randrange
lista = [randrange(1,20) for i in range(10)]
def suma(lista):
    total=sum(lista)
    return total
print('La lista de numeros generados es:',lista)
resultado=suma(lista)
print("el resultado de la suma entre los numeros generados es:",resultado)
input('Apretar enter para terminar')