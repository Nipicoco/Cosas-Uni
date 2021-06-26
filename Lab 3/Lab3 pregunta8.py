'''
Analisis
Entradas: palabra1, palabra2
Salidas: (len(palabra1))>(len(palabra2)) 
Proceso: if (len(palabra1))>(len(palabra2)) :
Pseudocodigo:
Algoritmo palabra
	Escribir "Ingresar primera palabra: "
	Leer palabra1
	Escribir "Inatgesar segunda palabra: "
	Leer palabra2
	
	Si Longitud(palabra1)>Longitud(palabra2)
		Imprimir "La palabra de mayor longitud es: ", palabra1
	SiNo
		Imprimir "La palabra de mayor longitud es: ", palabra2
	FinSi
FinAlgoritmo
'''



palabra1=(input("Ingresar primera palabra: "))
palabra2=(input("Ingresar segunda palabra: "))
if (len(palabra1))>(len(palabra2)) :
    print ("La palabra de mayor longitud es:", palabra1)
elif(len(palabra1))==(len(palabra2)):
      print("Favor ingresar palabras de distinta longitud")
else:
    print ("La palabra de mayor longitud es:", palabra2)
print("==========")
input("Presionar enter para terminar")
