#Descripcion: Crea una matriz de 6 x 5 usando listas de comprensión (todo en una sola linea), finalmente mostrar por pantalla la matriz.
#Entradano hay parametros de entrada
#Salida: matriz 6x5
lista=[[n1*1 for n1 in range(5)], [n2*1 for n2 in range(5)], [n3*1 for n3 in range(5)], [n4*1 for n4 in range(5)], [n5*1 for n5 in range(5)], [n6*1 for n6 in range(5)]]
a=lista
for y in range(len(a)):
    for x in range(len(a[y])):
        print(a[y][x],end=("  ")) 
    print() 