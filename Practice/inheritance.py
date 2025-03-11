# class 10/03/25
class Veichle:
    def __init__(self, brand,model,year):
        self.brand = brand
        self.model = model
        self.year = year
        
    def display_info(self):
        print(f"{self.brand} {self.model} {self.year}")


class Car(Veichle):
    def __init__(self, brand,model,year, num_doors):
        super().__init__(brand, model, year)
        self.num_doors = num_doors
        
    def display_info(self):
        print(f"{self.brand} {self.model} {self.year} has {self.num_doors}")  
        
class Moto(Veichle):
    def __init__(self, brand,model,year, has_sidecar):
        super().__init__(brand, model, year)
        self.has_sidecar = has_sidecar
        
    def display_info(self):
        print(f"{self.brand} {self.model} {self.year} has {self.has_sidecar}")  
    
    
car1  = Car("Toyota", "Camry", 2025, 4)
mot1 = Moto("Harley", "Davidson", 2000, 0)

car1.display_info()
mot1.display_info()