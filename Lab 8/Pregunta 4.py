##Descripcion: Encontrar el numero generado aleatoriamente entre 1 y 100, lanzando errores si es mayor o menor
##Entrada: numero generado
##Salida: resultado, dependiente de lo que se defina en el programa.(No posee parametros definidos de salida)
from random import randint
 
def juego():
   numero_secreto = randint(1, 100)
   adivinar = int(input("Encontrar el numero entre 1 y 100:"))
   adivinadas = 1
   while numero_secreto != adivinar:
      if adivinar > numero_secreto:
         adivinar = int(input("Adivina un numero menor: "))
      elif adivinar < numero_secreto:
         adivinar = int(input("Adivina un numero mayor: "))
      adivinadas += 1
      if adivinar==numero_secreto:
          return "Yay! ganaste en",adivinadas, "turnos!"


print(juego())