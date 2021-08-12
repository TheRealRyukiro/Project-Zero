from API import *

# test 123fdsijfids

class Battle:
    def __init__(self,Player,Enemy):
        self.Player = Player
        self.Enemy = Enemy



    def Fight(self): 
        playerBar = 0
        enemyBar = 0
        while self.Player.Health > 0 and self.Enemy.Health > 0:
            playerBar += self.Player.equippedWeapon.Speed 
            enemyBar += self.Enemy.equippedWeapon.Speed  
        

            if playerBar >= 100:
                playerBar -= 100
                self.Enemy.loseHealth(self.Player.equippedWeapon.dmg)
                clear()
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                 
                print("Name: " + self.Player.firstName + " " + self.Player.lastName + "\nHealth " + str(self.Player.Health) + " / " + str(self.Player.maxHealth)+"\nlv " +  str(self.Player.Level) + "\nExp" + str(self.Player.Exp) + " / " + str(self.Player.ExpLevelUp) + "\nCarry weight: " + str(self.Player.currentCarryWeight) + " / " + str(self.Player.maxCarryWeight) 
                + " lbs\ngold: {:,.2f}".format(self.Player.Money) + "\nDays survived: " + str(self.Player.Days))
                
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


                printC("Its your Turn")
                printC("You Attack for " + str(self.Player.equippedWeapon.dmg) + " damage.")
                printC("Player has: {} health left".format(self.Player.Health)) 
                printC("The " + self.Enemy.lastName + " has: {} health left".format(self.Enemy.Health))
                inputC("Press ENTER to move to next turn.")
                
            
            
            elif enemyBar >= 100:
                enemyBar -= 100
                
                self.Player.loseHealth(self.Enemy.equippedWeapon.dmg)
                clear()
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                 
                print("Name: " + self.Player.firstName + " " + self.Player.lastName + "\nHealth " + str(self.Player.Health) + " / " + str(self.Player.maxHealth)+"\nlv " +  str(self.Player.Level) + "\nExp" + str(self.Player.Exp) + " / " + str(self.Player.ExpLevelUp) + "\nCarry weight: " + str(self.Player.currentCarryWeight) + " / " + str(self.Player.maxCarryWeight) 
                + " lbs\ngold: {:,.2f}".format(self.Player.Money) + "\nDays survived: " + str(self.Player.Days))
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

                printC(self.Enemy.firstName + " " + self.Enemy.lastName + "s Turn")
                printC("The " + self.Enemy.firstName + " " + self.Enemy.lastName + " Attacks for "+ str(self.Enemy.equippedWeapon.dmg)+" damage")
                printC("Player has: {} health left".format(self.Player.Health))
                printC("The " + self.Enemy.lastName + " has: {} health left".format(self.Enemy.Health))
                inputC("Press ENTER to move to next turn.")
                time.sleep(1.5)
    

               
            if(self.Player.Health <= 0):
                printC("The " + self.Enemy.firstName + " " + self.Enemy.lastName + " has won the battle {} health left".format(self.Enemy.Health))
                print("get rekt")
                time.sleep(1.5)
                return False
            
            
            elif(self.Enemy.Health <= 0):
                printC("You defeated the " + self.Enemy.firstName + " " + self.Enemy.lastName + " with {} health left".format(self.Player.Health))
                self.Player.gainExp(5)
                time.sleep(1.5)
                return True
