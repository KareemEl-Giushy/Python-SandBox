# ------------------------
# OOP in python
# Abstract Method (abc module) #
# ------------------------

from abc import ABCMeta, abstractmethod

class Programming(metaclass=ABCMeta):

    @abstractmethod
    def has_oop(self):
        pass
    
    def has_name(self):
        pass

class C(Programming):
    def has_oop(self):
        return "NO"

class Cpp(Programming):
    def has_oop(self):
        return "Yes"

class Csharp(Programming):
    def has_oop(self):
        return "Yes"

class Java(Programming):
    pass

class Python(Programming):
    def has_oop(self):
        return "Yes"

# lang = Programming() # Won't Wrok Becase it's just an abstract method here in the base (Estanba)

lang = Python()
print(lang.has_oop())

lang = Cpp()
print(lang.has_oop())

lang = C()
print(lang.has_oop())

# lang = Java() # the method is't there so it won't work you must put the method even if it's empty
