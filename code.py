import time as t
import random as r

sanitisation = 0
censorblock = 0

while sanitisation != 1 or 2:
    sanitisation = input("do you wish to play a censored version of the game (removes common coarse language and possibly vulgar language i.e 'neet'), yes or no?  ")
    if sanitisation == "yes":
        print("you are proceeding with the censored version")
        sanitisation = 1
    elif sanitisation == "no":
        print("you are proceeding with the uncensored version")
        sanitisation = 2
    elif sanitisation != "yes" or "no":
        print("please input yes or no")

name = input("enter your name here ")
lost = input("are you lost or not? ")

heshe = r.randint(0,1)

if heshe == 1:
    heshe = "he"
else:
    heshe = "she"

if lost == "yes":
    lost = "he is lost!"
elif lost == "no":
    lost = "luckily he is not lost as the south side of chicago is a very dangerous place "
elif lost != "no" or "yes":
        if sanitisation == 1:
            censorblock = "half-baked muffin"
        elif sanitisation == 2:
            censorblock = "neet"
    lost = "(you typed something other than yes or no you",censorblock,")"

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

print("monster health",monsterhealth)
print("player health",playerhealth)
while monsterhealth > 0:
    choice = input("1.attack 2.defend")
    if choice == "1":
        monsterhealth -= playerdamage
        print("you attacked the",monster)
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
    print("player health", playerhealth)
    print("monster health", monsterhealth)
    
    if monsterhealth <= 0:
        print("you win")
    elif playerhealth <= 0:
        print("you lose you ilwitted bafoon, i didnt even think it was possible to lose")
        t.sleep(0.75)
        print("YOU KNOW WHAT")
        print("you know what im just crash the whole program SCREW YOU")
        quit()
