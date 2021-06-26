def pares(n):
    numbers = []
    for i in range (0, int((n+2)/2)):
        numbers.append(2*i)
    return numbers
n=100
print(pares(n))
input('Apretar enter para terminar')