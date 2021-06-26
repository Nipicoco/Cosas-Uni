##descripcion: el usuario ingresa los datos que desea almacenar, el programa volverá a solicitar palabras a guardar hasta que ingrese la palabra guardar, luego
##se pide confirmar si desea terminar de guardarlos datos, si confirma el programa solicitara crear una contraseña y luego ingresarla nuevamente, si no son iguales,
##coincidan y si el usuario no desea guardar el programa volvera a solicitar palabras para almacenarlas hasta que nuevamente ingrese la palabra guardar y se repita
##entrada: lista, confirmacion, contraseña, confirmar contraseña
##salida: lista, confirmacion
lista=[]
def repetir():
    a=input("ingrese nueva palabra: ")
    str(a).lower()
    lista.append(a)

    while a!="guardar":
        a=input("ingrese nueva palabra: ")
        str(a).lower()
        lista.append(a)

    lista.remove("guardar")
    print(lista)
repetir()

def confirmar():
    print("¿Desea guardar la palabra")
    print("Confirmar con SI")
    print("Negar con NO")
    confirmar=input("Ingresar la opcion: ")
    str(confirmar).lower()

    if confirmar=="SI":
        c1=input("cree una nueva contraseña: ")
        c2=input("ingrese su contraseña: ")
        str(c1).lower()
        str(c2).lower()
        while c1!=c2:
            c2=input("ingrese su contraseña: ")
        print("lista almacenada con exito")
    if confirmar=="NO":
        repetir()
        confirmar()
confirmar()
