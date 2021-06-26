'''
Analisis
Entradas: edad
salidas: edad_mayor 
proceso: si edad>mayor entonces 'es mayor de edad' por edad-mayor años, sino si edad<mayor entonces 'es menor de edad' por mayor-edad años
Pseudocodigo: 
Algoritmo p9
	Escribir 'Ingresar edad: '
	leer edad
	mayor_edad<-18
	si edad>mayor_edad
		Imprimir 'Es mayor de edad por ',edad-mayor_edad,' Años'
	SiNo
		si edad<mayor_edad
			Imprimir 'Le faltan ',mayor_edad-edad,' Años para ser mayor de edad'
		SiNo
			si edad=mayor_edad
				Imprimir 'Usted es mayor de edad'
			FinSi
		FinSi
	FinSi
FinAlgoritmo

'''
edad=int(input('Ingresar edad: '))
mayor=18

if edad>mayor:
    print('Usted es mayor de edad por',edad-mayor,"Años")
elif edad==mayor:
    print('Usted es mayor de edad')
else:
    print('Le faltan',mayor-edad,"años para ser mayor de edad")
input('Enter para terminar')