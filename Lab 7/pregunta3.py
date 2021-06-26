##descripcion: realiizar una lista, cuyos valores guarden otra lista que tenga los datos de personas la que detalla su nombre, edad y altura, para luego mostrar por
##por pantalla cual es la persona con mas edad, el de menor edad, el de estatura mas alta, estatura mas baja, nombre mas largo y nombre mas corto.
##entrada: no posee parametro de entrada
##salida: datos que se encuentrar en la lista, persona con mas edad, el de menor edad, el de estatura mas alta, estatura mas baja, nombre mas largo y nombre mas corto
alturaA=1.61
edadA=12
nombreA="Nicolas Andres Vergara Antil"
a=[nombreA,edadA,alturaA]

alturaB=1.70
edadB=32
nombreB="Eduardo Viejo Pesado"
b=[nombreB,edadB,alturaB]

alturaC=1.90
edadC=27
nombreC="Andrea Casas Armadas"
c=[nombreC,edadC,alturaC]

alturaD=1.21
edadD=92
nombreD="Armando Casas"
d=[nombreD,edadD,alturaD]

alturaE=1.78
edadE=32
nombreE="Arturo Celig Sanchez"
e=[nombreE,edadE,alturaE]

lista=[a,b,c,d,e]

print("Los datos de de una lista: ",lista)

print(a)
print(b)
print(c)
print(d)
print(e)

print("")
print("la persona mas vieja: ",nombreD,", con una edad de: ",edadD," años\nla persona mas joven es: ",nombreA,", con una edad de: ",edadA," años\n")
print("la persona más alta es: ",nombreC,", con una altura de: ",alturaC)
print("la persona más baja es: ",nombreD,", con una altura de: ",alturaD)
print("la persona con el nombre mas largo es: ",nombreA,", con una longitud de: ",len(nombreA))
print("la persona con el nombre mas corto es: ",nombreD,", con una longitud de: ",len(nombreD))

    
