import random

class Character:
    def __init__(self, forename, surname):
        self.forename = forename
        self.surname = surname
        self.hp = 100      #Health points
        self.dmg = 10      #Damage
        self.hr = 100
    
    def stats(self):
        print(self.forename, self.surname)
        print("HP:", self.hp)
        print("DMG: ", self.dmg)
        print("Hit rate:", self.hr)
    
    def attack (self, enemy): #subtract dmg dealt from enemy hp
        roll = random.randint(1, 100)
        if roll <= self.hr:
            enemy.hp -= self.dmg
            print(f"{self.forename} {self.surname} attacks {enemy.forename} {enemy.surname}")
            enemy.stats()
            if enemy.hp <= 0:
                print(enemy.forename, enemy.surname, "was defeated")
                print(self.forename, self.surname, "has won the battle!")
        else:
            print(self.forename, self.surname, "missed!")
    
    def search_for_weapon(self):
        loot_available = [Sword, Mace, Dagger, None]
        found_item = random.choice(loot_available)
        
        if found_item != None:
            self.dmg = found_item.dmg
            self.hr = found_item.hr
            print(f"{self.forename} {self.surname} found a {found_item.name}!")
            self.stats()
        else:
            print(f"{self.forename} {self.surname} searched but found nothing!")

class Weapon:
    def __init__(self, name, dmg, hit_rate):
        self.name = name
        self.dmg = dmg
        self.hr = hit_rate
    
Sword = Weapon("Sword", 25, 75)
Mace = Weapon("Mace", 40, 50)
Dagger = Weapon("Dagger", 15, 90)
