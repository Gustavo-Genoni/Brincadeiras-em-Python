import math
numero = int(input("Informe um valor: "))
if (numero < 2):
    print ("O número não é primo")
elif (numero == 2):
    print ("O número é primo")
else:
    div = numero % 2
    if (div == 0):
        print ("O número não é primo!")
    else:
        n = 3
        r = numero % n
        raiz = math.pow(numero, 1/2)
        while ((r != 0) and (n < raiz)):
            n = n + 2
            r = numero % n
        if (r != 0):
            print ("O valor é primo")
        else:
            print ("O valor informado não é primo")
        
