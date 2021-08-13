

#----------Imports----------#
from Person import Person
import Weapon
from Event import Event
from API import *
#----------Imports----------#


clear()
answer = input("Would you like to run the game? (yes/no) ")
if(answer == "no"):
    sys.exit()  
Difficulty = input("Please select from one of three difficulties (Easy Medium Hard) ").capitalize()
clear()
firstName = input("What is your adventurer's first name: ").capitalize()  # asks player for first name
clear()
lastName = input("What is your adventurer's last name: ").capitalize() # asks player for last name
clear()



Player = None # creates the player 
equippedWeapon = None # creates the equipped weapon and sets it to none (waits to be set by the player)




while True:

    print("First Name: " + firstName + "\nLast Name: " + lastName)
    
    answer = input("Adventurer " + firstName + " " + lastName + ", Is this your character? (yes/no)  ").lower()

    if( answer == "yes"): 
        clear()
        Player = Person(firstName,lastName,Difficulty,100,1,True,equippedWeapon)
        break
       
    elif(answer == "no"): # asks the user to re-enter the disired stats
        clear()
        firstName = input("What is your first name: ").capitalize()  # asks player for first name 
        clear()
        lastName = input("What is your last name: ").capitalize()
        clear()
        
    


        
    else: 
        
        print("Please type yes or no as your answer")
clear()

print("Your starting gold is: {:,.2f}".format(Player.Money))
print("Your starting carry weight is: "+  str(Player.currentCarryWeight) + "/ "+ str(Player.maxCarryWeight))
input("Press enter key to continue...")
print("\n~~~~~~~~~~~~~~~~~~~~~~")
4
print("First Name: " + Player.firstName + "\nLast Name: " + Player.lastName + "\nWeight: " + str(Player.currentCarryWeight) +  "/ " + str(Player.maxCarryWeight) 
+ " lbs\nGold: {:,.2f}".format(Player.Money))
print("\n~~~~~~~~~~~~~~~~~~~~~~")






while True:

    answer = input("Please choose a weapon: Sword, Bow or a Warhammer.\nFor more info about the weapons, type (info): ").capitalize()
    #-----------------------------starting weaopn choice-------------------------------#
    if(answer == "Sword"):
        Player.equippedWeapon = Weapon.rustySword   #sets the players equipped with to the players disired starting weapon with its attributes from the weapon class
        print("You have chosen the "+ Player.equippedWeapon.name)
        break
    if(answer == "Bow"):
        Player.equippedWeapon = Weapon.trainingBow
        print("You have chosen the "+ Player.equippedWeapon.name)
        break
    if(answer == "Warhammer"):
        Player.equippedWeapon = Weapon.wornWarhammer 
        print("You have chosen the "+ Player.equippedWeapon.name)
        break
    if(answer == "Info"):
        clear()
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("The sword is a one handed weapon that deals morderate damage, but has a fast attack speed.")
        print("The bow is a two handed weapon the deals high damage, and has a medium attack speed.")
        print("The warhammer is a two handed weapon the deals exterme damage, but has a slow attack speed.")
       #-----------------------------End weaopn choice-------------------------------#



input("Press enter to start your adventure...")
clear()
#--------------------------Start of the game--------------------------#
spawnEvent = Event(Player)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
answer = input("You awake in a wagon with your hands bound. Nobody is around do you. Do you try to escape? ")
if (answer == "yes"):
    print("You have succsessfully escaped!!")
    Player.gainDay()
    
if (answer == "no"):
    print("You did nothing, you were eventuly spotted then killed")
    print("\n~~~~~~~~~~~~~~~~~~~~~~")

    print("First Name: " + Player.firstName + " " + Player.lastName + "\nHealth " + str(Player.Health) + " / " + str(Player.maxHealth)+"\nlv " + str(Player.Level) + "\nCarry weight: " + str(Player.currentCarryWeight) + " / " + str(Player.maxCarryWeight) 
        + " lbs\ngold: {:,.2f}".format(Player.Money) + "\nDays survived: " + str(Player.Days))
    print("\n~~~~~~~~~~~~~~~~~~~~~~")
    sys.exit()






while True:

    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    
    print("Name: " + Player.firstName + " " + Player.lastName + "\nHealth " + str(Player.Health) + " / " + str(Player.maxHealth)+"\nlv " +  str(Player.Level) + "\nExp" + str(Player.Exp) + " / " + str(Player.ExpLevelUp) + "\nCarry weight: " + str(Player.currentCarryWeight) + " / " + str(Player.maxCarryWeight) 
        + " lbs\ngold: {:,.2f}".format(Player.Money) + "\nDays survived: " + str(Player.Days))
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    
    
    spawnEvent.newEvent()



