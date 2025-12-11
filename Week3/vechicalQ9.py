class vehicle:
    def __init__(self,brand,year):
        self.brand=brand
        self.year=year
    def info(self):
        return f"car brand: {self.brand} and year: {self.year}"


class car(vehicle):
    def __init__(self,brand, year, model):
       super().__init__(brand, year)
       self.model=model
    def info(self):
        return f"Car Brand: {self.brand}, Model: {self.model}, Year: {self.year}"
    

print("Testing Vehicle class:")
v1 = vehicle("Generic", 2010)
print(v1.info())

print("\nTesting Car class (with overridden info() method):")
c1 = car("Mercedes", 2004, "S-Class")
print(c1.info())

print("\nTesting polymorphism:")
vehicles = [vehicle("Ford", 2015), car("Toyota", 2020, "Camry")]
for vehicle in vehicles:
    print(vehicle.info())