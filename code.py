
#WARNING! program is currently not fully functional

import time as t
import random as r
import string as s

censorgage = []
percens = []

def wronganswer():
    global percens
    if percens == True:
        print('you have chosen an option outside of the inputs parameters')
        percens = False
        censorchoice()
    else:
        print("you have chosen an option outside of the games parameters you neet")
        print(percens)
    
def censorchoice():
    global censorgage
    global precens
    censor = input("do you wish to play the censored version of the game (removes common harsh language aswell as potentionally vulgar phrases i.e 'neet' ")
    if censor == "yes":
        censorgage = True
        print("you are playing the censored version of the game")
    elif censor == "no":
        censorgage = False
        print("you are playing the uncensored version of the game")
    else:
        precens = True
        wronganswer()
        print(precens)
        
censorchoice()
        

name = input("\nenter your name here ")
lost = input("are you lost or not? ")

heshe = r.randint(0,1)

string = "(you typed something other than yes or no you neet)"
if censorgage == True:
    censor = string.replace("neet", "half-baked muffin")
else:
    censor = string

if heshe == 1:
    heshe = "he"
elif heshe == 0:
    heshe = "she"

if lost == "yes":
    lost = "he is lost!"
elif lost == "no":
    lost = "luckily he is not lost as the south side of chicago is a very dangerous place "
elif lost != "no" or "yes":
    lost = censor

print(name,"is stuck in the south side of chicago",lost)

monster = input("input a scary monster ")
movement = input("input a type of movement ")

print("he is being chased by a",monster,", luckily he is smart enough to", movement,"away")

print("but the ",monster,"is slowly approaching, will he get away?")
t.sleep(1)
print("the",monster,"is getting closer")
t.sleep(0.3)
print(".")
t.sleep(0.3)
print(".")
t.sleep(0.3)
print(".")
print("its getting closer")
t.sleep(0.3)
print(".")
t.sleep(0.3)
print(".")
t.sleep(0.3)
print(".")
print("its getting closer!")
t.sleep(0.3)
print(".")
t.sleep(0.3)
print(".")
t.sleep(0.3)
print(".")
print("OH NO!",heshe,"caught",name,", whatever will he do?")

monsterhealth = 10
playerhealth = 15
monsterdamage = 1
playerdamage = 2
monsterai = r.randint(0,1)

tutorial = input("do you wish to start the tutorial for the combat section? ")
if tutorial == "yes":
    print("attacking lowers the monsters health, guarding has a 50% chance to block the monsters attacks, you take your turn first, once your turn is over the mosnter has a turn, then repeat")
else:
    print("tutorial skipped")
    
    string = "you lose you neet, i didnt even think it was possible to lose"
if censorgage == True:
    censor = string.replace("neet", "illwitted bafoon")
else:
    censor = string

def genericbattle():
    global monsterhealth
    global monsterai
    global monsterdamage
    global playerhealth
    global playerdamage
    global defeatlist
    global defeatchoice
    global player
    global monster
    choice = input("\n1.attack 2.defend ")
    if choice == "1":
        monsterhealth -= playerdamage
        print("you attacked the",monster)
        playerdamage = 2
    elif choice == "2":
        monsterdamage = 0
        print("you raised your shield, defending yourself from the",monster)
    elif choice != "1" or "2":
        print("you chose an option outside of the games parameters, your turn has been skipped")
    if monsterai == 1:
        playerhealth -= monsterdamage
        print("the",monster,"attacked you")
    else:
        playerdamage = 1
        print("the",monster,"defended itself")
    monsterai = r.randint(0,1)
    print(name,"health", playerhealth)
    print(monster,"health", monsterhealth)
    monsterdamage = 1
    if monsterhealth <= 0:
        print("you win")
    elif playerhealth <= 0:
        defeatlist = ["was slain by", "was killed by", "was mauled by"]
        defeatchoice = r.choice(defeatlist)
        print(name,defeatchoice,monster)
        print("ahh you know what")
        t.sleep(0.75)
        print("YOU KNOW WHAT")
        string = "you know what im just crash the whole program SCREW YOU"
        if censorgage == True:
            censor = string.replace("SCREW YOU", "GOODBYE")
        else:
            censor = string
        print(censor)
        quit()
    else:
        genericbattle()

print("\n",name,"health",playerhealth)
print(monster,"health",monsterhealth)
genericbattle()
