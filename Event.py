"""
list all type of events in the game
shop encounter
random encounters
help encounters
loot encounters
monster encounters
find encounter
finish encounter messages
Have shop encounters between events set after x amount of encounts based on world tier





"""
#----------Imports----------#

from math import *
from Person import Person
from Battle import Battle
import Weapon
from API import *

#----------End of Imports----------#



#----------Predefined Arrays----------#






#-----------------Location encounters------------------------#
locationEncounter = ["Along your journey you come across a camp.",
                     "You encounter a stray goblin on your journey.",
                     "You walk along the path and find tower.",
                    ]

#-----------------Location encounters------------------------#


#-----------------Tower encounters------------------------#
towerEncounter = ["You enter the tower and find a ragged bag. Who knows what's inside?!!",
                  "You walk in to the tower and spot a sleeping goblin."
                  ]
#-----------------Tower encounters------------------------#


#-----------------Bag randomizer------------------------#
bagRandomizer = ["You open the bag and to your suprise you find a pouch of gold!!!",
                 "You open the bag and find a mysterious tome, you open the book.\
                 The books pages turn rapidly.You have acquired new knowledge!!!"]
#-----------------Bag randomizer------------------------#


#-----------------Camp encounters------------------------#
campEncounter = ["You walk closer to the camp.You spot a mysterious figure walking out of one the tents.",
                 "You walk closer to the camp. it appears to be deserted..."  ]

#------------------shop weapon radomizer-----------------#
shopWeaponRadomizer = [ Weapon.rustySword,
                       Weapon.trainingBow,
                       Weapon.wornWarhammer,
                       Weapon.vineStaff]
#------------------shop weapon radomizer-----------------#

#------------------shop potion radomizer-----------------#
shopPotionRadomizer = ["Health potion",
                       "Speed potion"]

#------------------End shop potion radomizer-------------#                 

#----------End of Predefined----------#


#----------Event-----------#
class Event:
    def __init__(self,Player):
        self.Player = Player
    def die(self): # This function displays youre stats on death
        clear() # clears the screen to cleanly diplay the players death stats
         
        print("Name: {Name}\
            \nHealth: {Health} / {maxHealth}\
            \nlevel: {Level}\
            \nExp: {Exp} / {ExpLevelUp}\
            \nCarry weight: {currentCarryWeight} / {maxCarryWeight}lbs\
            \nGold: {Money:,.2f}\
            \nDays survived: {Days}".format(
                                            Name = self.fullName,
                                            Health = self.Health,
                                            maxHealth = self.maxHealth,
                                            Level = self.Level,
                                            Exp = self.Exp,
                                            ExpLevelUp = self.ExpLevelUp,
                                            currentCarryWeight = self.currentCarryWeight,
                                            maxCarryWeight = self.maxCarryWeight,
                                            Money = self.Money,
                                            Days = self.Days
                                                        ))
        sys.exit()
