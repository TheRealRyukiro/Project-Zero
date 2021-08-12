"""
    This is the Person Class. This class is used to create new people.

"""


class Person:
    def __init__(self, firstName, lastName, Difficulty, health, Speed,isFriendly = True, equippedWeapon = None): #def means to define x as a function. __init__ is the constructor that initializes the class when called. everything in the () are parameters to the constructor.
        # The Person's name
        self.firstName = firstName
        self.lastName = lastName
        
        # The Person's Level management
        self.Level = 1
        self.Exp = 0
        self.ExpLevelUp = 10
        

        # The Person's weight        
        self.maxCarryWeight = 30
        self.currentCarryWeight = 0
        # How much money the person has to use or drop.
        self.Money = 0
        # How much health the person has
        self.maxHealth = health
        self.Health = self.maxHealth
        
        # default speed of person
        self.Speed = Speed
        
        
        # what weapon the person has equipped
        self.equippedWeapon = equippedWeapon
        
        # what Difficulty is the person
        self.Difficulty = Difficulty
        # if the person is friendly to the player or not
        self.isFriendly = isFriendly
        
        # how many Days the player survived
        self.Days = 0


        # modifies stats based on the Person's Difficulty
        if(self.Difficulty.capitalize() == "Easy"):
            self.Money = 500
            if(isFriendly): self.Health *= 2
            self.maxCarryWeight *= 1.5
            self.Health = round(self.Health)
            self.maxCarryWeight = round(self.maxCarryWeight)
            self.Exp *= 1.5
            self.Exp = round(self.Exp)
        elif(self.Difficulty.capitalize() == "Medium"):
            self.Money = 100
            if(isFriendly): self.Health *= 1
            self.Health = round(self.Health)
            self.maxCarryWeight *= 1
            self.maxCarryWeight = round(self.maxCarryWeight)
            self.Exp *= 1
            self.Exp = round(self.Exp)
        elif(self.Difficulty.capitalize() == "Hard"):
            self.Money = 0
            if(isFriendly): self.Health *= 0.5
            self.Health = round(self.Health)
            self.maxCarryWeight *= 0.5
            self.maxCarryWeight = round(self.maxCarryWeight)
            self.Exp *= 0.8
            self.Exp = round(self.Exp)
        

    # Person gains a set amount of health
    def gainHealth(self, addHealth):
        self.Health += addHealth
        if (self.Health > self.maxHealth):
            self.Health = self.maxHealth
        return self.Health # returns how much health the person has
    
    
    # Person loses a set amount of health
    def loseHealth(self, loseHealth):
        self.Health -= loseHealth
        return self.Health # returns how much health the person has
    
    # Person gains a set amount of carry weight
    def gainWeight(self,addWeight):
        self.maxCarryWeight += addWeight
        return self.weight # returns how much weight the person can carry

    # Person loses a set amount of carry weight
    def loseWeight(self,loseWeight):
        self.weight -= loseWeight
        return self.weight # returns how much weight the person can carry
    

    # Person gains a set amount of money
    def gainMoney(self,addMoney):
        self.Money += addMoney
        return self.Money # returns how much money the person
    

    # Person loses a set amount of money
    def loseMoney(self,loseMoney):
        self.Money -= loseMoney
        return self.Money # returns how much money the person


    # Person gains a survived day
    def gainDay(self):
        self.Days += 1
        return self.Days # Adds a day survived then returns how many Days it survived
    

    def gainExp(self,amount):
        self.Exp += amount
        while(self.Exp >= self.ExpLevelUp):
            print("Level Up")
            self.Level += 1
            self.ExpLevelUp = round(100*1.38**(self.Level-5))
            self.maxHealth += 10
            self.maxCarryWeight += 5
        return self.Level

    