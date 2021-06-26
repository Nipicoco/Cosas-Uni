##Descripcion: Escribir una funcion que reciba un natural y devuelva su factorial.
##Entradas: numero
##Salidas: factorial
print("==========")
numero=int(input("Ingresar un numero: "))
print("==========")

while numero==0:
    numero=int(input("Ingresar un numero distinto de cero: "))
####
def factorial(n):
    producto=1
    for i in range(1, n + 1):
        producto *=i

    return producto
print("El factorial del numero ingresado es:",factorial(numero))
print("==========")
