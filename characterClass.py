import random

class Player:
    def __init__(self, name, gender, profession, level, exp, maxHealth, currentHealth, mana, attack, specialAttack, defense, healing):
        self.name = name
        self.gender = gender
        self.profession = profession
        self.level = level
        self.exp = exp
        self.maxHealth = maxHealth
        self.currentHealth = currentHealth
        self.mana = mana
        self.attack = attack
        self.specialAttack = specialAttack
        self.defense = defense
        self.healing = healing
        
    def getName(self):
        return self.name
    
    def getGender(self):
        return self.gender
    
    def getProfession(self):
        return self.profession
    
    def getLevel(self):
        return self.level
    
    def getExp(self):
        return self.exp
    
    def getMaxHealth(self):
        return self.maxHealth
    
    def getCurrentHealth(self):
        return self.currentHealth
    
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
    
    def setExp(self, newExp):
        self.exp += newExp
        if self.exp > 100:
            self.exp -= 100
            self.levelUp(1)
            
    def levelUp(self, levelUp):
        self.level += levelUp
        #Calling function to increase attributes after level up
        self.attributesIncrease(self.getProfession)
    
    def attributesIncrease(self,profession):
        match(profession):
            case "Paladin":
                self.maxHealth += 30
                self.mana += 15
                self.attack += 20
                self.specialAttack += 30
                self.defense += 15
                self.healing += 7
                return "Stats have been increased"
            case "Knight":
                self.maxHealth += 40
                self.mana += 5
                self.attack += 25
                self.specialAttack += 35
                self.defense += 20
                self.healing += 5
                return "Stats have been increased"
            case "Sorcerer":
                self.maxHealth += 5
                self.mana += 15
                self.attack += 10
                self.specialAttack += 50
                self.defense += 5
                self.healing += 15
                return "Stats have been increased"
            case "Druid":
                self.maxHealth += 5
                self.mana += 15
                self.attack += 10
                self.specialAttack += 40
                self.defense += 5
                self.healing += 17
                return "Stats have been increased"

class Knight(Player):
    def __init__(self, name, gender,level, exp, maxHealth, currentHealth, mana, attack, specialAttack, defense, healing):
        super().__init__(name, gender, "Knight",level, exp, maxHealth, currentHealth, mana, attack, specialAttack, defense, healing)
        
    def attack(self):
        damage = random.randint(0, self.attack)
        return damage
    
    def specialAttack(self):
        if self.mana > 30:
            self.mana -= 30
            damage = random.randint(0, self.specialAttack)
            return damage
        else:
            return f"Sorry, your current mana is: {self.mana} and it is too low"
    
    def heal(self):
        if self.mana > 10:
            self.mana -= 10
            self.health += self.healing
        else:
            return f"Sorry, your current mana is: {self.mana} and it is too low"

class Paladin(Player):
    def __init__(self, name, gender, level, exp, maxHealth, currentHealth, mana, attack, specialAttack, defense, healing):
        super().__init__(name, gender, "Paladin", level, exp, maxHealth, currentHealth, mana, attack, specialAttack, defense, healing)
    
    def attack(self):
        damage = random.randint(0, self.attack)
        return damage
    
    def specialAttack(self):
        if self.mana > 25:
            self.mana -= 25
            damage = random.randint(0, self.specialAttack)
            return damage
        else:
            return f"Sorry, your current mana is: {self.mana} and it is too low"
    
    def heal(self):
        if self.mana > 10:
            self.mana -= 10
            self.health += self.healing
        else:
            return f"Sorry, your current mana is: {self.mana} and it is too low"
        

class Druid(Player):
    def __init__(self, name, gender, level, exp, maxHealth, currentHealth, mana, attack, specialAttack, defense, healing):
        super().__init__(name, gender, "Druid", level, exp, maxHealth, currentHealth, mana, attack, specialAttack, defense, healing)
    
    def attack(self):
        damage = random.randint(0, self.attack)
        return damage
    
    def specialAttack(self):
        if self.mana > 45:
            self.mana -= 45
            damage = random.randint(0, self.specialAttack)
            return damage
        else:
            return f"Sorry, your current mana is: {self.mana} and it is too low"
    
    def heal(self):
        if self.mana > 10:
            self.mana -= 10
            self.health += self.healing
        else:
            return f"Sorry, your current mana is: {self.mana} and it is too low"

class Sorcerer(Player):
    def __init__(self, name, gender, level, exp, maxHealth, currentHealth, mana, attack, specialAttack, defense, healing):
        super().__init__(name, gender, "Sorcerer", level, exp, maxHealth, currentHealth, mana, attack, specialAttack, defense, healing)
        
    def attack(self):
        damage = random.randint(0, self.attack)
        return damage
    
    def specialAttack(self):
        if self.mana > 50:
            self.mana -= 50
            damage = random.randint(0, self.specialAttack)
            return damage
        else:
            return f"Sorry, your current mana is: {self.mana} and it is too low"
    
    def heal(self):
        if self.mana > 10:
            self.mana -= 10
            self.health += self.healing
        else:
            return f"Sorry, your current mana is: {self.mana} and it is too low"