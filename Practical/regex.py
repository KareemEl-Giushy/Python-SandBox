# ------------------------
# Regex in python #
# ------------------------
import re

mystring = re.search(r"[A-Z]", "KKKareem El-Giushy")
print(mystring)
# print(dir(mystring))
print(mystring.span())
print(mystring.string)
print(mystring.re)
print(*mystring.regs)
print(mystring.group())


print("=" * 50)

mystring = re.findall(r"[A-Z]","Kareem El-Giushy")
print(mystring)
# print(dir(mystring))

print("=" * 50)

emailregex = re.search(r"[A-z0-9\.]+@[A-z0-9]+\.(com|net|info|ru)", "kareem.64123 @gmail.com")
print(True if emailregex else False)
# print(emailregex.string)
# print(emailregex.span())
# print(emailregex.group())

print("=" * 50)
inemail = input("Please, Enter Your Email: ").strip()
emailregex = re.findall(r"[A-z0-9\.]+@[A-z0-9]+\.com|net|info|ru", inemail)
print(emailregex)