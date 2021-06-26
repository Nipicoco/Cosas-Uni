'''
Analisis
Entradas: n1,n2,n3
salidas: multip, menor, mayor
proceso: si el primer numero es mayor al segundo, escribirlo y multiplicar el tercer valor ingresado para comparar si el resultado de la multiplicacion de el menor con el tercer valor es mayor al numero mas grande.
Pseudocodigo:
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

'''


numero1=int(input("Ingresar primer numero: "))
numero2=int(input("Ingresar segundo numero: "))
mini=min(numero1,numero2)
mayor=max(numero1,numero2)
if numero1==numero2:
    print("El numero menor es:",mini)
else:
    print('El numero menor es:',mini)
numero3=int(input('Ingresar tercer numero: '))
multip=(numero3*mini)
print("Si mutiplicamos el tercer numero con el menor seria:",multip)
if multip>mayor:
    print('El numero resultado de la multiplicacion es mayor que el numero mas grande de la primera comparacion')
else:
    print('El numero resultado de la multiplicacion es menor que el numero mas grande de la primera comparacion')
input('Enter para salir')