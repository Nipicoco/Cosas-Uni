def lista(a):
    numbers = []
    for i in range (0, int((a+1)/1)):
        numbers.append(1*i)
    return numbers
a=1000
n=lista(a)
def multiplicacion(numer):
    producto=1  
    for n in numer:
        producto*=n+1
    return producto
print("la multiplicacion de todos numeros entre 1 a 1000 es: ",multiplicacion(lista(a)))
input('Apretar enter para terminar')