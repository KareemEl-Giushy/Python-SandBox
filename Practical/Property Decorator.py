# ------------------------
# OOP in python
# Property Decorator #
# ------------------------

class User():
    def __init__(self):
        self.age = 18

    @property
    def age_in_days(self):
        print(self.age)
        return self.age * 365.25


kareem = User()

# kareem.age_in_days() # not Working any more Because we made it a property

kareem.age_in_days