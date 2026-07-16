import random

class Team:
    def __init__(self, name):
        self.name = name
        self.heroes = []

    def add_hero(self, hero):
        self.heroes.append(hero)

    def remove_hero(self, name):
        for hero in self.heroes:
            if hero.name == name:
                self.heroes.remove(hero)
                return

    def view_all_heroes(self):
        for hero in self.heroes:
            print(hero.name)

    def statistics(self):
        total_kills = 0
        total_deaths = 0

        for hero in self.heroes:
            total_kills += hero.kills
            total_deaths += hero.deaths

        print(f"Team: {self.name}")
        print(f"Kills: {total_kills}")
        print(f"Deaths: {total_deaths}")

    def attack(self, other_team):
        living_heroes = [hero for hero in self.heroes if hero.is_alive()]
        living_opponents = [hero for hero in other_team.heroes if hero.is_alive()]
    
    while living_heroes and living_opponents:
        hero = random.choice(living_heroes)
        opponent = random.choice(living_opponents)

        hero.fight(opponent)

        living_heroes = [
            hero for hero in self.heroes if hero.is_alive()
        ]
        living_opponents = [
            hero for hero in other_team.heroes if hero.is_alive()
        ]

    def revive_heroes(self):
        for hero in self.heroes:
            hero.current_health = hero.starting_health

