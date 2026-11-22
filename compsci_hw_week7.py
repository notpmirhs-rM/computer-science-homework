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
        choice = input("(A)ttack or (S)earch for a weapon: ").strip().upper()
        if choice == "A":
            attacking.attack(defending)
        elif choice == "S":
            attacking.search_for_weapon()
        else:
            print("Invalid choice, you hesitated and lost your turn")
        attacking, defending = defending, attacking
    
Sword = Weapon("Sword", 25, 75)
Mace = Weapon("Mace", 40, 50)
Dagger = Weapon("Dagger", 15, 90)


#GAME START
P1_1 = input("Player 1 input your forename: ")
P1_2 = input("Player 1 input your surname: ")
P2_1 = input("Player 2 input your forename: ")
P2_2 = input("Player 2 input your surname: ")
    
player_1 = Character(P1_1, P1_2)
player_2 = Character(P2_1, P2_2)

battle(player_1, player_2)
