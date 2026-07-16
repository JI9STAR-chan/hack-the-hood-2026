import random
from ability import Ability
from armour import Armor
from weapons import Weapon

class Hero:
    def __init__(self, name, starting_health=100):
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
        self.abilities = []
        self.armors = []
    
    def battle(self, opponent):
        my_list = [self.name, opponent.name]
        print(random.choice(my_list))
        
        if len(self.abilities) == 0 or len(opponent.abilities) == 0:
            print("Draw")
        return

        while self.is_alive() and opponent.is_alive():
            opponent.take_damage(self.attack())

        if not opponent.is_alive():
            print(f"{self.name} won!")
    

        self.take_damage(opponent.attack())

        if not self.is_alive():
            print(f"{opponent.name} won!")
        


    def add_ability(self, ability):
        self.abilities.append(ability)


    def attack(self):
        total_damage = 0
        for ability in self.abilities:
            total_damage += ability.attack()
        print(total_damage)
        return total_damage


    def add_armor(self, armor):
        self.armors.append(armor)

    def add_weapon(self, weapon):
        self.abilities.append(weapon)


    def defend(self):
        total_block = 0
        for armor in self.armors:
            total_block += armor.block()
        print(total_block)
        return total_block


    def take_damage(self, damage):
        total_block = self.defend()
        actual_damage = damage - total_block
        self.current_health -= actual_damage
        actual_damage = max(damage - total_block, 0)
        self.current_health -= actual_damage
        if self.current_health < 0:
            self.current_health = 0
        print(self.current_health)
        return actual_damage

if __name__ == "__main__":
    my_hero = Hero("phainon", 150)
    print(my_hero.name)
    print(my_hero.current_health)
    my_opponent = Hero("nanook", 200)
    my_hero.battle(my_opponent)
    my_hero.add_ability(Ability("Beginning of the end", 50))
    my_hero.add_ability(Ability("stride to deliverance", 30))
    my_hero.add_ability(Ability("pyric corpus", 20))
    my_hero.attack()
    my_hero.add_armor(Armor("winged helm", 50))
    my_hero.add_armor(Armor("shield of the ancients", 30))
    my_hero.add_armor(Armor("breastplate of the gods", 20))
    my_hero.defend()
    my_hero.take_damage(30)
    my_hero.add_weapon(Weapon("sword of the ancients", 50))
    my_hero.add_weapon(Weapon("sword of the gods", 30))