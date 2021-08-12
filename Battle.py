from API import *

#
class Battle:

    def __init__(self,Player,Enemy):
        # importing the Player object
        self.Player = Player
        # importing the Enemy object
        self.Enemy = Enemy



    def Fight(self): 
        playerBar = 0
        enemyBar = 0
        while self.Player.Health > 0 and self.Enemy.Health > 0:
            
            # The Attack bar for the enemy & the player is based off their speed
            playerBar += self.Player.equippedWeapon.Speed
            enemyBar += self.Enemy.equippedWeapon.Speed
            
            # The enemy & player damage is based off their equipped weapon's damage
            playerDamage = self.Player.equippedWeapon.dmg
            enemyDamage = self.Enemy.equippedWeapon.dmg

            #This combines the first & last name of the enemy and the player
            playerFullName = self.Player.firstName + " " + self.Player.lastName
            enemyFullName = self.Enemy.firstName + " " + self.Enemy.lastName

            if playerBar >= 100:
                # The Player's turn to attack
                playerBar -= 100
                self.Enemy.loseHealth(playerDamage)
                clear()
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                 
                print("Name: {Name}\
                      \nHealth: {Health} / {maxHealth}\
                      \nlevel: {Level}\
                      \nExp: {Exp} / {ExpLevelUp}\
                      \nCarry weight: {currentCarryWeight} / {maxCarryWeight}lbs\
                      \nGold: {Money:,.2f}\
                      \nDays survived: {Days}".format(
                                                        Name = playerFullName,
                                                        Health = str(self.Player.Health),
                                                        maxHealth = str(self.Player.maxHealth),
                                                        Level = str(self.Player.Level),
                                                        Exp = str(self.Player.Exp),
                                                        ExpLevelUp = str(self.Player.ExpLevelUp),
                                                        currentCarryWeight = str(self.Player.currentCarryWeight),
                                                        maxCarryWeight = str(self.Player.maxCarryWeight),
                                                        Money = str(self.Player.Money),
                                                        Days = str(self.Player.Days)
                                                        ))
                
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


                printC("It's your turn")
                printC("You attack for {Damage} damage.".format(Damage = playerDamage))
                printC("Player has {Health} health left".format(Health = str(self.Player.Health))) 
                printC("The {Name} has {Health} health left".format(Name = enemyFullName, Health = str(self.Enemy.Health)))
                inputC("Press ENTER to move to next turn.")
                
            
            
            elif enemyBar >= 100:
                enemyBar -= 100
                
                self.Player.loseHealth(enemyDamage)
                clear()
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                
                print("Name: {Name}\
                      \nHealth: {Health} / {maxHealth}\
                      \nlevel: {Level}\
                      \nExp: {Exp} / {ExpLevelUp}\
                      \nCarry weight: {currentCarryWeight} / {maxCarryWeight}lbs\
                      \nGold: {Money:,.2f}\
                      \nDays survived: {Days}".format(
                                                        Name = playerFullName,
                                                        Health = str(self.Player.Health),
                                                        maxHealth = str(self.Player.maxHealth),
                                                        Level = str(self.Player.Level),
                                                        Exp = str(self.Player.Exp),
                                                        ExpLevelUp = str(self.Player.ExpLevelUp),
                                                        currentCarryWeight = str(self.Player.currentCarryWeight),
                                                        maxCarryWeight = str(self.Player.maxCarryWeight),
                                                        Money = str(self.Player.Money),
                                                        Days = str(self.Player.Days)
                                                        ))
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

                printC("{firstName} {lastName}s Turn".format(firstName = self.Enemy.firstName, lastName = self.Enemy.lastName))
                
                printC("The {Name} attacks for {Damage} damage".format(Name = enemyFullName, Damage = enemyDamage))
                printC("Player has: {Health} health left".format(Health = self.Player.Health))
                printC("The {Name} has: {Health} health left".format(Name = enemyFullName, Health = self.Enemy.Health))
                inputC("Press ENTER to move to next turn.")
                time.sleep(1.5)
    

               
            if(self.Player.Health <= 0):
                printC("The {Name} has won the battle with {Health} health left".format(Name = enemyFullName, Health = str(self.Enemy.Health)))
                print("get rekt")
                time.sleep(1.5)
                return False
            
            
            elif(self.Enemy.Health <= 0):
                printC("You defeated the {Name} with {Health} health left".format(Name = enemyFullName, Health = str(self.Enemy.Health)))
                self.Player.gainExp(5)
                time.sleep(1.5)
                return True
