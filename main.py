import random
def humanGuess ():
    number = random.randrange(0,10)
    print(number)
    op = -1
    while(number != op):
        op = int(input("Introduce un numero: "))
        if (number == op):
            print("Felicidades ganaste, el numero era {}".format(number))
        else:
            if(number > op): 
                print("Te falto")
            else:
                print("Te pasaste")

def computerGuess():
    NumMenor=0
    NumMayor=1000
    number = random.randrange(NumMenor,NumMayor) 
    bandera = False 
    
    while(bandera == False):
        print (number)
        print("Este es tu numero?")
        opc= input("Si | No:  ").lower()
        if( opc == "no"):
            print("Tu numero es mayor o menor al mio?")
            opc2 = input("Mayor | Menor: ").lower()
            if (opc2 == "menor"): 
                NumMayor=number
                Num= random.randrange(NumMenor,NumMayor)
                number=Num
            else: 
                  NumMenor=number
                  Num = random.randrange(NumMenor,NumMayor)
                  number=Num
        else:
            bandera = True

    
computerGuess()