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

global playerXP
playerXP = 0
global level
level = 1
global levelupcost
levelupcost = 500

#start tutorial/intro section

global player
print('a lot is still in development and not functional, also ive been coding 2 hours ontop of schhol on 4 hours of sleep so im too tired to test shit, ill work on fixing the stuff that wont work tommorow ig')
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

global monster
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
    if playerXP > levelupcost:
        level += 1
        levelupcost *= 1.5
        wonbattle()
    else:
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
    print('the left path seems rather damp')

def forestsectionright():
    print('the right path is much thicker, who knows whats lurking in the thick mass of flaura')

def forestsection():
    print('you have entered the spooky forest! Rumor has it that the secret forest key lurks at the end\n')
    print('you begin navigating the dark twisting forest')
    while lrchoicesectloop == True:
        lrchoice = ('you come upon a fork in the path, do you go left or right')
        if lrchoice == 'left':
            print('you went left')
            lrchoicesectloop = False
            forestsectionleft()
        elif lrchoice == 'right':
            print('you went right')
            lrchoicesectloop = False
            forestsectionright()
        else:
            print('you choose an option outside of the games paraneters')
    
def chooselocation():
    print('choose which section to go to')
    choiceloc = input('1 = forest, 2 = cave, 3 = sky realm, 4 = death castle')
    if choiceloc == '1':
        forestsection()
    if choiceloc == '2':
        cavesection()
    if choiceloc == '3':
        skyrealm()
    if choiceloc == '4':
        deathcastle()
    if choiceloc != '1' or '2' or '3' or '4':
        print('you choose an option other than the 4 shown, this may be because you typed the place name instead of its corresponding number')
        chooselocation()
