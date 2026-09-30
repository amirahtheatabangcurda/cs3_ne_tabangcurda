
class Plant:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage

    def attack(self, zombie):
        print(f"plant {self.name} attacks {zombie.name} and takes {self.damage} damage")
        zombie.take_damage(self.damage)
    

    def take_damage(self, amount):
        self.health -= amount
        if self.health < 0:
            self.health = 0
        print("{self.name} takes {amount} damage. Health is now {self.health}")

class Zombie:

    def __init__(self, name, health, damage, distance):
        self.name = name
        self.health = health
        self.damage = damage
        self.distance = distance

    def move(self):
        self.distance = -1
        print(f"{self.zombie} zombie is moving closer, distance:{self.distance}")

        
    def attack(self, plant):
        print(f"zombie{self.zombie} attacks{self. plant} and takes {self.damage} damage")
        plant.take_damage(self.damage)

    def take_damage(self, amount):
        self.health -= amount
        if self.health < 0:
            self.health = 0
        print("{self.name} takes {amount} damage. Health is now {self.health}")

plant1 = Plant("peashooter", 40,10)
plant2 = Plant("snowpea",25,5 )
zombie1 = Zombie("buckethead", 100, 15,5 )

print("mini plants VS zombies begin!")
print(f"defenders:{plant1.name} health: {plant1.health} & {plant2.name} health: {plant2.health}")
print(f"enemies: {zombie1.name} zombie  health: {zombie1.health} at a distance of{zombie1.distance} ")

turn = 1
while True:
    print("- - - TURN - - - ")
   
    if plant1.health > 0:
        plant1.attack(zombie1)
        if zombie1.health <= 0:
            break   

    if plant2.health > 0:
        plant2.attack(zombie1)
        if zombie1.health <= 0:
            break 

    if zombie1.distance > 0:
        Zombie.move()
    else:
       
        if plant1.health > 0:
            zombie1.attack(plant1)
        elif plant2.health > 0:
            zombie1.attack(plant2)
            
  
    print(f"[Status Check] {plant1.name}: {plant1.health} HP | {plant2.name}: {plant2.health} HP | {Zombie.name}: {Zombie.health} HP (Distance: {Zombie.distance})\n")
    
    if plant1.health <= 0 and plant2.health <= 0:
        break
        
    turn += 1


print("\n ------------ GAME OVER!!!!-------------")
if zombie1.health <= 0:
    print("The plants winn!! the path is now safe!")
else:
    print(" The zombies win, the defense broke down ")

print(f"Final State -> {plant1.name}: {plant1.health} HP | {plant2.name}: {plant2.health} HP | {Zombie.name}: {Zombie.health} HP")
print("________________________________________________________________")



        




