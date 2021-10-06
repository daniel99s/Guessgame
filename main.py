import random 
def humanguess():
    number=random.randrange(0,10)
    print (number)

    num =-1

    num=int(input("Ingresa un numero del 1 al 10"))

    while num!=number:
        if number==num:
            print(f"Felicidades ganaste{num}")
            

        elif num>number:
            print(f"el numero que eligio es mayor{num}")

        else:
            print(f"el numero que aligio es menor{num}")

humanguess()
