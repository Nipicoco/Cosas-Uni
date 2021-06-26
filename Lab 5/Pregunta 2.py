def nmenor(a,b,c):
    if a==b and b<c: return a
    if c==b and b<a: return b
    if a==c and c<b: return c
    if a<b and (b<=c or b>c): return a
    if a>b and (a<=c or a>c): return b
    if a>c and (a<=b or a>b): return c
    
a=int(input("ingrese primer numero: "))
b=int(input("ingrese segundo numero: "))
c=int(input("ingrese tercer numero: "))    
resultado=nmenor(a,b,c)
print("el numero menor es: ",resultado)
input('Apretar enter para terminar')