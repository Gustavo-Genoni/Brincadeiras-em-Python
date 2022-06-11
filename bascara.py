import math


a, b, c = input("Informe o valor de A,B e C respectivamente: ").split()
a = int(a)
b = int(b)
c = int(c)

if (a == 0):
    print ("Não é equação de segundo grau!")
else:
    delta = (b**2) - (4*a*c)
    if delta < 0:
        print ("Não existe raiz!")
    elif delta == 0:
        raiz = -b / (2*a)
        print ("Raiz única: %.2f"%raiz)
    else:
        x1 = (-b + math.sqrt(delta))/(2*a)
        x2 = (-b - math.sqrt(delta))/(2*a)
        print ("X1 = %.2f \nX2 = %.2f"%(x1,x2))