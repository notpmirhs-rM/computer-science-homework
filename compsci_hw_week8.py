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
        weapons_available = [Sword, Mace, Dagger, Whip, None]
        found_weapon = random.choice(weapons_available)
        
        if found_weapon != None:
            self.dmg = found_weapon.dmg
            self.hr = found_weapon.hr
            print(f"{self.forename} {self.surname} found a {found_weapon.name}!")
            self.stats()
        else:
            print(f"{self.forename} {self.surname} searched but found nothing!")

    def search_for_item(self):
        roll = random.randint(1,100)
        if roll <= 10:
            item_found = Super_Health_Potion
            print("Received: ", item_found.name)
            if self.hp < 100:
                self.hp = min(self.hp + item_found.heal_amount, 100)
            self.stats()
        elif roll <= 40:
            item_found = Health_Potion
            print("Received: ", item_found.name)
            if self.hp < 100:
                self.hp = min(self.hp + item_found.heal_amount, 100)
            self.stats()
        elif roll <= 70:
            item_found = Damage_Potion
            print("Received: ", item_found.name)
            self.dmg *= item_found.damage_boost
            self.stats()

        else:
            print("Received: Nothing")

class Item:
    def __init__(self, name):
            self.name = name

class Heal(Item):
    def __init__(self, name, heal_amount):
        super().__init__(name)
        self.heal_amount = heal_amount

class DamageBoost(Item):
    def __init__(self, name, damage_boost):
            super().__init__(name)
            self.damage_boost = damage_boost

Health_Potion = Heal("Health Potion", 15)
Super_Health_Potion = Heal("Super Health Potion", 30)
Damage_Potion = DamageBoost("Damage Boost Potion", 1.1)

class Weapon:
    def __init__(self, name, dmg, hit_rate):
        self.name = name
        self.dmg = dmg
        self.hr = hit_rate

def battle(player_1, player_2):
    turn = 1
    attacking = player_1
    defending = player_2
    print("----------------")
    print("Battle... START!")
    print("----------------")
    player_1.stats
    player_2.stats
    
    while player_1.hp > 0 and player_2.hp > 0:
        choice = input("(A)ttack, Search for a (W)eapon:, or Search for an (I)tem: ").strip().upper()
        if choice == "A":
            attacking.attack(defending)
        elif choice == "W":
            attacking.search_for_weapon()
        elif choice == "I":
            attacking.search_for_item()
        else:
            print("Invalid choice, you hesitated and lost your turn")
        print(f"{defending.forename} {defending.surname}'s turn")
        attacking, defending = defending, attacking
    
Sword = Weapon("Sword", 25, 75)
Mace = Weapon("Mace", 40, 50)
Dagger = Weapon("Dagger", 15, 90)
Whip = Weapon("Whip", 20, 80)

#GAME START
P1_1 = input("Player 1 input your forename: ")
P1_2 = input("Player 1 input your surname: ")
P2_1 = input("Player 2 input your forename: ")
P2_2 = input("Player 2 input your surname: ")
    
player_1 = Character(P1_1, P1_2)
player_2 = Character(P2_1, P2_2)

battle(player_1, player_2)
