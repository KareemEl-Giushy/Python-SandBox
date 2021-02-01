# ------------------------
# OOP in python 
# Multipule Inheritance #
# ------------------------

class BaseOne:
    def __init__(self):
        print("this is from base one. Negar")
    @staticmethod
    def make():
        print("this make is from base one")
    def bla(self):
        print("hello")
class BaseTwo:
    def __init__(self):
        print("this is from base two")
    def blasy(self):
        print("Helooyya")

class Derived(BaseOne, BaseTwo):
    @staticmethod
    def make():
        print("Modified")
        

cally = Derived()

cally.make()
cally.bla()
cally.blasy()