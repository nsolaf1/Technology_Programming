class Car:
    wheels = 4
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color
    
    def drive(self):
        print(f"{self.brand} is {self.color} and is Driving")
    
    def get_wheels(self):
          print(f"this car car {self.wheels} wheels")
    
    @staticmethod
    def car_info():
        print("Cars are the transportation system")
    
    
lambo = Car("Lamborghini", "Yellow")
mycar = Car("Honda", "red")
mycar1 = Car("Ford", "BLACK")


lambo.drive()
lambo.get_wheels()

mycar.drive()
mycar1.drive()
mycar1.get_wheels()
mycar1.get_wheels()
mycar1.car_info()




