"""
Analisis
Variables entrada: Numero1, numero2, numero3
Variables salida: numero1_mayor, numero2_mayor, numero3_mayor
Proceso: Si n1>n2 Y n1>n3 Entonces, Si n3>n1 Y n3>n2 Entonces, Si n2>n1 Y n2>n3 Entonces, Si n1=n2 Entonces, Si n2=n3 Entonces, Si n1=n2 Y n2=n3 Entonces
Pseudocodigo: 
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
	Si n1<n2 Y n1<n3 Entonces
		Escribir 'El numero menor es:',n1
	FinSi
	Si n3<n1 Y n3<n2 Entonces
		Escribir 'El numero menor es:',n3
	FinSi
	Si n2<n1 Y n2<n3 Entonces
		Escribir 'El numero menor es:',n2
	FinSi
	Si n1=n3 y n1=n2 Entonces
		Escribir 'Los numeros son iguales.'
	FinSi
FinAlgoritmo
"""

#Algoritmo para calcular si los numeros difieren en tamaño
numero1 = int(input('Introducir primer numero: '))
numero2 = int(input('Introducir segundo numero: '))
numero3 = int(input('Introducir tercer numero: '))
if numero1<=numero2 and numero1<=numero3: 
  print("El numero mas pequeño es: ",numero1)
elif numero2<=numero1 and numero2<=numero3:
  print("El numero mas pequeño es: ",numero2)
else:
    print("El numero mas pequeño es: ",numero3)
input('Apretar cualquier tecla')