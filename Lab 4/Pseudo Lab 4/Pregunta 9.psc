Algoritmo p9
	Escribir 'Ingresar edad: '
	leer edad
	mayor_edad<-18
	si edad>mayor_edad
		Imprimir 'Es mayor de edad por ',edad-mayor_edad,' A�os'
	SiNo
		si edad<mayor_edad
			Imprimir 'Le faltan ',mayor_edad-edad,' A�os para ser mayor de edad'
		SiNo
			si edad=mayor_edad
				Imprimir 'Usted es mayor de edad'
			FinSi
		FinSi
	FinSi
FinAlgoritmo
