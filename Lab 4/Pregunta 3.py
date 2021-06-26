'''
Analisis
Entradas: n1
salidas: multip
proceso: si n1%2==0 y n1%7==0 Entonces escribir: escribir 'Es multiplo de 2 y 7', sino escribir: 'NO ES MULTIPLO'
pseudocodigo:
Algoritmo multip
	Definir n1 Como Entero
	Escribir 'Ingresar un numero'
	leer n1
	si n1%2==0 y n1%7==0 Entonces
		Escribir 'Es multiplo de 2 y 7'
	SiNo
		Escribir 'No es multiplo ni de 2, ni de 7'
	FinSi
FinAlgoritmo
'''


numero=int(input('Ingresar un numero: '))
if numero%2==0 and numero%7==0:
    print('El numero es multiplo de 2 y 7')
else:
    print('No es múltiplo de 2 ni de 7')
input('Presionar enter para terminar')