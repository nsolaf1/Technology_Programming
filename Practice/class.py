class Character:
    def __init__(self, health, damage, speed):
        self.health = health
        self.damage = damage
        self.speed = speed

    # def __str__(self):
    #     return f'{self.health} {self.damage} {self.speed}'

    def double_speed(self):
        self.speed *= 2


warrior = Character(100, 50, 20)
ninja = Character(70, 30, 40)

print(warrior.speed)
print(ninja.speed)

warrior.double_speed()

print(f" Warrior New Speed {warrior.speed}")

