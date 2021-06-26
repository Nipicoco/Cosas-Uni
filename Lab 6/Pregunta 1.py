## Descripcion: lee la lista y la entrega de forma invertida
## Entradas: lista
## Salidas: reverso(lista)

lista=[1,"pizza",2,"pan",3,"choripan",4,"espinilla",5,"pelo"]

def reverso (lista):
    if lista==[]:
        reves=lista
    else:
        reves=[lista[-1]]+reverso(lista[:-1])
    return reves

print("La lista es:",lista)
print("La lista invertida es:",reverso(lista))