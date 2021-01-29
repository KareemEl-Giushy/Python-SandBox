# ------------------------
# OOP in python #
# ------------------------

class Kareem:
    
    NotAllowedNames = ["Shit", "Fuck", "Hell", "Hamada"]
    kareem_num = 0

    def __init__(self, f = "Kareem", m = "El-Giushy", l = "El-Meghawry"): #instance Method
        self.fname = f
        self.mname = m
        self.lname = l
        self.height = 170
        self.weight = 80
        self.hairColor = "Black"
        Kareem.kareem_num += 1

    def FullName(self): #instance Method
        if not self.fname in Kareem.NotAllowedNames:
            return f"{self.fname} {self.mname} {self.lname}"
        else:
            raise ValueError("Are You Fucking Kidding Me ??")
    
    def NamewithTitle(self, gender = ""): #instance Method
        if gender.lower() == "female" or gender.lower() == "f":
            return f"Hello Ms.{self.FullName()}"
        else:
            return f"Hello Mr.{self.FullName()}"

    def DeleteUser(self): #instance Method
        kareem_num -= 1

k = Kareem("Fucky")

# print(dir(Kareem()))
# print("=" * 50)
# print(dir(k))

# print(k.fname)
# print(k.height)
# print(k.hairColor)
print(k.FullName())
print(k.NamewithTitle("f"))   