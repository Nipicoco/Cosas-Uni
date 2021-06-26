## Descripcion: Une los dominios y los nombres en orden aleatorio
## Entradas: nombre, dominio
## Salidas: juntar(nombre,dominio)

from random import randint
nombre=["Nicolas","Andres","Ricardo","Exequiel","Catalina"]
dominio=["@goqoez.com","@gmail.com","@outlook.cl","@educa.uct","@adretail.cl","@grange.cl","@outlook.com","@hotmail.cl","@yopmail.cr","@alu.uct.cl"]

def juntar(nombre,dominio):
    a=nombre[(randint(0,4))]
    b=dominio[randint(0,9)]
    correo=a+b
    texto="".join(correo)
    return texto
a=juntar(nombre,dominio)
b=juntar(nombre,dominio)
c=juntar(nombre,dominio)
d=juntar(nombre,dominio)
e=juntar(nombre,dominio)
lista=[a,b,c,d,e]
print(lista)

