import random

class Contestant():
    def __init__(self, name = "Nameless"):
        self.name = name

    def set_soulmate(self, soulmate):
        self.soulmate = soulmate

class Game():
    def __init__(self):
        self.contestants = []
        self.perfect_pairs = set()

    def set_contestants(self, names):
        for name in names:
            self.contestants.append(Contestant(name))

    def set_perfect_pairs(self):
        for i in range(7):
            self.perfect_pairs.add((self.contestants.pop(0), self.contestants.pop(random.randint(0, len(self.perfect_pairs)))))
        #self.perfect_pairs.add(self.contestants[0], self.contestants[1])


names = ["Bob", "John", "Mary", "Rick", "Emma", "Ana", "Harry", "Meredith", "Perry", "Rita", "Derek", "Paula", "Arthur", "Peter", "Lina", "Samantha"]
game = Game()
game.set_contestants(names)
game.set_perfect_pairs()

for pair in game.perfect_pairs:
    print(pair)


print("Introducing our contestants: ")
for contestant in game.contestants:
    print(contestant.name)

