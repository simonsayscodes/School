import random 
z = random.randint(1,10)

for x in range(5): 
    Write = int(input())

    if Write == z: 
        print(" Win ") 
        break
    elif Write > z:
        print(" Guess lower :) ")
    elif Write < z: 
        print("Guess higher :) ")

#Skriv en lopp för Write. 
