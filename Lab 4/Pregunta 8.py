'''
Analisis
Entradas: aleat1,aleat2,aleat3,aleat4,aleat5
salidas: lista,suma
proceso: generar numeros aleatorios y sumarlos todos.
pseudocodigo:
Algoritmo aleator
	aleat1 <-Aleatorio(10,100)
	aleat2 <-Aleatorio(10,100)
	aleat3 <- Aleatorio(10,100)
	aleat4 <- Aleatorio(10,100)
	aleat5 <- Aleatorio(10,100)
	suma<-(aleat1)+(aleat2)+(aleat3)+(aleat4)+(aleat5)
	Imprimir aleat1,',',aleat2,',',aleat3,',',aleat4,',',aleat5
	Imprimir 'La suma de los valores es ',suma
FinAlgoritmo
'''

from random import randint
alea1=randint(10,100)
alea2=randint(10,100)
alea3=randint(10,100)
alea4=randint(10,100)
alea5=randint(10,100)
lista=alea1,alea2,alea3,alea4,alea5
suma=alea1+alea2+alea3+alea4+alea5

print('Los numeros generados son:',lista)
print('La suma de los valores es:',suma)
input('Enter para terminar')
