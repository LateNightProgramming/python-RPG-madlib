#WARNING! program is currently not fully functional
#still shit

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

playerXP = 0
level = 1
levelupcost = 500

#start tutorial/intro section

global player
name = input("\nenter your name here ")
lost = input("are you lost or not? ")

global heshe
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
    global playerhealth
    global monsterdamage
    global defeatlist
    global defeatchoice
    global monsterai
    global playerdamage
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

def wonbattle():
    global playerXP
    global level
    global levelupcost
    
    playerXP = level * 400

    if playerXP > levelupcost:
        level += 1
        levelupcost *= 1.5
        wonbattle()
    else:
        print('player level:',level)
        print('level up complete')
    

print("\n",name,"health",playerhealth)
print(monster,"health",monsterhealth)
genericbattle()
wonbattle()

#end tutorial section/intro

randomencounter = []

def randomencounter():
    global randomencounter
    randomencounter = r.choice([True or False or '1' or '2' or '3' or '4'])
    if randomencounter == True:
        print('a battle has started!/n')
        genericbattle()

def forestsectionleft():
    global lrchoicesectloop
    lrchoicesectloop = False

    print('the left path seems rather damp')

def forestsectionright():
    print('the right path is much thicker, who knows whats lurking in the thick mass of flaura')

lrchoicesectloop = True

def forestsection():
    global lrchoice
    global lrchoicesectloop
    lrchoicesectloop = True
    print('you have entered the spooky forest! Rumor has it that the secret forest key lurks at the end\n')
    print('you begin navigating the dark twisting forest')
    lrchoice = input('do you wish to go left or right?')
    while lrchoicesectloop == True:
        if lrchoice == 'left':
            print('you went left')
            forestsectionleft()
        elif lrchoice == 'right':
            print('you went right')
            lrchoicesectloop = False
            forestsectionright()
        else:
            print('you choose an option outside of the games paraneters')
            forestsection()
    
def chooselocation():
    print('test')
    global choicelocwhile
    global choiceloc
    choicelocwhile = True
    print('choose which section to go to')
    choiceloc = input('1 = forest, 2 = cave, 3 = sky realm, 4 = death castle')
    while choicelocwhile == True:
        if choiceloc == '1':
            forestsection()
        elif choiceloc == '2':
            cavesection()
        elif choiceloc == '3':
            skyrealm()
        elif choiceloc == '4':
            deathcastle()
        else:
            print('you choose an option other than the 4 shown, this may be because you typed the place name instead of its corresponding number')
            chooselocation()
chooselocation()
