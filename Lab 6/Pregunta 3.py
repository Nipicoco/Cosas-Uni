## Descripcion: Juntar dos cadenas de caracteres e imprimir
## Entradas: A,B
## Salidas: joint(A,B)

a = ["Usted tiene 20 horas para vivir"," deme todos sus mangas"]
b = [","]
def joint(a,b):
    caracteres = a[0]+b[0]+a[1]
    return caracteres
frase = joint(a,b)

print(frase)





