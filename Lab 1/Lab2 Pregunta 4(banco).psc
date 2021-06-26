
Algoritmo ganancias
	definir monto como entero
	
	monto_año1<-monto*12
	monto_int1<-(monto*12)*0.014
	total1<-monto_año1+monto_int1
	
	monto_año2<-(monto*24)
	monto_int2<-(monto*24)*0.028
	total2<-monto_año2+monto_int2
	
	monto_año3<-(monto*36)
	monto_int3<-(monto*36)*0.0312
	total3<-monto_año3+monto_int3
	
	monto_total<-(monto_año1+monto_año2+monto_año3)+(monto_int1+monto_int2+monto_int3)
	
	
	Escribir "Ingrese monto a depositar"
	
	Escribir "---------------"
	
	Leer monto
	
	monto_año1<-monto*12
	
	Escribir "---------------"
	
	Imprimir "El monto ahorrado el primer año sin intereses seria: ", monto_año1
	
	monto_int1<-(monto*12)*0.014
	
	Escribir "---------------"
	
	Imprimir "La ganancia de intereses seria: ", REDON(monto_int1*100)/100;
	
	Escribir "---------------"
	total1<-monto_año1+monto_int1
	
	Imprimir "El monto ahorrado en 1 año con intereses seria de: ", REDON(total1*100)/100;
	
	monto_año2<-(monto*24)
	
	Escribir "---------------"
	
	Imprimir "Monto ahorrado a 2 años sin intereses seria: ", monto_año2
	
	Escribir "---------------"
	
	monto_int2<-(monto*24)*0.028
	
	Imprimir "La ganancia de intereses seria: ", REDON(monto_int2*100)/100;
	
	Escribir "---------------"
	total2<-monto_año2+monto_int2

	Imprimir "El monto ahorrado a 2 años con intereses seria de: ", REDON(total2*100)/100;
	
	Escribir "---------------"
	monto_año3<-(monto*36)
	
	Imprimir "Monto ahorrado a 3 años sin intereses seria:", monto_año3
	
	Escribir "---------------"
	
	monto_int3<-(monto*36)*0.0312
	
	Imprimir "La ganancia de intereses seria: ", REDON(monto_int3*100)/100;
	
	Escribir "---------------"
	total3<-monto_año3+monto_int3
	Imprimir "El monto ahorrado a 3 años con intereses seria de: ", REDON(total3*100)/100;
	
	Escribir "---------------"
	monto_total<-(monto_año1+monto_año2+monto_año3)+(monto_int1+monto_int2+monto_int3)
	Imprimir "El total de dinero ahorrado es: ",(monto_total)
	
	Escribir "==============================================================="
	
	Imprimir "El monto de las ganancias de intereses en tres años es: ", (monto_int1+monto_int2+monto_int3)
FinAlgoritmo