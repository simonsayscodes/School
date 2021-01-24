#1 Randomisera tal 
import random 

randomTal = int(random.random()*10+1)
#2 Ta in en gissning 
Gissning = int(input("Gissning:"))
#3 Gemför gissningar med random tal
if randomTal == Gissning: 
    print("Winner pog you")
else: 
    print("Du förlorade kinda cring")
#3.1 Om rätt svar spelaren vinner 
#3.2 Om inte rätt forsätt x antal gånger tills inte mer då förlora 
