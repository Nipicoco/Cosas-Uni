'''
Analisis
Entrada: numero
Salida: numero<8, numero>12, numero==8
Proceso: if numero<8, elif numero>12, elif numero==8:
Pseudocodigo:
Algoritmo p9
Definir  edad Como Entero
	Escribir "Ingresar su edad"
	Leer edad
	Si edad<8
		Imprimir "Su entrada es gratis"
	Sino
		Si edad>12 
			Escribir "Debe cancelar $1500"
		Sino
			Si edad=8
				Escribir "Debe cancelar $800"
			SiNo
				Si edad>8
					Escribir "Debe cancelar $800"
				FinSi
			FinSi
		FinSi
	FinSi
FinAlgoritmo
'''
#Algoritmo para calcular si la edad es mayor, igual o menor a 8,12
edad=int(input("Ingresar su edad: "))
if edad<6:
    print("Su entrada es gratis, dirigirse a puerta de acceso")
elif edad>=6 and edad>=18:
    print("El valor a pagar es de $3500")
elif edad>18 and edad<55:
    print("Valor a pagar es de $4500")
elif edad>55:
    print("Valor a pagar es de $3000")

input("Presione ENTER para terminar")