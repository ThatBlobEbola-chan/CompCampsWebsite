from random import randint
import sys

classes = ['Memelord', 'Weed Doctor', 'Over Hyperactive Piece of Garbage', 'Tank. Like, an actual tank.']
classHealth = [100, 120, 50, 150]
classDamage = [5, 3, 10, 2]


playerName = ''
playerHealth = classHealth
playerClass = -1

monsterNames = ['Angry Mcdonalds Employee', 'Pepe', 'Ice Cream', 'Bed', 'Five Nights at Freddys']
monsterHealth = [60, 150, 10, 40, 70]
monsterDamage = [4, 2, 7, 5, 3]

input ("Waddup ya piece of garbage, ready for the SECOND TIME WASTING SIMULATOR?")
input ("yeah k get ready brohamski")

playerName = input("State your name, as you're in for a world of pain and it is the first step to getting through it.")
print("Choose a class.")
playerClass = input("0 for MEMELORD, 1 for WEED DOCTOR, 2 for OVERHYPERACTIVE PIECE OF GARBAGE, 3 for TANK. LIKE, AND ACTUAL TANK.")

input("Welcome " + playerName + " to TIME WASTING SIMULATOR 2!!")

def battle(monsterName, monsterHealth, monsterDamage):
    global playerHealth
    print ("You encountered " + monsterName)

    while(monsterHealth > 0):
        print (monsterName + " has " + str(monsterHealth) + " health")
        print (playerName + " has " + str(classHealth) + " health")
        if (monsterName == 'Angry Mcdonalds Employee'):
            print("This monster is a minimum wage employee who was angered after you shortchanged them.")
        if (monsterName == 'Pepe'):
            print("This monster is a sentient meme, bloodlusted by meme magic. Has high HP but doesn't deal much damage.")
        if (monsterName == 'Ice Cream'):
            print("This monster is an ice cream cone.. It looks mighty frickin tasty. Try not to get brainfreeze though.")
        if (monsterName == 'Bed'):
            print("Its so soft.. and comfy.. HAAAAAAAH")
        if (monsterName == 'Five Nights at Freddys'):
            print("This is legitimately a generic horror game. May cause sudden heart failure from very spooky frights.")
        
        print("What would you like to do??")
        print("(Press R to RUN, A to ATTACK, H to HEAL.)")
        choice = input().upper()
        if (choice == 'R'):
            if (randint(0, 1) == 1):
                print("You ran away!")
                return
            else:
                print("You frickin' suck at running.")
        if (choice == 'A'):
            monsterHealth -= randint(0, classDamage)
            classHealth -= randint(0, monsterDamage)

        if (choice == 'H'):
            heal()

        if (classHealth <= 0):
            print("You suck so hard you can't move anymore. You're dead.")
            sys.exit()
        
    input("You have defeated " + monsterName + ". Press ENTER to continue.")

def heal():
    print("HEAL YOSELF")
    classHealth + randint(0,20)
            
    

def gameLoop():
    while(True):
        print("What you wanna do B")
        choice = input().upper()
        if (choice == 'Q'):
            sys.exit()
        if (choice == 'B'):
            m = randint(0,4)
            battle(monsterNames[m], monsterHealth[m], monsterDamage[m])

gameLoop()
