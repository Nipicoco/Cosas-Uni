Algoritmo p6
definir n1, n2 Como Entero
	Escribir 'Ingresar primer numero'
	leer n1
	Escribir 'Ingresar segundo numero'
	leer n2
	si n1>n2
		Escribir 'El numero menor es ',n2
		Escribir 'Ingresar tercer numero: '
		leer n3
		multip<-(n3*n2)
		Escribir 'La multiplicacion del numero 3 con el menor numero es ' multip
		si multip>n1 Entonces
			escribir 'El numero resultado de la multiplicacion es mayor que el numero mas grande de la primera comparacion'
		SiNo
			Escribir 'El numero resultado de la multiplicacion es menor que el numero mas grande de la primera comparacion'
		FinSi
	FinSi
	si n2>n1
		Escribir 'El numero menor es ',n1
		Escribir 'Ingresar tercer numero: '
		leer n3
		multip<-(n3*n1)
		Escribir 'La multiplicacion del numero 3 con el menor numero es ' multip
		si multip>n2 Entonces
			escribir 'El numero resultado de la multiplicacion es mayor que el numero mas grande de la primera comparacion'
		SiNo
			Escribir 'El numero resultado de la multiplicacion es menor que el numero mas grande de la primera comparacion'
		FinSi
	FinSi
	
FinAlgoritmo
