#Descripcion: Genera una matriz de N y M (N y M se deben solicitar al usuario) y generar que los bordes tengan 1 y el centro este con 0
#Entrada: filas,columnas
#Salida: matriz
m = []
f = int(input("filas: "))
c = int(input("columnas: "))

for x in range(0,f):
  list = []
  for p in range(0, c):
    list.append(0)
  m.append(list)

for y in range(len(m)): 
    for z in range(len(m[y])):
        if(y==0 or z==0 or z == len(m[y])-1 or y== len(m)-1): 
            m[y][z]=1
    print(m[y],end=" ")
    print()