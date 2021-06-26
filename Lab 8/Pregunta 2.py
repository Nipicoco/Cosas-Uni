##Descripcion: Realizar una funcion que calcule el m.c.d entre dos numeros y otra que calcule el m.c.m entre dos numeros, los sume y muestre si es numero primo o no
##Entradas: numero1, numero2, numero1a, numero2a
##salidas: primo, mcm, mcd
titulo = "Calculadora MCM"
print("=" * len(titulo) + "\n" + titulo + "\n" + "=" * len(titulo))

numero1=int(input("Ingresar numero: "))
numero2=int(input("Ingresar segundo numero: "))
def mcm(a,b):
    z = max(a,a)

    while True:
        if (z % a == 0) and (z % b == 0):
            return z
            
        z += 1
print("El mcm de sus numeros es: ",mcm(numero1,numero2))
#
#
titulo = "Calculadora MCD"
print("=" * len(titulo) + "\n" + titulo + "\n" + "=" * len(titulo))

numero1a=int(input("Ingresar numero: "))
numero2a=int(input("Ingresar segundo numero: "))
def mcd(a,b):
    a = max(a, b)
    b = min(a, b)
    while b!=0:
        mcd = b
        b = a%b
        a = mcd
    return mcd
print("El mcd de sus numeros es:",mcd(numero1a,numero2a))
#
#
def prim(c):
    if c<2:
        return "Si"
    for i in range(2,c):
        if c%i==0:
            return "No"
        return "Si"
#
#
titulo = "Calculadora MCM + MCD"
print("=" * len(titulo) + "\n" + titulo + "\n" + "=" * len(titulo))

c= mcm(numero1,numero2)+mcd(numero1a,numero2a)
print("La suma de ",mcm(numero1,numero2),"+",mcd(numero1a,numero2a),"es:", c,)
print('Es',c,"Primo o no?")
print(prim(c))