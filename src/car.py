# src/car.py

class Car:
    """Represents a car with a make, model, and year."""
    
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def display_info(self):
        """Prints out the car's information."""
        print(f"Car: {self.year} {self.make} {self.model}")
