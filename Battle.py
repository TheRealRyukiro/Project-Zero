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

        Player = self.Player
        Enemy = self.Enemy
        while Player.Health > 0 and Enemy.Health > 0:
            
            # The Attack bar for the enemy & the player is based off their speed
            playerBar += Player.equippedWeapon.Speed
            enemyBar += Enemy.equippedWeapon.Speed
            
            # The enemy & player damage is based off their equipped weapon's damage
            playerDamage = Player.equippedWeapon.dmg
            enemyDamage = Enemy.equippedWeapon.dmg

            if playerBar >= 100:
                # The Player's turn to attack
                playerBar -= 100
                Enemy.loseHealth(playerDamage)
                clear()
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                 
                print("Name: {Name}\
                      \nHealth: {Health} / {maxHealth}\
                      \nlevel: {Level}\
                      \nExp: {Exp} / {ExpLevelUp}\
                      \nCarry weight: {currentCarryWeight} / {maxCarryWeight}lbs\
                      \nGold: {Money:,.2f}\
                      \nDays survived: {Days}".format(
                                                        Name = Player.fullName,
                                                        Health = Player.Health,
                                                        maxHealth = Player.maxHealth,
                                                        Level = Player.Level,
                                                        Exp = Player.Exp,
                                                        ExpLevelUp = Player.ExpLevelUp,
                                                        currentCarryWeight = Player.currentCarryWeight,
                                                        maxCarryWeight = Player.maxCarryWeight,
                                                        Money = Player.Money,
                                                        Days = Player.Days
                                                        ))
                
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


                printC("It's your turn")
                printC("You attack for {Damage} damage.".format(Damage = playerDamage))
                printC("Player has {Health} health left".format(Health = str(Player.Health))) 
                printC("The {Name} has {Health} health left".format(Name = Enemy.fullName, Health = str(Enemy.Health)))
                inputC("Press ENTER to move to next turn.")
                
            
            
            elif enemyBar >= 100:
                enemyBar -= 100
                
                Player.loseHealth(enemyDamage)
                clear()
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                
                print("Name: {Name}\
                      \nHealth: {Health} / {maxHealth}\
                      \nlevel: {Level}\
                      \nExp: {Exp} / {ExpLevelUp}\
                      \nCarry weight: {currentCarryWeight} / {maxCarryWeight}lbs\
                      \nGold: {Money:,.2f}\
                      \nDays survived: {Days}".format(
                                                        Name = Player.fullName,
                                                        Health = str(Player.Health),
                                                        maxHealth = str(Player.maxHealth),
                                                        Level = str(Player.Level),
                                                        Exp = str(Player.Exp),
                                                        ExpLevelUp = str(Player.ExpLevelUp),
                                                        currentCarryWeight = str(Player.currentCarryWeight),
                                                        maxCarryWeight = str(Player.maxCarryWeight),
                                                        Money = str(Player.Money),
                                                        Days = str(Player.Days)
                                                        ))
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

                printC("{firstName} {lastName}s Turn".format(firstName = Enemy.firstName, lastName = Enemy.lastName))
                
                printC("The {Name} attacks for {Damage} damage".format(Name = Enemy.fullName, Damage = enemyDamage))
                printC("Player has: {Health} health left".format(Health = Player.Health))
                printC("The {Name} has: {Health} health left".format(Name = Enemy.fullName, Health = Enemy.Health))
                inputC("Press ENTER to move to next turn.")
                time.sleep(1.5)
    

               
            if(Player.Health <= 0):
                printC("The {Name} has won the battle with {Health} health left".format(Name = Enemy.fullName, Health = str(Enemy.Health)))
                print("get rekt")
                time.sleep(1.5)
                return False
            
            
            elif(Enemy.Health <= 0):
                printC("You defeated the {Name} with {Health} health left".format(Name = Enemy.fullName, Health = str(Enemy.Health)))
                Player.gainExp(5)
                time.sleep(1.5)
                return True
