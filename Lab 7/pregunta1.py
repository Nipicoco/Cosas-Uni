##descripion: mostrar por pantalla los primeros 15 numeros de la sucesion de fibonacci
##entrada: no posee parametro de entrada
##salida: muestra por pantalla la secuencia de fibonacci (primeros 15 numeros)
def fibonacci(n):
    a=0
    b=1
    for i in range(n):
        c=a+b
        a=b
        b=c
    return b

for numero in range(15):
    print(fibonacci(numero))
