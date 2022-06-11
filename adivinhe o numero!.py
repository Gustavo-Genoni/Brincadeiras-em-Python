import random

from numpy import number
x = random.randint(1,100)

numer = 0
limiteSup = 100
limiteInf = 1
while (numer != x):
    numer = int(input("Iforme um valor para adivinhar: "))
    if (numer == x):
        print ("Você acertou o número!")
    else:
        if (numer > x):
            limiteSup = numer -1
            print ("O valor está entre %d e %d"%(limiteInf,limiteSup))
        else:
            limiteInf = numer + 1
            print ("O valor está entre %d e %d"%(limiteInf,limiteSup))
