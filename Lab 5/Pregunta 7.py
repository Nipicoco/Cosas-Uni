def primos(inicial, final):
    primos=[]
    for n in range(inicial, final+1):
        contador=0
        for i in range(1, n+1):
            if n % i == 0:
                contador +=1
        if contador == 2:
            primos.append(n)
    return primos
a=1
b=100
print(primos(a,b))
input('Apretar enter para terminar')