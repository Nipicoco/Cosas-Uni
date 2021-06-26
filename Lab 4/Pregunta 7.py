'''
Analisis
Entradas: Numero_letra
Salidas: valor_adecuado
proceso: si numetra=1,2,3, 4,5,6,7,8,9,0
Pseudocodigo:
Algoritmo numero
	Escribir "Ingresa un caracter: "
	leer numetra
	
	si numetra = "1"
		Escribir "El caracter ingresado es un numero"
	sino
		si numetra = "2"
			Escribir "El caracter ingresado es un numero"
		SiNo
			si numetra = "3"
				Escribir "El caracter ingresado es un numero"
			SiNo
				si numetra = "4"
					Escribir "El caracter ingresado es un numero"
				SiNo
					si numetra = "5"
						Escribir "El caracter ingresado es un numero"
					SiNo
						si numetra = "6"
							Escribir "El caracter ingresado es un numero"
						SiNo
							si numetra = "7"
								Escribir "El caracter ingresado es un numero"
							SiNo
								si numetra = "8"
									Escribir "El caracter ingresado es un numero"
								sino
									si numetra = "9"
										Escribir "El caracter ingresado es un numero"
									SiNo
										si numetra = "0"
											Escribir "El caracter ingresado es un numero"
										SiNo
											Escribir "El caracter ingresado es una letra"
										FinSi
									FinSi
								FinSi
							FinSi
						FinSi
					FinSi
				FinSi
			FinSi
		FinSi
	FinSi
FinAlgoritmo
'''
numetra = input("Ingrese un valor: ")[:1]
if numetra == "1" or numetra == "2" or numetra == "3" or numetra == "4" or numetra == "5"or numetra == "6" or numetra == "7" or numetra == "8" or numetra == "9" or numetra == "0":
    print("El valor ingresado es un numero")
else:
    print("El valor ingresado es una letra")
input('Presionar enter para terminar')