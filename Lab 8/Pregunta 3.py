##Descripcion: Realiza una calculadora, para esto deberá solicitar 2 números al usuario y luego preguntarle al usuario cual es la operación que desea realizar
##Entradas: num1, num2
##Salidas: resultado


def sumar(x, y):
    return x + y
def restar(x, y):
    return x - y
def multiplicar(x, y):
    return x * y
def dividir(x, y):
    return x / y


def repeticion():
    opcion = input("Que desea hacer: \n1.Sumar\n2.Restar\n3.Multiplicar\n4.Dividir\n5.Apagar\nIngresar opcion: ")
    if opcion in ('1', '2', '3', '4',):
        num1 = int(input("Ingresar primer numero: "))
        num2 = int(input("Ingresar segundo numero: "))
    if opcion == '1':
        print('=======')
        print(num1, "+", num2, "=", sumar(num1, num2))
        print('=======')
        repeticion()
    elif opcion == '2':
        print('=======')
        print(num1, "-", num2, "=", restar(num1, num2))
        print('=======')
        repeticion()
    elif opcion == '3':
        print('=======')
        print(num1, "*", num2, "=", multiplicar(num1, num2))
        print('=======')
        repeticion()
    elif opcion == '4':
        print('=======')
        print(num1, "/", num2, "=", dividir(num1, num2))
        print('=======')
        repeticion()
    elif opcion == '5':
        print("Adios")
        exit(0)
    else:
        print('Opcion invalida')
        repeticion()
repeticion()