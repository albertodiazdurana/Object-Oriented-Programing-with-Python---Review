class GameOfThronesCharacter:
    def __init__(self, name, strength, health):
        self.name = name
        self.strength = strength
        self.health = health

    def attack(self):
        return self.strength

    def hit(self, points):
        self.health -= points

    def isAlive(self):
        return self.health > 0

    def print(self):
        print(f"Name: {self.name}, Class: {self.__class__.__name__}, Strength: {self.strength}, Health: {self.health}")


class JonSnow(GameOfThronesCharacter):
    def __init__(self):
        super().__init("Jon Snow", 10, 100)


class DaenerysTargaryen(GameOfThronesCharacter):
    def __init__(self):
        super().__init("Daenerys Targaryen", 8, 120)


class NightKing(GameOfThronesCharacter):
    def __init__(self):
        super().__init("Night King", 15, 150)
