'''
Analisis
Entrada: aleat, aleat2, aleat3
Salida: (aleat+aleat2+aleat3)/3
Proceso: def alear, aleat2, aleat3 <-(azar(7)), resultado<- (aleat+aleat2+aleat3)/3
Pseudocodigo:
Algoritmo lab36
	definir aleat,aleat2,aleat3 como real
	
	aleat <- (azar(7))
	aleat2 <- (azar(7))
	aleat3<- (azar(7))

	Escribir aleat
	Escribir aleat2
	Escribir aleat3
	resultado<- (aleat+aleat2+aleat3)/3
	Escribir "El promedio entre estos numeros es:" ,resultado
FinAlgoritmo
'''

#Algoritmo para calcular el promedio entre 3 valores
import random #Importar random
num1 = (random.uniform(0,7))
num2 = (random.uniform(0,7))
num3 = (random.uniform(0,7))

result = (num1+num2+num3)/3 #resultado de la suma de 3 numeros y dividido en 3
print("",num1)
print("",num2)
print("",num3)
print("==========")
print("El promedio entre estos numeros es: ", result) #Mostrar resultado
print("==========")
input("Presiona ENTER para salir.")