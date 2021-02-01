# ------------------------
# OOP in python 
# Encapsulation 
# Public - Protected - Private #
# ------------------------

class Member():
    def __init__(self, name):
        self._name = name
        self.__gender  = "male"

    def say_hello(h):
        return f"Hello Eng.{h._name}"
    def gender(self):
        return f"You Ara a {self.__gender}"

member1 = Member("kareem")

print(member1._name) # protected Attribute

print(member1._Member__gender) # private attribute

member1._name = 'kemoo'
print(member1._name)

print(member1.say_hello())
print(member1.gender())