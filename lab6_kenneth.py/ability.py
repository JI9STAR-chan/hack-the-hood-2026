import random

class Ability:
    def __init__(self, name, max_damage):
        self.name = name
        self.max_damage = max_damage

    def attack(self):
        random_attack = random.randint(0, self.max_damage)
        print(random_attack)
        return random_attack


if __name__ == "__main__":
    ability_1 = Ability("shine with valor", 50)
    print(ability_1.name)
    print(ability_1.max_damage)
    ability_1.attack()