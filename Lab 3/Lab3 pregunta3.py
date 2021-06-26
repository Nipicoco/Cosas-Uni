'''
ANALISIS:
Entrada: "letra1"
salida: vocal, novocal
Proceso: Si letra1="a" o letra1="e" o letra1="i" or letra1="o" o letra1="u"
Pseudocodigo:
Algoritmo pregunta3
	Escribir "Escribir letra: "
	leer letra1
	Si letra1 Es "a" o letra1 es "e" o letra1 es "i" o letra1 es "o" o letra1 es "u"
		
		Imprimir "Es una vocal"
	SiNo
	Si letra1 Es "A" o letra1 es "E" o letra1 es "I" o letra1 es "O" o letra1 es "U"
		
		Imprimir "Es una vocal"
SiNo
	Imprimir "No es una vocal"
FinSi
FinSi
FinAlgoritmo
'''

#Algoritmo para calcular si una letra es o no vocal.
letra1 = str(input("Ingresar una letra: "))
print("==========")
if letra1[-1]=="a" or letra1[-1]=="e" or letra1[-1]=="i" or letra1[-1]=="o" or letra1[-1]=="u" :
    print("Esta letra es una vocal")
elif letra1=="A" or letra1=="E" or letra1=="I" or letra1=="O" or letra1=="U":
	 print("Esta letra es una vocal")
else: 
    print("Esta letra no es una vocal")
print("==========")
input("Presiona ENTER para salir.")