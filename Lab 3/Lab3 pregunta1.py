'''
Analisis
Entrada:n1,n2
salida: 'El numero mas grande es: ',n1 o n2
Proceso: if numero1>numero2, else, elif
pseudocodigo:
Algoritmo Lab3
	Escribir '=============='
	Escribir 'Insertar primer numero: '
	Leer n1
	Escribir '=============='
	Escribir 'Insertar segundo numero: '
	Leer n2
	Escribir '=============='
	Si n1>n2 Entonces
		Escribir 'El numero mas grande es: ',n1
	FinSi
	Si n2>n1 Entonces
		Escribir 'El numero mas grande es: ',n2
	FinSi
	Si n1=n2 Entonces
		Escribir 'Los numeros son iguales.'
	FinSi
	Escribir '=============='
FinAlgoritmo
'''
#Algoritmo para calcular si el numero es mayor al otro, o son iguales.
numero1 = int(input("Escribir numero 1: "))
print("==========")
numero2 = int(input("Escribir numero 2: "))
print("==========")
if numero1>numero2 : 
    print ("El numero mayor es: ",numero1)
elif numero2>numero1:
   print ("El numero mayor es: ",numero2)
elif numero1==numero2 :
    print ("Los numeros son iguales")
print("==========")
input("Presiona ENTER para salir.")