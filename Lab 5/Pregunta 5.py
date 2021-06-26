def multiplos(n):
    numbers = []
    for i in range (0, int((n+3)/3)):
        numbers.append(3*i)
    return numbers
n=150
print(multiplos(n))
input('Apretar enter para terminar')