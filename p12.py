class GameCharacter:
        
    def __init__(self, name, pos, health):
        self.name = name
        self.pos = pos
        self.health = health

    def move (self, by_amount):
        self.pos += by_amount

character = GameCharacter("Anton", 5, 100)

print(character.name)
character.health = 120
print(character.health)
character.move(10)
print(character.pos)

