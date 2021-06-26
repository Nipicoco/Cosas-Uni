##descripcion: Crear dos parámetros, el primer parámetro es una cadena de caracteres y el segundo parámetro es un solo carácter.
##Su funcion sera devolver "Asi es" si el carácter se encuentra dentro de la cadena y "No se encuentra dentro" en caso que no exista dentro de la cadena.
##entrada: no posee parametros de entrada.
##salida: mostrar por pantalla la cadena, el caracter que se busca y la respuesta si el caracter se encuentra dentro.

cadena="Hola"
print(cadena)
caracter='a'
def encontrar(cadena,caracter):
    true="Asi es"
    false="No se encuentra dentro"
    if cadena[0:1]=='a' or cadena[1:2]=='a' or cadena[2:3]=='a' or cadena[3:4]=='a' or cadena[4:5]=='a' or cadena[5:6]=='a' or cadena[6:7]=='a' or cadena[7:8]=='a' or cadena[8:9]=='a' or cadena[9:10]=='a' or cadena[10:11]=='a':
        return true
    else:
        return false

print("¿el caracter",caracter,"se encuentra en la cadena de saludo?")
print(encontrar(cadena,caracter))



