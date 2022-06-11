
n1, n2, n3 = input("Informe 3 numeros inteiros: ").split()
n1 = int(n1)
n2 = int(n2)
n3 = int(n3)


print ("A - Geometria \nB- Ponderada\nC- Harmonica\nD- Aritimédica \n")
op = input("Informe a opção correspondente: ")
if (op == "a") or (op == "A"):
    operacao = pow((n1*n2*n3),1/3)
    print ("A operação resultou em: %.2f"%operacao)
elif (op == "b") or (op == "B"):
    operacao = (n1+2*n2+3*n3)/6
    print ("A operação resultou em: %.2f"%operacao)
elif (op == "c") or (op == "C"):
    operacao = 1/(1/n1+1/n2+1/n3)
    print ("A operação resultou em: %.2f"%operacao)
elif (op == "d") or (op == "D"):
    operacao = (n1+n2+n3)/3
    print ("A operação resultou em: %.2f"%operacao)
else:
    print ("Opção informada incorreta!")
