#Descripcion:Genera una matriz de N x M con números aleatorios entre 100.000 y 5.000.000, donde N representa el numero de sucursales de una compañía (Este numero se debe solicitar por pantalla) y M corresponde a la cantidad de meses que existen durante un año
#Entrada: sucursal,meses
#Salida: total ventas por sucursales, en meses y en total de la compania
from random import randint as q        
n = int(input("Numero de sucursales: "))
m = int(input("Meses: "))
l1 = []
l2 = []
for i in range(n):
    l1.append(0)
for i in range(m):
    l2.append(0)
ma=[[(q(100000,5000000)) for x in l2]for x in l1] 
for e in range(len(ma)):
    for p in range(len(ma[e])):
        print(ma[e][p],end=" ")
    print()     
totalc = 0
totals=[]
sucu = 0
mes = [0]*m
menor = 0      
for i in range(len(ma)):
    for j in range(len(ma[i])):
        totalc+=ma[i][j]
        menor[j]+=ma[i][j]
    totals.append(sum(ma[i]))                                      
print("El total de cada sucursal es: ",totals)      
for i in range(len(totals)):
        totalc += totals[i]
print("El total de ventas de la compania es: {}".format(int(totalc/2)))           
for w in range(len(totals)):
    sucu=totals[0]
    if(totals[w]>sucu):
        sucu=totals[w]
print("la sucursas con mas ventas fue {} con un total de {} ventas".format((w+1), sucu))           
for i in range(len(menor)):
    if(menor[i] < menor[mes]):
        mes = menor[i]
print("Dentro de la lista, el mes que menos vendio fue: {}".format(mes))