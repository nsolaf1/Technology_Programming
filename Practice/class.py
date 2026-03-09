# class Person:
#   def __init__(self, name, age,gender):
#     self.name = name
#     self.age = age
#     self.gender = gender
  
#   def greet(self):
#     print(f"hello {self.name}, you age is {self.age} and you are {self.gender}")

# p1 = Person("John", 36, 0)
# p2 = Person("123", 36, 0)

# # print(p1.name)
# # print(p1.age)
# # print(p1.gender)

# p1.greet()
# p2.greet()


class Car():
  def __init__(self, color, brand, speed):
    self.color = color
    self.brand = brand
    self.speed = speed
    
  def start(self):
    print(f"your {self.color} car has started")
  
  def stop(self):
    print(f"your {self.brand} with color {self.color} car has Stopped")
  
  def speed1(self):
    print(f"your speed is {self.speed}")
  
    
bmw = Car("red", "X9", 999)

bmw.start()
bmw.stop()
bmw.speed1()
    




