import random

class Player:
    def __init__(self,email, name, gender, profession, level, exp, maxExp, maxHealth, currentHealth, maxMana, currentMana, attack, specialAttack, defense, healing, gold):
        self.email = email
        self.name = name
        self.gender = gender
        self.profession = profession
        self.level = level
        self.exp = exp
        self.maxExp = maxExp
        self.maxHealth = maxHealth
        self.currentHealth = currentHealth
        self.maxMana = maxMana
        self.currentMana = currentMana
        self.attack = attack
        self.specialAttackManaCost = 0
        self.specialAttack = specialAttack
        self.defense = defense
        self.healing = healing
        self.gold = gold
        self.inventory = []
        self.isAlive = True
    
    def getEmail(self):
        return self.email
        
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
    
    def getMaxExp(self):
        return self.maxExp
    
    def getMaxHealth(self):
        return self.maxHealth
    
    def getCurrentHealth(self):
        return self.currentHealth
    
    def getMaxMana(self):
        return self.maxMana
    
    def getCurrentMana(self):
        return self.currentMana
    
    def getAttack(self):
        return self.attack
    
    def getSpecialAttack(self):
        return self.specialAttack
    
    def getDefense(self):
        return self.defense
    
    def getHealing(self):
        return self.healing
    
    def getGold(self):
        return self.gold
    
    def getInventory(self):
        return self.inventory
            
    
    def getIsAlive(self):
        if(self.isAlive == True):
            return True
        return False
    
    def performAttack(self):
        damage = random.randint(0, self.attack)
        return damage
    
    def getSpecialAttackDamage(self):
        if self.currentMana >= self.specialAttackManaCost:
            self.currentMana -= self.specialAttackManaCost
            damage = random.randint(0, self.specialAttack)
            print(f"currentMana after special attack: {self.currentMana}")
            return damage
        else:
            return None
    
    def setExp(self, newExp):
        self.exp += newExp
        if self.exp >= self.maxExp:
            self.exp -= self.maxExp
            self.levelUp(1)
            
    def levelUp(self, levelUp):
        self.level += levelUp
        print(f"You have advanced from level {self.level - 1} to {self.level}")
        #Calling function to increase attributes after level up
        self.attributesIncrease(self.getProfession())
    
    def attributesIncrease(self,profession):
        match(profession):
            case "Paladin":
                self.maxExp *= 1.5
                self.maxHealth += 30
                self.maxMana += 15
                self.attack += 20
                self.specialAttack += 30
                self.defense += 15
                self.healing += 7
                return "Stats have been increased"
            case "Knight":
                self.maxExp *= 1.5
                self.maxHealth += 40
                self.maxMana += 5
                self.attack += 25
                self.specialAttack += 35
                self.defense += 20
                self.healing += 5
                return "Stats have been increased"
            case "Sorcerer":
                self.maxExp *= 1.5
                self.maxHealth += 5
                self.maxMana += 15
                self.attack += 10
                self.specialAttack += 50
                self.defense += 5
                self.healing += 15
                return "Stats have been increased"
            case "Druid":
                self.maxExp *= 1.5
                self.maxHealth += 5
                self.maxMana += 15
                self.attack += 10
                self.specialAttack += 40
                self.defense += 5
                self.healing += 17
                return "Stats have been increased"

class Knight(Player):
    def __init__(self,email, name, gender, profession, level, exp, maxExp, maxHealth, currentHealth,maxMana, currentMana, attack, specialAttack, defense, healing, gold):
        super().__init__(email,name, gender, "Knight",level, exp, maxExp, maxHealth, currentHealth,maxMana, currentMana, attack, specialAttack, defense, healing, gold)
        self.specialAttackManaCost = 30
    
    def heal(self):
        if self.currentMana > 10:
            self.currentMana -= 10
            self.currentHealth += self.healing
        else:
            return f"Sorry, your current Mana is: {self.currentMana} and it is too low"

class Paladin(Player):
    def __init__(self,email, name, gender, profession, level, exp, maxExp, maxHealth, currentHealth,maxMana, currentMana, attack, specialAttack, defense, healing, gold):
        super().__init__(email,name, gender, "Paladin", level, exp, maxExp, maxHealth, currentHealth,maxMana, currentMana, attack, specialAttack, defense, healing, gold)
        self.specialAttackManaCost = 25
    
    
    def heal(self):
        if self.currentMana > 10:
            self.currentMana -= 10
            self.currentHealth += self.healing
        else:
            return f"Sorry, your current Mana is: {self.currentMana} and it is too low"
        

class Druid(Player):
    def __init__(self, email, name, gender, profesison, level, exp, maxExp, maxHealth, currentHealth, maxMana, currentMana, attack, specialAttack, defense, healing, gold):
        super().__init__(email, name, gender, "Druid", level, exp, maxExp, maxHealth, currentHealth, maxMana, currentMana, attack, specialAttack, defense, healing, gold)
        self.specialAttackManaCost = 45
    
    def heal(self):
        if self.currentMana > 10:
            self.currentMana -= 10
            self.currentHealth += self.healing
        else:
            return f"Sorry, your current Mana is: {self.currentMana} and it is too low"

class Sorcerer(Player):
    def __init__(self, email, name, gender, profession, level, exp, maxExp, maxHealth, currentHealth,maxMana, currentMana, attack, specialAttack, defense, healing, gold):
        super().__init__(email, name, gender, "Sorcerer", level, exp, maxExp, maxHealth, currentHealth, maxMana, currentMana, attack, specialAttack, defense, healing, gold)
        self.specialAttackManaCost = 50
    
    def heal(self):
        if self.currentMana > 10:
            self.currentMana -= 10
            self.currentHealth += self.healing
        else:
            return f"Sorry, your current Mana is: {self.currentMana} and it is too low"