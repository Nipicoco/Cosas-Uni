numeros = []
pares = 0
impares = 0
c = (x %2)

a = "Para terminar de agregar numeros utilize [-1]"
print("\n" + a + "\n" + "-" * len(a) + "\n")

numero_ingresado = int(input("Ingrese numeros para agregarlos al conjunto: "))
numeros.append(numero_ingresado)
x = numero_ingresado
c = (x %2)
while numero_ingresado != -1 :
    numero_ingresado = int(input("Ingrese numeros para agregarlos al conjunto: "))
    numeros.append(numero_ingresado)
    x = numero_ingresado
    c = (x %2)
    if c == 0:
        pares += 1

    elif c != 0:
        impares += 1

if c == 0:
    pares += 1

elif c != 0:
    impares += 1

print("Los numeros ingresados son: {}\nLa cantidad de numeros pares es: {}\nLa cantidad de numeros impares es: {}".format(numeros, pares, impares))