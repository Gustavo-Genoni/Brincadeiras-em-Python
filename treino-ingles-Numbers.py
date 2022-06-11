
from doctest import testfile
from random import randint
score = 0
while (True):
    numero = randint(1,20)
    escrita = ['','one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen','twenty']
    print ("%d"%numero)
    resposta = (input("Informe a escrita do numero: "))
    if escrita[numero] == resposta:
        score = score + 1
        print ("Resposta correta! \n ")
        

        game = randint(0,10)
        if (game >= 5):
            numero = randint(1,20)
            print("%s"%escrita[numero])
            resposta = int(input("Informe o numero corresposndente: "))
            if (resposta == numero):
                score = score + 1
                print ("Você acertou! \n")
                
            else:
                print ("Você errou!")
                print ("Score total: %d"%score)
                break

    else:
        print ("Você errou!")
        print ("Score total: %d"%score)
        break
    
