gunner =  str(input())
Emma = str(input())
gunner = gunner.split(" ")
Emma =  Emma.split(" ")
gunnerdice =(int(gunner[0]) + int(gunner[1]))/2 + (int(gunner[2]) + int(gunner[3]))/2
Emmadice = (int(Emma[0]) + int(Emma[1]))/2 + (int (Emma[2]) +int(Emma[3]))/2
if gunnerdice == Emmadice:
    print ("tie")
elif gunnerdice > Emmadice:
    print ("Gunner wins")
elif Emmadice > gunnerdice:
    print ("Emma wins")
