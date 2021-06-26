#Descripcion: Eliminar todos los 0 de una lista definida
#Entrada: No posee parametros de entrada
#Salida: Lista sin cero

lista = [0,5,1,0,3,5,4,8,9,0,2,1,0,6,0,0,1,6,8]
while 0 in lista: lista.remove(0)
print("La lista sin el numero cero es la siguiente:",lista)  #[5, 1, 3, 5, 4, 8, 9, 2, 1, 6, 1, 6, 8]