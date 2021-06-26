#Descripcion: Muestra por pantalla los números de la lista, los números a mostrar son desde el tercer número (índice 2) hasta el octavo número (índice 7) sin usar range().
#Entrada: No posee parametros de entrada
#Salida: indice de la lista

lista = [0,5,1,0,3,5,4,8,9,0,2,1,0,6,0,0,1,6,8]

counter=0
for i in lista:
    if(counter>=2 and counter<=7):
        print(lista[counter])
    counter+=1 