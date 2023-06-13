class Car:
    def __init__(self):
        self.make = "Tayota"
        self.model = "Camri"
        self.year = 124
        self.mileage = 0
        
    def drive(self, distance):
        self.mileage += distance
    
    def get_mileage(self):
        return self.mileage
    
c = Car()

c.drive(31)
print(c.get_mileage())