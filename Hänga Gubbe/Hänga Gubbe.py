# 1 Gör en förklaring av början av spelat vad det går ut på och hur det funkar. Med hjälp av en print i början av koden.
# 1.1 Gör en input: för att ska spelaren ska kunna gissa på bokstäver
# 1.2 Bara gissa en bokstav i taget

# 2 Slumpa fram ett random ord från av en lista som innehåller ett visst lista
# 2.1 Printa en ord som har exakt samma ord fast utbytte bokstäver med “_”

# 3 Gör ett värde som har ording alfabet = ABCDEFGHIJKLMNOPQRSTUVWXYZ
# 3.1 Fungera med stora och små bokstäver

# 4 Om gissa rätt repitera loppen av loppen göra en while true lopp
# 4.1 Gissa fel minska repitionen

# 5 Om rätt på alla bokstaver från början printa “Rätt”
# 5.1 Om 10 du tar slut på print player “lose”


# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
# Import list:

import os
import time
import sys
import random

alfabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    

# Info command
infoOne = "        Narrator:  Hangman is a guessing game where you have 8 tries to guess a word."
infoTwo = "                   You do this with guessing one letter at a time."
infoThree = "                   There will appear a guessing board:"
infoFour = "                   __ __ __ __ __ Guest letters: "
infoFive = "                   Where you can guesst a letter for example (V) or (v)."
infoSix = "                   There could be two outcome to that."
infoSeven = "                   Ether you get the answerer right "
infoEight = "                   And it would look like this: "
infoNine = "                   V __ __ __ __  Guest letters: V"
infoTen = "                   Or you get it wrong: "
infoElven = "                   __ __ __ __ __ Guest letters: V"
# infoTwelve="


easyList = ["easy","hard","cow","cat","dog","how","story","phone","clock","pen","notes","true"]

mediumList = ["umbrella","exist","calculator","headset","clouds","alarmclock","Running","axe"] 

hardList = ["programming","universe","microphone","awkward","matrix","funny","microwave","deshawo"]

funList = ["Fun fake David Sjöberg (24,1,2021) says: Om man doppar sina bollar i soja kan man känna smaken"]#"Enligt Simon Jendman (24,1,2021) så kan Ludvig Svahla inte vara en man för att han är under 180 cm lång","Sex är haram","Simon är bra på Cs från okändkälla","Simon Jendman är nästan klar med Halv blodsbprincen","Pog du är snygg idag : )"]

print("__________________________________________________________________________________________")
print("\n")


#funtions 

def startMenu ():
    print(
        "__________________________________________________________________________________________")
    print("\n")
    print("  _      __    __                     __         __ __                                 __")
    print(" | | /| / /__ / /______  __ _  ___   / /____    / // /__ ____  ___ ___ _  ___ ____    / /")
    print(" | |/ |/ / -_) / __/ _ \/  ' \/ -_) / __/ _ \  / _  / _ `/ _ \/ _ `/  ' \/ _ `/ _ \  /_/ ")
    print(" |__/|__/\__/_/\__/\___/_/_/_/\__/  \__/\___/ /_//_/\_,_/_//_/\_, /_/_/_/\_,_/_//_/ (_)  ")
    print("                                                             /___/                       ")

    print("\n")
    print("                            Press (1) to start the game")
    print("\n")
    print("                            Press (2) for info about the game")
    print("\n")
    print("                            Press (3) for a fun fact")
    print("\n")
    print("                            Press (4) to close the game")
    print("\n")

    print("__________________________________________________________________________________________")
    print("\n")


def startGame(word): 
    hideWord =["_", " "]*len(word) 
    fail = False 
    guessedLetters = []
    hearts = 0 
    # print (hearts) add the hangman animation online som finns i functioner 
   
    
    while hearts < 6:
        wordList = []
        for x in word:
            wordList.append(x)
            wordList.append(" ")
        if wordList == hideWord:
            print("\n")
            print("You win ")
            exit()
        print (HANGMANPICS[hearts])    
        print ("".join(hideWord))
        print("\n")
        guess = input ("Guess a letter: ").upper()
        if len(guess) == 1 and guess in alfabet and guess not in guessedLetters: 
            if guess in word:
                for x in range (len(word)):
                    if guess == word [x]:
                        hideWord[2*x] = guess 
            else: 
                hearts += 1
                print("\n")
                 
            if hearts == 6:
                print ("You lost ")
                exit()
        else:
            print("\n")
            print ("Already tried this letter")
            continue
        
        
        
    
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

startMenu() 
#def wordRandom

choice = int(input())
if choice == 1:
    print ("                    You can chose between three difficulties! ")
    print ("\n")
    print ("                            Press (1) for Easy mode")
    print ("\n")
    print ("                            Press (2) for Medium mode")
    print ("\n")
    print ("                            Press (3) for Hard mode")
    print ("\n")
    print("__________________________________________________________________________________________")
    print ("\n")
    choice2 =  int(input()) 
    if choice2 == 1: 
        word = (random.choice(easyList))    

    elif choice2 == 2: 
        word = (random.choice(mediumList))    

    elif choice2 == 3: 
        word = (random.choice(hardList))
       
    word = (word.upper())
    print ("\n")  
    startGame(word)
        
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
               
        
    if choice == 2: 
        for char in infoOne:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.03)
        
        print ("\n")

        for char in infoTwo:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.03)
        
        print ("\n")

        for char in infoThree:
            sys.stdout.write(char)
            sys.stdout.flush() 
            time.sleep(0.03)

        print ("\n")

        for char in infoFour:
            sys.stdout.write(char)
            sys.stdout.flush()        
            time.sleep(0.03)
        print ("\n")
        for char in infoFive:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.03)
        print("\n")
        for char in infoSix:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.03)
        print("\n")
        for char in infoSeven:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.03)
        print("\n")
        for char in infoEight:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.03)
        print("\n")
        for char in infoNine:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.03)
        print("\n")
        for char in infoTen:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.03)
        print("\n")
        for char in infoElven:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.03)
        print("\n")
        print ("__________________________________________________________________________________________")    # Lägg till animations på första felet 
    
    if choice == 3:
        fun = (random.choice(funList))
        print("kuk",fun)

#elif choice2 == 2: 
        #word = (random.choice(mediumList)) 

    elif choice == 4:
        print ("\n")
        print ("Good bye : )")
        exit()



    elif choice >= 5:
        print ("\n") 
        startMenu()
        print ("That's not a option!")


    elif choice == 0:
        print ("\n") 
        startMenu()
        print ("That's not a option!")

    
