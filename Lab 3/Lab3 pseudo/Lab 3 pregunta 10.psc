Proceso  p10
	definir numerop, total, boleto_U como entero
	Imprimir "La lista de peliculas de hoy es: "
	Imprimir "1.La perdicion de league of legends"
	Imprimir "2.El rey de las sopaipillas"
	Imprimir "3.Terminando el trabajo de programacion"
	Imprimir "4.Como pasar la carrera sin programar"
	Imprimir "5.Completos: Una historia de amor"
	
	primera<- "1) La perdicion de league of legends"
	segunda<- "2) El rey de las sopaipillas"
	tercera<- "3) Terminando el trabajo de programacion"
	cuarta<- "4) Como pasar la carrera sin programar"
	quinta<- "5) Completos: Una historia de amor"
	
	val_primera<-1500
	val_segunda<-1550
	val_tercera<-2500
	val_cuarta<-4500
	val_quinta<-1400
	
	
	Escribir "Insertar numero de pelicula a comprar: "
	leer numerop
	si numerop=1
		Imprimir  "La pelicula seleccionada es: ",primera, " y el valor de este ticket es de: ", val_primera
		Escribir "Cuantos boletos desea comprar: "
		leer boleto_U
		Imprimir "El valor de los boletos seria: ", boleto_u*val_primera
		Escribir "Desea pagar los boletos para la funcion O desea rechazar la compra: "
		leer respuesta
		Si respuesta="pagar" o respuesta='Pagar'
			Escribir 'Ha comprado ',boleto_u,' Boletos' ". Gracias por preferir CinePark"
		FinSi
		Si respuesta="Rechazar" o respuesta='rechazar'
			Escribir 'Que tenga un buen dia!'
		FinSi
	    FinSi
	si numerop=2
		Imprimir  "La pelicula seleccionada es: ",segunda, " y el valor de este ticket es de: ", val_segunda
		Escribir "Cuantos boletos desea comprar: "
		leer boleto_U
		Imprimir "El valor de los boletos seria: ", boleto_u*val_segunda
		Escribir "Desea pagar los boletos para la funcion O desea rechazar la compra: "
		leer respuesta
		Si respuesta="pagar" o respuesta='Pagar'
			Escribir 'Ha comprado ',boleto_u,' Boletos' ". Gracias por preferir CinePark"
		FinSi
		Si respuesta="Rechazar" o respuesta='rechazar'
			Escribir 'Que tenga un buen dia!'
		FinSi
		FinSi
	si numerop=3
		Imprimir  "La pelicula seleccionada es: ",tercera, " y el valor de este ticket es de: ", val_tercera
		Escribir "Cuantos boletos desea comprar: "
		leer boleto_U
		Imprimir "El valor de los boletos seria: ", boleto_u*val_tercera
		Escribir "Desea pagar los boletos para la funcion O desea rechazar la compra: "
		leer respuesta
		Si respuesta="pagar" o respuesta='Pagar'
			Escribir 'Ha comprado ',boleto_u,' Boletos' ". Gracias por preferir CinePark"
		FinSi
		Si respuesta="Rechazar" o respuesta='rechazar'
			Escribir 'Que tenga un buen dia!'
		FinSi
		FinSi
	si numerop=4
		Imprimir  "La pelicula seleccionada es: ",cuarta, " y el valor de este ticket es de: ", val_cuarta
		Escribir "Cuantos boletos desea comprar: "
		leer boleto_U
		Imprimir "El valor de los boletos seria: ", boleto_u*val_cuarta
		Escribir "Desea pagar los boletos para la funcion O desea rechazar la compra: "
		leer respuesta
		Si respuesta="pagar" o respuesta='Pagar'
			Escribir 'Ha comprado ',boleto_u,' Boletos' ". Gracias por preferir CinePark"
		FinSi
		Si respuesta="Rechazar" o respuesta='rechazar'
			Escribir 'Que tenga un buen dia!'
		FinSi
		FinSi
		
	si numerop=5
		Imprimir  "La pelicula seleccionada es: ",quinta, " y el valor de este ticket es de: ", val_quinta
		Escribir "Cuantos boletos desea comprar: "
		leer boleto_U
		Imprimir "El valor de los boletos seria: ", boleto_u*val_quinta
		Escribir "Desea pagar los boletos para la funcion O desea rechazar la compra: "
		leer respuesta
		Si respuesta="pagar" o respuesta='Pagar'
			Escribir 'Ha comprado ',boleto_u,' Boletos' ". Gracias por preferir CinePark"
		FinSi
		Si respuesta="Rechazar" o respuesta='rechazar'
			Escribir 'Que tenga un buen dia!'
		FinSi
		FinSi
FinAlgoritmo
