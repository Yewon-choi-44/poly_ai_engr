class GameChar:
    strength = 10
    energy = 100

    def __init__(self, id, alias):
        self.id = id
        self.alias = alias

    def training(self):
        self.strength += 2

user1 = GameChar("user1", "user2")
user2 = GameChar("user2", "user2")
print(user1.__dict__)
print(user2.__dict__)

user1.training()
print(user1.__dict__)
print(user2.__dict__)

print(user1.strength, user2.strength)