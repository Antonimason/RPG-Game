import random

class Enemy:
    def __init__(self, name, exp, currentHealth, maxHeatlh, attack, specialAttack, defense, healing, gold):
        self.name = name
        self.exp = exp
        self.currentHealth = currentHealth
        self.maxHeatlh = maxHeatlh
        self.attack = attack
        self.specialAttack = specialAttack
        self.defense = defense
        self.healing = healing
        self.gold = gold
        
    def getName(self):
        return self.name
    
    def getExp(self):
        return self.exp
    
    def getCurrentHealth(self):
        return self.currentHealth
    
    def getmaxHeatlh(self):
        return self.maxHeatlh
    
    def getAttack(self):
        return self.attack
    
    def getSpecialAttack(self):
        return self.specialAttack
    
    def getDefense(self):
        return self.defense
    
    def getHealing(self):
        return self.healing
    
    def getGold(self):
        reward = random.randint(0, self.gold)
        return reward
    
    def performAttack(self):
        damage = random.randint(0, self.attack)
        return damage
    
    def performSpecialAttack(self):
        damage = random.randint(0, self.specialAttack)
        return damage
    
    def performHealing(self):
        heal = random.randint(0, self.healing)
        self.currentHealth += heal
    
class Rat(Enemy):
    def __init__(self):
        super().__init__("Rat", exp=10, currentHealth=50, maxHeatlh=50, attack=5, specialAttack=8, defense=2, healing=0, gold=10)

class Dog(Enemy):
    def __init__(self):
        super().__init__("Dog", exp=20, currentHealth=70, maxHeatlh=70, attack=10, specialAttack=20, defense=5, healing=0, gold = 20)

class Elf(Enemy):
    def __init__(self):
        super().__init__("Elf", exp=40, currentHealth=120, maxHeatlh=120, attack=15, specialAttack=30, defense=10, healing=20, gold = 40)

class Soldier(Enemy):
    def __init__(self):
        super().__init__("Soldier", exp=70, currentHealth=170, maxHeatlh=170, attack=25, specialAttack=42, defense=15, healing=25, gold = 60)

class Orc(Enemy):
    def __init__(self):
        super().__init__("Orc", exp=100, currentHealth=250, maxHeatlh=250, attack=30, specialAttack=50, defense=20, healing=30, gold = 80)

class Dragon(Enemy):
    def __init__(self):
        super().__init__("Dragon", exp=300, currentHealth=500, maxHeatlh=500, attack=100, specialAttack=230, defense=30, healing=70, gold = 400)

class Hydra(Enemy):
    def __init__(self):
        super().__init__("Hydra", exp=500, currentHealth=650, maxHeatlh=650, attack=130, specialAttack=320, defense=25, healing=100, gold = 600)

class Demon(Enemy):
    def __init__(self):
        super().__init__("Demon", exp=800, currentHealth=1000, maxHeatlh=1000, attack=200, specialAttack=400, defense=300, healing=120, gold = 1000)