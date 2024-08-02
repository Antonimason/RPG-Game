class Enemy:
    def __init__(self, name, exp, health, mana, attack, specialAttack, defense, healing):
        self.name = name
        self.exp = exp
        self.health = health
        self.mana = mana
        self.attack = attack
        self.specialAttack = specialAttack
        self.defense = defense
        self.healing = healing
        
    def getName(self):
        return self.name
    
    def getExp(self):
        return self.exp
    
    def getHealth(self):
        return self.health
    
    def getMana(self):
        return self.mana
    
    def getAttack(self):
        return self.attack
    
    def getSpecialAttack(self):
        return self.specialAttack
    
    def getDefense(self):
        return self.defense
    
    def getHealing(self):
        return self.healing