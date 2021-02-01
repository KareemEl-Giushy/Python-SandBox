# ------------------------
# OOP in python 
# Inheritance#
# ------------------------

class Food: # Parent (Base Class)

    def __init__(self, name):
        self.name = name
        print(f"{self.name} Is Created From Base Class")

    @staticmethod
    def eat():
        print("Eating Food")

class Apple(Food): # Child (Derived Class)
    def __init__(self):
        print("This is crated From Apple Calss")

class orange(Food): # Child (Derived Class)
    def __init__(self, name):
        
        Food.__init__(self, name)
        
        # Better Way
        # super().__init__(name)

        print(f"This Print is from orange[{self.name}] class")

foody = Food("pizza")
foody_two = Apple()
foody_two.eat()

print("=" * 50)

foody_three = orange("orange")