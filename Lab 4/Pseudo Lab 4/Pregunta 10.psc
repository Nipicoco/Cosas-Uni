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
