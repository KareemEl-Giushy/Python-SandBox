# ------------------------
# OOP in python
# Getters And Setters #
# ------------------------

class Member():

    def __init__(self):
        self.name = ""
        self.age = 0
        self.gender = ""

    def get_name(self):
        return self.name

    def set_name(self, val):
        self.name = val


kareem = Member()

print(kareem.get_name())
kareem.set_name('kareem')
print(kareem.get_name())
