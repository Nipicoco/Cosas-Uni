'''
Analisis pseint
Entradas: Nombre1, Nombre2
Salidas: ultima1,ultima2,primera1,primera2
si primera1 es igual a primera 2, escribir quer hay coincidencia, si ultima 1 es igual a ultima 2, hay coincidencia, sino escribir que no hay .
pseudocodigo:
Algoritmo p1
	Escribir 'Ingresar primer nombre'
	leer n1
	Escribir 'Ingresar segundo nombre'
	leer n2
	primera1 <- Minusculas(Subcadena(n1,1,1))
	ultima1 <- Minusculas(Subcadena(n1,Longitud(n1)-0,Longitud(n1)-0))
	primera2 <- Minusculas(Subcadena(n2,1,1))
	ultima2 <- Minusculas(Subcadena(n2,Longitud(n2)-0,Longitud(n2)-0))
	
	si primera1==primera2
		Imprimir 'Si hay coincidencia'
	SiNo
		si ultima1==ultima2
			Imprimir 'Si hay coincidencia'
		SiNo
			Imprimir 'No hay coincidencia'
		FinSi
		
	FinSi
	
FinAlgoritmo



'''
#tienes dos nombres, 
nombre1 = input("Ingresa un nombre: ")
nombre2 = input("Ingresa un nombre: ")

primera_letra1 = nombre1[0].lower()
ultima_letra1 = nombre1[-1].lower()
primera_letra2 = nombre2[0].lower()
ultima_letra2 = nombre2[-1].lower()

if primera_letra1 == primera_letra2:
    print("Hay coincidencia")
elif ultima_letra1 == ultima_letra2:
    print("Hay coincidencia")
else:
    print("No hay coincidencia")
input('Enter para salir')