'''
Analisis: 
Entrada: Año1
Salidas: Bisiesto, No_bisiesto
Proceso: if ano1%4==0, elif ano1%100==0, elif ano1%400!=0.
Pseudocodigo:
Algoritmo años
	Escribir 'Ingresar año'
	Leer año
	Si año es divisible por 4 y año no Es Divisible Por 100
		Escribir 'Es bisiesto'
	SiNo
			Si año Es Divisible Por 400
				Imprimir "Es bisiesto"
			SiNo
				Imprimir "No es bisiesto"
			FinSi
		Finsi
FinAlgoritmo
'''
#Algoritmo para calcular si el año es bisiesto o no, disculpe profe por las def pero no tengo ñ por la distri americana
ano1 =int(input("Ingresar un año: "))
print("==========")
if ano1%4==0 and ano1%100!=0:
    print("el año", ano1,"es bisiesto")
elif ano1%100==0:
    print("el año", ano1, "no es bisiesto")
elif ano1%400==0:
    print("el año", ano1, "es bisiesto")
else:
    print("el año", ano1, "no es bisiesto")
print("==========")
input('apretar cualquier tecla para terminar')