#----------Event-----------#

    
#----------------Battle chances--------------------------#
   
    def chanceToFlee(self,chance): 
        return random.random() < chance # Example self.chanceToFlee((30 / 100)): 30 percent to flee from the enemy
   
    def chanceToBeFriendly(self,chance):
        return random.random() < chance  # Example self..chanceToBeFriendly chance of someone being friendly


    #------------------------chance Encounters---------------------#
    
    def chanceForDruid(self,chance):
        return random.random() < chance # Example self.chanceForDruid percent percent chance to find a druid 
    
    def chanceForGoblin(self,chance):
        return random.random() < chance # Example self.chanceForGoblin
     

    #------------------------Escape chance---------------------#
    
    def newEvent(self): # function spawns a new event 
        answerCheck = True
        Player = None 
        while True:    

            if(answerCheck): event = random.choice(locationEncounter) # randomly pickes a location encounter for the locationEncounter list
            
            printC(event) # prints the encounter that has been chosen to the player.
            
            #------------------------------------Starts the tower encounter------------------------------------#
            while True: 
                    if(event == "You walk along the path and find tower."):
                        answer = inputC("Would you like to enter the tower (yes/no) ").capitalize() # user decides whether to enter the tower or not (risks included)
                        if(answerCheck): encounter = random.choice(towerEncounter)

                        if(answer == "Yes"):   # Decision statement from the player to enter the tower
                            answerCheck = True
                            self.Player.gainDay()   # add 1 day to the gain day counter
                               # this picks a random encounter inside the towerEncounter array. then stores it temporarily in the encounter var

                            printC(encounter)
                            inputC("Press any key to continue...")
                            
                            if encounter == ("You enter the tower and find a ragged bag. Who knows what's inside?!!"):
                                

                                #-------------------------------------Start bagRandomizer-----------------------------------#
                                if(answerCheck): encounter = random.choice(bagRandomizer)   # this picks a random encounter inside the towerEncounter array. then stores it temporarily in the encounter var
                                printC(encounter)
                                inputC("Press any key to continue...")
                                
                                if encounter == ("You open the bag and to your suprise you find a pouch of gold!!!"):
                                    

                                    self.Player.gainMoney(random.randrange(0 , 26))
                                    break  # randomly pickes a number between 0 and 25 to give gold to the player
                                

                                if encounter == ("You open the bag and find a mysterious tome, you open the book.\
                                                The books pages turn rapidly.\
                                                You have acquired new knowledge!!!"):
                                    self.Player.gainExp(random.randrange(0 , 101))
                                    break
                                #-------------------------------------End bag Randomizer-----------------------------------#

                                #------------------------------------Start of goblin in tower------------------------------#              
                            if encounter == ("You walk in to the tower and spot a sleeping goblin."):
                                
                                if(answerCheck): encounter =  inputC("Sneak by or surprise attatck!! (sneak or surprise) ")
                                sleepyGoblin = Person ("Sleepy","goblin",self.Player.Difficulty,30,0,False, Weapon.rustySword)
                                

                                if(encounter == "surprise"):
                                    if (battle.Fight() == False): self.die() # starts the battle state
                                    self.Player.gainDay()   # add 1 day to the gain day counter
                                    break
                                    

                                if(encounter == "sneak"): # if you try to sneack by the enemy
                                    sleepyGoblin = Person ("Sleepy","goblin",self.Player.Difficulty,30,0,False, Weapon.rustySword)
                                    break
                                
                                else:
                                    printC("I'm sorry, but that's not a valid answer")
                                    answerCheck = False


                                    if self.chanceToFlee((30 / 100)):
                                        surprisedGoblin = Person ("Surprised","goblin",self.Player.Difficulty,30,0,False, Weapon.rustySword) # sets the enemy's parameters
                                    
                                        battle = Battle(self.Player, surprisedGoblin) # battle takes the player and the enemy name 
                                
                                        printC("You successfully snuck by the {} {} !".format(sleepyGoblin.firstName , sleepyGoblin.lastName ))
                                        self.Player.gainDay() # add 1 day to the gain day counter
                                        break


                                    else:
                                        printC("You failed your attempt to flee from the {} {} !".format(sleepyGoblin.firstName , sleepyGoblin.lastName ))
                                        if (battle.Fight() == False): self.die() #starts the battle state True if you win false if you die
                                        self.Player.gainDay() # add 1 day to the gain day counter
                                        break
                                #------------------------------------End of goblin tower------------------------------#   
                                
                            
                        elif(answer == "No"): # Decision statement from the player to enter the tower  
                            inputC("You continue on your way.Press enter to continue...") # End of encounter
                            self.Player.gainDay() # Add 1 day to the gain day counter
                            break
                        else:
                            printC("I'm sorry, but that's not a valid answer") # catch statement 
                            answerCheck = False
                #----------------------------------------End of tower encounter-------------------------------------#
                            
             #----------------------------------------start of camp encounter---------------------------------------#while true:        

                    if(event == "Along your journey you come across a camp."):
                        if(answerCheck): encounter = random.choice(campEncounter)
                        printC(encounter)
                        
                        if encounter == ("You walk closer to the camp. it appears to be deserted..."):
                            answer = inputC("Would you like to sleep at the camp (yes/no) ") # user decides whether to sleep at the cam or not (risks included)


                            if(answer == "yes"):
                                answer == inputC("You slept at the camp.Press enter to continue...")
                                self.Player.gainDay()
                                self.Player.gainHealth(10)
                                printC("You gained 10 hit ponits")
                                answerCheck = True
                                break


                            elif(answer == "no"):
                                answer == inputC("You continue on your way.Press enter to continue...")
                                self.Player.gainDay()
                                answerCheck = True
                                break
                                
                                
                            else:
                                printC("I'm sorry, but that's not a valid answer")
                                answerCheck = False
                                    

                        elif encounter == ("You walk closer to the camp.You spot a mysterious figure walking out of one the tents."):

                            answer = inputC("Do you greet the mysterious figure?!!! (yes/no) ")

                            if(answer == "yes"):

                                inputC("You speak out to the person in the shadows")
                                if self.chanceForDruid((30 / 100)):

                                    inputC("You see the figure turn fast as he is was startled. Its a druid!!!")
                                    if self.chanceToBeFriendly((50 / 100)):

                                        inputC("The druid attacks you on sight")
                                        druid = Person ("Exiled","druid",self.Player.Difficulty,30,1,False, Weapon.vineStaff)
                                        battle = Battle(self.Player, druid)
                                            
                                        if (battle.Fight() == False): self.die()
                                        self.Player.gainDay()
                                        answerCheck = True
                                        break
                                        
                                elif inputC("The druid appears to be friendly. He pulls the energy from the plants and trees around to heal all your wounds"):
                                    self.Player.Health = self.Player.maxHealth
                                    inputC("You have been fully restored says the druid!!!!")
                                    answerCheck = True
                                    break
                                        

                                elif self.chanceForGoblin((30 / 100)):
                                        printC("You see the figure turn fast as he is was startled. Its a goblin!!!")
                                        if self.chanceToBeFriendly((50 / 100)):

                                            goblin = Person ("wondering","goblin",self.Player.Difficulty,30,1,False, Weapon.rustySword)
                                            battle = Battle(self.Player, goblin)

                                            if (battle.Fight() == False): self.die()
                                            self.Player.gainDay()
                                            answerCheck = True
                                            break

                                        elif inputC("The goblin appears to be friendly"):
                                            inputC("The goblin offers to show you his wears")
                                            answer == inputC("Would you like to see his wears? (yes/no) ")   

                                            if(answer == "yes"):
                                                inputC("The goblin shows you his wears")
                                                shopWeapon1 = random.choice(shopWeaponRadomizer)
                                                shopWeapon2 = random.choice(shopWeaponRadomizer) 
                                                    
                                                answer = inputC("The goblins stock includes: {} for {} Gold ".format(shopWeapon1 , str(shopWeapon1.goldCost )) /
                                                "{} for {} gold" (shopWeapon2, str(shopWeapon2.goldCost)) + " Gold " + random.choice(shopPotionRadomizer)).capitalize()
                                                printC("Please type weapon one if you chose to buy the shopWeapon1")
                                                printC("Please type weapon two if you chose to buy the second weapon")
                                                printC("Please type potion if you chose to buy the potion")
                                                printC("Type leave to the the shop")
                                                if answer == ("Weapon one"):
                                                    
                                                    shopWeapon1.goldCost = self.Player.loseMoney()

                                                    inputC("You have purchased the " + Weapon.name)
                                                    inputC("Cool a new weapon")
                                                    answerCheck = True
                                                    break
                                                elif answer == ("Weapon one"):
                                                    shopWeapon2.goldCost = self.Player.loseMoney()
                                                    
                                                    inputC("You have purchased the " + Weapon.name)
                                                    inputC("Cool a new weapon")
                                                    answerCheck = True
                                                    break
                                                elif answer == ("Potion"): # potion not currently coded
                                                    answerCheck = True
                                                    break

                                                elif answer == ("leave"):
                                                    inputC("You left the shop!!!")
                                                    answerCheck = True
                                                    break
                                                else:
                                                    printC("Sorry thats not a answer")
                                                    answerCheck = False
                                                    
                                            if(answer == "no"):
                                                inputC("You decide not to see his wears and you continue on your way...")
                                                answerCheck = True 
                                                break  
                                            else:
                                                print("Sorry thats not a answer")
                                                answerCheck = False

                            if(answer == "no"):
                                inputC("You continue on your way...")
                                answerCheck = True
                                break
                            else:
                                printC("I'm sorry, but that's not a valid answer")
                                answerCheck = False




             #----------------------------------------End of camp encounter---------------------------------------#   
            
            #-----------------------------------------Start of goblin encounter--------------------------------#
            
                    if(event == "You encounter a stray goblin on your journey."):

                        answer = inputC("Would you like to face the goblin or try to flee!! (face or flee) ")
                        goblin = Person ("lonely","goblin",self.Player.Difficulty,30,1,False, Weapon.rustySword)
                        battle = Battle(self.Player, goblin) # battle takes the player and the enemy 
                
                
                        if(answer == "face"):
                            if (battle.Fight() == False): self.die()
                            self.Player.gainDay()
                            answerCheck = True
                            break


                        if(answer == "flee"):
                            if self.chanceToFlee((30 / 100)):
                                printC("You successfully fled from the {} {}!"  .format( goblin.firstName , goblin.lastName))
                                self.Player.gainDay()
                                answerCheck = True
                                break

                        else:
                            printC("You failed your attempt to flee from the {} {}!"  .format( goblin.firstName , goblin.lastName))
                            if (battle.Fight() == False): self.die()
                            answerCheck = True
                            break

                    else:
                        printC("I'm sorry, but that's not a valid answer")
                        answerCheck = False
                #-----------------------------------------End of goblin encounter--------------------------------#
                
