'''
Analisis
Entrada: nombre1, nombre2
salida: nombre_mayor, diferencia_longitud
proceso: escribir la longitud del nombre mas largo y la cantidad de caracteres que difieren.
Pseudocodigo:
Algoritmo p10
	Escribir 'Ingresar primer nombre'
	leer n1
	Escribir 'Ingresar segundo nombre'
	leer n2
	l1<-Longitud(n1)-Longitud(n2)
	l2<-Longitud(n2)-Longitud(n1)
	
	Si Longitud(n1)>Longitud(n2) Entonces
		Imprimir 'El nombre de mayor longitud es ',n1,' y la diferencia de caracteres es de: ',l1
	SiNo
		Si Longitud(n2)>Longitud(n1) Entonces
			Imprimir 'El nombre de mayor longitud es ',n2,' y la diferencia de caracteres es de: ',l2
		SiNo
			si Longitud(n1)=Longitud(n2)
				Imprimir 'Los nombres son de igual Longitud'
			FinSi
		FinSi
	FinSi
	
FinAlgoritmo

'''


nombre1=input('Ingresar primer nombre: ')
nombre2=input('Ingresar segundo nombre: ')

if len(nombre1)==len(nombre2):
    print('Los nombres son de igual longitud') 
elif len(nombre1)>len(nombre2):
    print('El nombre de mayor longitud es:',nombre1,"y la diferencia de caracteres es de:",len(nombre1)-len(nombre2))
else:
    print('El nombre de mayor longitud es:',nombre2,"y la diferencia de caracteres es de:",len(nombre2)-len(nombre1))
input('ENTER para terminar')