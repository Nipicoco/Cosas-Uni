'''
Analisis
Entradas:menu, ensalada, bebida
Salidas:precio_final
pseudocodigo:
Algoritmo menus
	definir menu,ensalada,bebida Como Entero
	primera<-1500
	segunda<-2500
	tercera<-5700
	cuarta<-1550
	quinta<-6000
	ensalada1<-800
	ensalada2<-1500
	ensalada3<-1100
	ensalada4<-960
	ensalada5<-770
	bebida1<-800
	bebida2<-900
	bebida3<-1000
	Imprimir '---------'
	Imprimir "El menu de hoy es: "
	Imprimir "1)Pan con carne"
	Imprimir "2)Chorizo aleman con papas"
	Imprimir "3)Carne asada"
	Imprimir "4)Tacos con mole"
	Imprimir "5)Sopa de mono"
	Imprimir '---------'
	Escribir 'Ingresar numero menu: '
	Imprimir '---------'
	leer menu
	si menu=1
		menu<-primera
	SiNo
		si menu=2
			menu<-segunda
		SiNo
			si menu=3
				menu<-tercera
			SiNo
				si menu=4
					menu<-cuarta
				SiNo
					si menu=5
						menu<-quinta
					SiNo
						Escribir 'El elemento seleccionado es incorrecto.'
					FinSi
				FinSi
			FinSi
		FinSi
	FinSi
	Imprimir '---------'
	Imprimir 'Las ensaladas disponibles son:'
	Imprimir '1)Lechuga a la parrila'
	Imprimir '2)Tomates con zanahoria'
	Imprimir '3)Choclo dulce'
	Imprimir '4)Coliflor'
	Imprimir '5)Tomates cherry con pasto'
	Imprimir '---------'
	Escribir 'Ingresar numero ensalada: '
	Imprimir '---------'
	leer ensalada
	si ensalada=1
		ensalada<-ensalada1
	SiNo
		si ensalada=2
			ensalada<-ensalada2
		SiNo
			si ensalada=3
				ensalada<-ensalada3
			SiNo
				si ensalada=4
					ensalada<-ensalada4
				SiNo
					si ensalada=5
						ensalada<-ensalada5
					SiNo
						Escribir 'El elemento seleccionado es incorrecto.'
					FinSi
				FinSi
			FinSi
		FinSi
	FinSi
	Imprimir '---------'
	Imprimir 'Las bebidas disponibles son:'
	Imprimir '1)Coca-cola'
	Imprimir '2)Fanta'
	Imprimir '3)Sprite'
	Imprimir '---------'
	Escribir 'Ingresar numero bebida: '
	Imprimir '---------'
	leer bebida
	si bebida=1
		bebida<-bebida1
	SiNo
		si bebida=2
			bebida<-bebida2
		SiNo
			si bebida=3
				bebida<-bebida3
			FinSi
		FinSi
	FinSi
	Imprimir '---------'
	Imprimir 'El valor de su compra es: $',menu+ensalada+bebida
	Escribir 'Desea pagar o rechazar el pedido: '
	leer pago_compra
	Imprimir '---------'
	Si pago_compra='pagar'
		Imprimir 'Gracias por comprar con nosotros'
		Imprimir '---------'
	SiNo
		si pago_compra='rechazar'
			Imprimir 'Nos vemos pronto'
			Imprimir '---------'
		FinSi
	FinSi
	
FinAlgoritmo

'''
primera=int(1500)#pan con carne
segunda=int(2500)#Chorizo aleman con papas
tercera=int(5700)#Carne asada
cuarta=int(1550)#Tacos con mole
quinta=int(6000)#Sopa de mono
#########
ensalada1=int(800)#Lechuga a la parrila
ensalada2=int(1500)#Tomates con zanahoria
ensalada3=int(1100)#Choclo dulce
ensalada4=int(960)#Coliflor
ensalada5=int(770)#Tomates cherry con pasto
#########
bebida1=int(800)#Coca-cola
bebida2=int(900)#Fanta
bebida3=int(1000)#Sprite

print("El menu de hoy es: \n1)Pan con carne\n2)Chorizo aleman con papas\n3)Carne asada\n4)Tacos con mole\n5)Sopa de mono")
print('===============')	
menu=int(input('Ingresar numero menu: '))
if menu == 1 :
    menu = primera
elif menu == 2 :
    menu = segunda 
elif menu == 3 :
    menu = tercera 
elif menu == 4 :
    menu = cuarta
elif menu == 5:
    menu = quinta
else:
    print("El menu seleccionado no se encuentra en el menu o ingreso un numero erroneo")
    exit(0)
print('===============')
print('Las ensaladas disponibles son: \n1)Lechuga a la parrila\n2)Tomates con zanahoria\n3)Choclo dulce\n4)Coliflor\n5)Tomates cherry con pasto')
print('===============')
ensalada=int(input('Ingresar numero ensalada: '))
if ensalada == 1 :
    ensalada = ensalada1
elif ensalada == 2 :
    ensalada = ensalada2 
elif ensalada == 3 :
    ensalada = ensalada3 
elif ensalada == 4 :
    ensalada = ensalada4
elif ensalada == 5:
    ensalada = ensalada5
else:
    print("El menu seleccionado no se encuentra en el menu o ingreso un numero erroneo")
    exit(0)
print('===============')
print('Las bebidas disponibles son: \n1)Coca-cola\n2)Fanta\n3)Sprite')
print('===============')
bebida=int(input('Ingresar numero bebida: '))
print('===============')
if bebida == 1 :
    bebida = bebida1
elif bebida == 2 :
    bebida = bebida2
elif bebida == 3 :
    bebida = bebida3
else:
    print("El menu seleccionado no se encuentra en el menu o ingreso un numero erroneo")
    exit(0)
print("El valor total de su compra es: $", menu+ensalada+bebida)
confirmar = input("pagar o rechazar compra: ")
if confirmar == "pagar":
    print("Gracias por preferir sabwey")
elif confirmar == "rechazar":
    print("Vuelva pronto")
else:
    print('El valor o palabra ingresado es erroneo.')
input('Presionar enter para terminar')