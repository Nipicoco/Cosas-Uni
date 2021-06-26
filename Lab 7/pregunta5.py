##descripcion:el usuario ingresa los datos que desea almacenar, el programa volverá a solicitar palabras a guardar hasta que ingrese el numero "-1", luego mostrar
##por pantalla cuantos números pares posee, cuantos numeros impares posee y cual pertenece a un numero primo.
##entrada: lista de numeros
##salida: mostrar la lista, mostrar los numeros impares, los pares y los primos
lista=[]
def repetir():
    a=int(input("ingrese un numero: "))
    lista.append(a)

    while a!=-1:
        a=int(input("ingrese un numero: "))
        lista.append(a)

    lista.remove(-1)
    print(lista)
repetir()
def impar(inicio,final):
    lista=[]
    for i in range(0, int(final)):
        if (i % 2) != 0:  
            lista.append(1*i)
    return lista
                     
def par(inicio,final):
    numbers = []
    for i in range (0, int((final+2)/2)):
        numbers.append(2*i)
    return numbers

def primos(inicio, final):
    primos=[]
    for n in range(inicio, final+1):
        contador=0
        for i in range(1, n+1):
            if n % i == 0:
                contador +=1
        if contador == 2:
            primos.append(n)
    return primos

inicio=lista[0]
final=lista[-1]

print("los impares de la lista son: ",impar(inicio,final))
print("los pares de la lista son: ",par(inicio,final))
print("los primos de la lista son: ",primos(inicio,final))
