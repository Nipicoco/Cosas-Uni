'''
Analisis
Entrada:numero1
Salida: "el numero es par,impar, positivo o negativo"
Proceso: if numero1%2==0 and numero1>0, elif numero1%2!=0 and numero1>0, elif numero1%2==0 and numero1<0, elif numero1%2!=0 and numero1<0:
Pseudocodigo:
Algoritmo Numeroparimpar
	Escribir "Ingresar un numero"
	Leer numero1
	Si numero1 Es Divisible Por 2 y numero1 Es Mayor Que 0
		Escribir "El numero es par y positivo"
	Sino 
		Si numero1 es menor que 0 y numero1 Es Divisible Por 2
			Escribir "El numero es par Y negativo"
	FinSi
	Si numero1 es mayor que 0 y numero1 no Es Divisible Por 2
			Escribir "El Numero es impar y positivo"
		SiNo
			Si numero1 Es menor Que 0 y numero1 no Es Divisible Por 2
				Escribir "El numero es impar y negativo"
			FinSi
		FinSi
	FinSi
	Si numero1 es 0 
		Escribir "Este numero no es ni par ni impar, tampoco positivo ni negativo"
	FinSi
FinAlgoritmo
'''
#Algoritmo para calcular si el numero es positivo, negativo, par e impar.
numero1 = int(input("Escribir numero 1: "))
print("==========")
if numero1%2==0 and numero1>0:
    print("el numero es positivo y par")
elif numero1%2!=0 and numero1>0: 
	print("El numero es positivo e impar")
elif numero1%2==0 and numero1<0:
	print("El numero es negativo y par")
elif numero1%2!=0 and numero1<0:
	print("El numero es negativo e impar")
print("==========")
input("Presiona ENTER para salir.")