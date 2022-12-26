class Car:
    def __init__(self,brand,year):
        self.brand = brand
        self.year = year
    def __str__(self):
        return f"{self.brand},{self.year}"

Mcar = Car("Mercedes","2020")
print(Mcar)
