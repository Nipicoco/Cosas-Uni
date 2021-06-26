Algoritmo Lab3
	Escribir 'Insertar primer numero'
	Leer n1
	Escribir '=============='
	Escribir 'Insertar segundo numero'
	Leer n2
	Escribir '=============='
	Escribir 'Insertar tercer numero'
	Leer n3
	Escribir '=============='
	Si n1>n2 Y n1>n3 Entonces
		Escribir 'El numero mas grande es:',n1
	FinSi
	Si n3>n1 Y n3>n2 Entonces
		Escribir 'El numero mas grande es:',n3
	FinSi
	Si n2>n1 Y n2>n3 Entonces
		Escribir 'El numero mas grande es:',n2
	FinSi
	Escribir '=============='
	Si n1=n2 Entonces
		Escribir 'El numero 1 y 2 son iguales'
	FinSi
	Si n2=n3 Entonces
		Escribir 'El numero 2 y 3 son iguales'
	FinSi
	Si n1=n3 Entonces
		Escribir 'El numero 1 y 3 son iguales'
	FinSi
	Si n1=n2 Y n2=n3 Entonces
		Escribir 'Todos los numeros son iguales'
	FinSi
FinAlgoritmo
