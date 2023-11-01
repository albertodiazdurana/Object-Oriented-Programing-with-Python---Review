from game_of_thrones_characters import JonSnow, DaenerysTargaryen, NightKing
import random

class BattleSimulator:
    def simulate_battle(self, character1, character2):
        while character1.isAlive() and character2.isAlive():
            # Character 1 attacks Character 2
            damage = character1.attack()
            character2.hit(damage)
            print(f"{character1.name} attacks {character2.name} for {damage} damage.")
            if not character2.isAlive():
                print(f"{character2.name} has been defeated!")
                break

            # Character 2 attacks Character 1
            damage = character2.attack()
            character1.hit(damage)
            print(f"{character2.name} attacks {character1.name} for {damage} damage.")
            if not character1.isAlive():
                print(f"{character1.name} has been defeated!")

        if character1.isAlive():
            print(f"{character1.name} is the winner!")
        else:
            print(f"{character2.name} is the winner!")

if __name__ == "__main__":
    jon_snow = JonSnow()
    daenerys = DaenerysTargaryen()
    night_king = NightKing()

    simulator = BattleSimulator()

    # Simulate a battle between two random characters
    character1 = random.choice([jon_snow, daenerys, night_king])
    character2 = random.choice([jon_snow, daenerys, night_king])
    while character1 == character2:
        character2 = random.choice([jon_snow, daenerys, night_king])

    simulator.simulate_battle(character1, character2)
