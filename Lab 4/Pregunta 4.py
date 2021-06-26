'''
Analisis
Entradas: lado1,lado2.lado3
Salidas: si se puede, no se puede
pseudocodigo:
Algoritmo p4
	Escribir 'Ingresar lado 1: '
	leer lado1
	Escribir 'Ingresar lado 2: ' 
	leer lado2
	Escribir 'Ingresar lado 3: '
	leer lado3
	lado1s<-lado1+lado2
	lado2s<-lado1+lado3
	lado3s<-lado2+lado3
	
si lado1s>lado3
	Escribir 'Si se puede'
SiNo
	si lado1s<lado3
		Escribir ('No se puede')
	SiNo
		si lado2s>lado2
			Escribir ('si se puede')
		SiNo
			si lado2s<lado2
				Escribir ('No se puede')
			SiNo
				si lado3s>lado1
					Escribir ('si se puede')
				SiNo
					si lado3s<lado1
						Escribir ('No se puede')
					FinSi
				FinSi
			FinSi
		FinSi
	FinSi
FinSi

FinAlgoritmo
'''



lado1=float(input('Ingresar lado 1: '))
lado2=float(input('Ingresar lado 2: '))
lado3=float(input('Ingresar lado 3: '))

lado1s=lado1+lado2
lado2s=lado1+lado3
lado3s=lado2+lado3

if lado1s>lado3:
    print('si se puede')
elif lado1s<lado3:
    print('No se puede')
elif lado2s>lado2:
     print('Si se puede')
elif lado2s<lado2:
     print('No se puede')
elif lado3s>lado1:
    print('Si se puede')
elif lado3s<lado1:
    print('No se puede')
input('Presionar enter para terminar')