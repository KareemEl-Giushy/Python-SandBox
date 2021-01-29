# ------------------------
# OOP in python 
# Class Methods And Static Methods#
# ------------------------

class Users:
    count = 0

    @classmethod
    def show_user_count(cls): # Class Method
        print(f"WE Have {cls.count} User(s) in our System")
    
    def __init__(self): # instance Method
        Users.count += 1

    @staticmethod
    def say_hello(): # Static Method
        print("Hello. It's Me")

kareem = Users()
ahmed = Users()
heba = Users()

kareem.show_user_count()
kareem.say_hello()