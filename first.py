# ------------
# type()
# All data in python are objects
# ------------

print(type(10)) # Integer

print(type(1.4)) # Float ( Floating-Point )

print(type("kareem")) # String

print(type(True)) # Boolean

print(type( [1, 2, 4, 5, 6] )) # List (An Array But not really)

print(type( (1, 2, 4, 5, 6, 7) )) # Tuple

print(type( {'One': 1, "Two": 2, "Three": 3} )) # dict => Dictionary

# -------------
#
# Variables In Python
#
# -------------

variable = 5

var = "kareem"

_hamada = "hamda"

hamada2 = "ya Hamada"

# Name != name
# reserved words
# help("keywords")

# mulit variables
a, b, c = 1, 2, 3
print(a)
print(b)
print(c)
# -------------
# Escape Sequances & Characters
# \b => Back Espase
# \newline => Escape newline + \ 
# \ => Escape Backslash
# \ => Escape Single And Double Quotes
# \n => Make newline (line feed)
# \r => carrage return
# \t => Horizontal Tab
# \x(hh) => Character Hexa Desimal Code Value
# #
# -------------

print("kareem\b\b El-Giushy")

print("kareem\
El-Giushy\
\El-Meghawry")

print("kareem \\ El-Giushy")

print("Kareem \"\
    Kemoo\"")

print('Ahmed \'Abdlewaheed\'')

print('output1\noutput2\noutput3')

print("1234567\rABCD") # 1234 => ABCD (ABCD567)

print("I Love\tPython")

print("\x4b\x41\x52\x45\x45\x4d")

# -------------
#
# Concatination IN Python
#
# -------------

var1 = "Kareem"
var2 = "salem"
print(var1 + ' ' + var2)

full = var1 + " " + var2
print(full)

# -------------
# Strings IN Python#
# -------------

# Multi Line String
myVariable = """Hello
Word "Test"
This 'Test'
is "'Testy'"
kareem"""
print(myVariable)


# String Indexing (Access Single Item)
myName = "I Love Python"
print(myName[0])
print(myName[-1]) # First element from the last => m

# Slicing (Access Multiple Sequencial Items)
# [start:end] End Not Included in output
# [start:end:steps]

print(myName[8:10]) # yt
print(myName[8:11]) # yth

print(myName[:10]) # if start not included it starts form 0
print(myName[10:]) # if End not Included it goes to the end index

print(myName[:]) # Full String Output
print(myName[0::1]) # Full String Output
print(myName[::1]) # Full String Output

# Steps Examples
print(myName[::2]) # Ilv yhn (Skip 1 Charachters And Get The Next)
print(myName[::3]) # Io tn (Skip 2 Characters And Get The Third)

# -------------
# String Methods In Python
# len() => String Length
# st#
# -------------

# len()
a = "I love Python So Much"
b = "     I love Python So Much   "
print(len(a))
print(len(b))

# strip() rstrip() lstrip() >> Strip Spaces by defualt " "
print(b.strip())
print(b.rstrip())
print(b.lstrip())

b = "####kare#em#####"
print(b.strip("#"))

# title() Capitalize the string and the letters after numbers
a = "python for beginners 101A"
print(a.title())

# Capitalize() Just Capitalizes The String
print(a.capitalize())

# zfill(<int Width>)
# 001
# 002
# 003
# 004
# 005
# 010
# 101
# 444

a, b, c, d = '1', '11', '111', '1111'
print(a)
print(b)
print(c)
print(d)
print(a.zfill(3))
print(b.zfill(3))
print(c.zfill(3))
print(d.zfill(3))


# upper() => UpperCase String
name = 'kareem elgiushy'
print(name.upper())

# lower() => lowerCase String
name = "KEMOO"
print(name.lower())

# splite() | rsplite() >> Splites the elements and make a list by default " "
a = "I Use Python In AI"
print(a.split())

b = "I#us#e#python#In#aI"
print(b.title().split("#"))

c = "I-Love-Python-I-am-a-Python-Developer"
print(c.title().split("-", 2))
print(c.title().rsplit("-", 2))

c="python-and-php-and-js-and-sql"
print(c.upper().split("-AND-"))


# center()
e="kareem"
print(e.center(9)) # kareem 6 chanracter 9-6 => 3 | 2 kareem 1
print(e.center(2, "#"))
print(e.center(8, "#")) # kareem 8 chanracter 8-6 => 2 | 1 kareem 1

# count(<sting>search, <int>start, <int>End) >> counts how many times the word existed
a = "I love python because python is easy"
print(a.count("python", 0, 25)) # from index 0 to index 25

# swapcase()
g = "I love python"
h = "i love pyThon"
print(g.swapcase())
print(h.swapcase())

# startwith(<string>search, <int>start, <int>end) what character does the string begin with
a = "kareem"
print(a.startswith("I"))
print(a.startswith("K"))
print(a.startswith("k"))
print(a.startswith("e", 3, 6))

# endswith()
print(a.endswith("m"))
print(a.endswith("r", 0, 2))

# index()
a = "I Love Python & PHP"
print(a.index("P"))
# print(a.index("p")) # Error Because Not Found
print(a.index("P", 0, 9))
# print(a.index("P", 0, 5)) # Error Because Not Found

print("-------------------")
#find()
print(a.find("P"))
print(a.find("P", 0, 9))
print(a.find("P", 0, 5)) # No Error But Gives -1

# rjust() ljust() Like center() But From only one side >> width + fill Character
c = "kareem"
print(c.rjust(10, "#"))
print(c.ljust(10, "#"))

# splitlines() >> Just like split but for lines
c = """

Kareem
El-Giushy
El-Meghawry

"""
print(c.split())
print(c.splitlines())

# expandtabs() >> How Many Tabs
a = "Hello\tworld\tfrom\tPython\t"
print(a)
print(a.title().expandtabs(2)) # >> Make The Tabs Just 2


# Checking
# istitle()
x = "Kareem El-Giushy"
y = "Kareem El-Giushy 3g"
print(x.istitle())
print(y.istitle())

print("-------------------")
# isspace()
x = ' '
y = ""
print(x.isspace())
print(y.isspace())

print("-------------------")
# islower()
x = "kareem"
y = "Kareem"
print(x.islower())
print(y.islower())

print("-------------------")
# isidentifier() >> takes a string and check if that string can be a variable name or not
var1 = "Kareem_Salem"
var2 = "kareem-salem"
var3 = "kareem123"
var4 = "kar23m"
var5 = "11kar23m"
var6 = "$kar23m"

print(var1.isidentifier())
print(var2.isidentifier())
print(var3.isidentifier())
print(var4.isidentifier())
print(var5.isidentifier())
print(var6.isidentifier())

print("-------------------")
# isalpha() >> checks just the alphapitical order
x = "AAAAAAAAaaaaBBBbbb"
print(x.isalpha())

# isalnum() >> checks the alaphapitical order and the num order
x = "AAAAAAAAaaBBBBCCC123"
print(x.isalnum())

print("-------------------")
# replace(Old Value, New Value, Count)
x = "I Love Python, Because Python Is Easy"
print(x)
print(x.replace("Python", "PHP"))
print(x.replace("Python", "PHP", 2))
print(x.replace("Python", "PHP", 1))

print("-------------------")
# separetor.join(Iterable) >> Iterable >> tuple and list
listy = ["kareem", "el-giushy", 'el-meghawry']
print("".join(listy))
print(" ".join(listy).title())
print("-".join(listy).title())
print("\t".join(listy).expandtabs(4).title())


# ------------------------
# ------------------------
# ----String Formating---- 
# ------------------------
# ------------------------

name = "kareem"
age = 18

# print("my name is ".title() + name + " and i'm ".capitatize() + age) # Types Error Can't Concate String With number
print("my name is %s and I'm %d" % (name, age))

# %s => String 
# %d => Digits
# %f => Float #

# Truncate String
# %.(How Many Characters)s
# Control Floating Points
# %.(How Many Floating Numbers)f

print("my name is %.3s and I'm %0.2f" % (name, age))

# ------------------------
# ------------------------
# ----String Formating---- 
# ------New Method--------
# ------------------------
name = "Kareem"
age = 18
rank = 10

print("My Name Is {}".format(name))
print("My name is {} and My age is {} : rank {}".format(name, age, rank))
print("My name is {:s} and My age is {:d} : rank {:f}".format(name, age, rank))

money = 154156415151564123
print("My Money: %d" % money)
print("My Money: {:_}".format(money))
print("My Money: {:,d}".format(money))
print("My Money: {:#d}".format(money))

a,b,c = "One", "Two", 3
print("Hello {0:s} {2:d} {1}".format(a,b,c))
print("Hello {0} {1} {2:f}".format(a,b,c))

# format in version 3.6+
print("My name is : {name} and my age is : {age}")
print(f"My name is : {name} and my age is : {age}")

# Complex Numbers
print(type(3+5j))

comp = 5+3j

print("Real Number: {}".format(comp.real))
print("Real Number: {}".format(comp.imag))
print(100)
print(float(100))
print(complex(100))

# ------------------------
# Lists #
# ------------------------

mylist = ['one', 'two', 'three', 'one', 'four', True, 2, 3.4, (1,2), [1,2]]

print(mylist)
print(mylist[0])
print(mylist[2])
print(mylist[-1])
print(mylist[-2])

print(mylist[1:4])
print(mylist[::2])


mylist = [1, 2, 3, 4, 5, True]
mylist[-1] = False
print(mylist)
mylist[0:3] = ["A", "B"]
print(mylist)
mylist[0:3] = ["A"]
print(mylist)
mylist[0:3] = "A"
print(mylist)

# -------------
# List Methods In Python
# -------------

# append()
myFriends = ['Amr', 'Alaa', 'Osama', 'Mohammed']
myFriends.append("Kareem")
print(myFriends)
myFriends.append(1)
print(myFriends)
myFriends.append(True)

myNewFriends = ['Mohee', "yousif"]
print(myFriends)
myFriends.append(myNewFriends)
print(myFriends)

# extend()
myFriends.extend(myNewFriends)
print(myFriends)
myFriends.extend('hamada')
print(myFriends)

# remove()
x = ['kareem', 1, 'mohammed', 'Ibraheem', 'yasser', 'kareem']
x.remove("kareem")
print(x)

# sort(reverse = false)
y = [123, 43, 0, -3, -100]
y.sort()
print(y)
y.sort(reverse=True)
print(y)

# reverse() --> Don't Sort A Lest just reverse it
y = ["kareem", 2, 3, 4,"mohammed"]
y.reverse()
print(y)

# clear()
a = [1, 2, 4]
x.clear()
print(x)

# copy()
a = [1, 3, 4, 5, 6]
c = a
a.append("kareem")
print(a)
print(c)
print("=================")
c = a.copy()
a.append("Yousif")
print(a)
print(c)

# count( 1 argument) => What Element to count
a = [1, 3, 4, 4, 5, 5, 5, 643, 4, 5]
print(a.count(4))

# index()
a = [1, 2, 3, 4, 4 ,5 ,5 ,6 ,6 ,4]
print(a.index(5))

# insert()
a = ["kareem", "yousif", "mohee", "JOe", "mohammed"]
a.insert(0, "Aziz")
print(a)
a.insert(-1, "BAhy")
print(a) # aziz kareem yousif mohee joe bahy mohammed

# pop()
a = ["kareem", "mohammed"]
print(a.pop(0))
print(a)

# ------------------------
# Tuples #
# ------------------------

myTuble = ('kareem', 'elgiushy')
myTuble2 = 'kareem', 'elgiushy'
print(type(myTuble))
print(type(myTuble2))
print(myTuble)
print(myTuble2)

# ------------------------
# Sets #
# ------------------------


# ------------------------
# Dictionary #
# ------------------------

myDict = {"name": 'kareem', "password": '123456789', "status": 'good'}

print(myDict)
print(myDict['name'])
print(myDict.get('name'))
print(myDict.keys())

languages = {
    'one': {
        "name": "html",
        "progress": "10/10"
    },
    'two': {
        "name": "css",
        "progress": "10/10"
    },
    'three': {
        "name": "php",
        "progress": "10/10"
    }
}

print(languages['two'])
print(languages['three']["name"])

print("Number Of Dictionary Items: %d" % len(languages))
print("Number of two items: {:f}".format( len(languages['two']) ) )

languages['four'] = {'name': 'sql', "progress": "9/10"}

languages['one']['name'] = 'html5'

print(languages)

html = languages['one']

html['name'] = 'html/html5'

print(html)
print(languages['one'])

print('=' * 50)

print(languages.keys())
print(languages.values())

print('=' * 50)
# setdefault()
user = {"name": 'kareem'}
print(user)
print(user.setdefault('name', 'ahmed'))
print(user.popitem())

print('=' * 50)

# ------------------------
# Data Conversion #
# ------------------------

# str() => convert to string

# int() => convert to integers

# tuple() => convert any to tuple
a = 'kareem'
b = [1, 2, 3, 4, 5, 6]
c = {"A", "B", "C"}
d = {"one": 1, 'two': 2, 'three': 3}

print(tuple(a))
print(tuple(b))
print(tuple(c))
print(tuple(d))

print('=' * 50)

# list() => convert any to list
a = 'kareem'
b = (1, 2, 3, 4, 5, 6)
c = {"A", "B", "C"}
d = {"one": 1, 'two': 2, 'three': 3}

print(list(a))
print(list(b))
print(list(c))
print(list(d))

print('=' * 50)

# set() => convert any to set
a = 'kareem'
b = [1, 2, 3, 4, 5, 6]
c = ("A", "B", "C")
d = {"one": 1, 'two': 2, 'three': 3}

print(set(a))
print(set(b))
print(set(c))
print(set(d))

print('=' * 50)

# dict() => from tuple or list to dictionary
b = [("A", 1), ("B", 2), ("C", 3)]
d = (("one", 1), ('two', 2), ('three', 3))

print(dict(b))
print(dict(d))

print('=' * 50)

# ------------------------
# if .... else if .... else statment #
# ------------------------

user = {
    "name": "kareem",
    "country": "Egypt",
    "student": True
}
course = {
    "name": "Python Course",
    "price": 100
}

if user['country'] == "Egypt" or user['country'] == 'Sudan':
    if user['student'] == True:
        print("Hello %s Because You Are From %s \nThe Course \"%s\" Price Is: %d$" % (user['name'], user['country'], course['name'], course['price'] - 95) )
    else:
        print("Sory You Aren't A Student ...")
elif user['country'] == "KSA":
    print("Hello %s Because You Are From %s \nThe Course \"%s\" Price Is: %d$" % (user['name'], user['country'], course['name'], course['price'] - 50) )
else:
    print("Hello %s Because You Are From %s \nThe Course \"%s\" Price Is: %d$" % (user['name'], user['country'], course['name'], course['price'] - 30) )

print("=" * 50)


# ------------------------
# Ternery If Statment ... shorthanded #
# ------------------------

movieRate = 18
age = 10

if age > movieRate:
    print("That movie is good for you".capitalize())
else:
    print("That movie isn't good for you".capitalize())

print("=" * 50)
print("=" * 50)
print("=" * 50)

print("this movie is good for you"if age > movieRate else "this movie is no good for you")

print("=" * 50)

# ------------------------
# membership operators 
# in
# not in #
# ------------------------

name = "Kareem"

print("K" in name) # true
print("x" in name) # false
print("e" in name) # true
print("k" in name) # false

print("=" * 50)

# list
friends = ['kareem', "mohammed", "youssif"]

print("kareem" in friends) # true
print("youssif" not in friends) # false
print("mohammed" in friends) # true

print("=" * 50)

# ------------------------
# Loops #
# ------------------------

# While Loops

# for loop

numbers = [1, 2, 3, 4, 5, 6]

for n in numbers:
    if n % 2 == 0:
        print("{:d} is An Even Number".format(n))
    else:
        print("{:d} is An Odd Number".format(n))
else:
    print("The Loop Is Finished !!")

kareem = "kareem"
for letter in kareem:
    print(letter)
else:
    print(f"No more Letters in {kareem}")


print("=" * 50)

# ------------------------
# Nested Loop new way #
# ------------------------
langs = {
    "html": {
        "Pugjs": 80
    },
    "css": {
        "sass": 40,
        "less": 69
    },
    "python": {
        "pytorch": 90,
        "TensorFlow": 95
    }
}

for lname, lvalue in langs.items():
    print("- " + lname.upper())
    for tech, progress in lvalue.items():
        print("== " + tech.capitalize() + " => " + str(progress) + "%")
    
print("=" * 50)
print("=" * 50)

# ------------------------
# Function ... Return #
# ------------------------

def hello() :
    return("hello world, new function :)")

message = hello()
print(message)

# ------------------------
# Function ... & Arguments #
# ------------------------

def hello(name = "Kemoo"):
    return "Hello Mr." + name

print(hello("kareem"))

print("=" * 50)
# ------------------------
# Function ... & Pack & Unpack (tuple and list)#
# ------------------------

mySkills = {
    "html": "10%",
    "js": "20%",
    "php": "30%"
}

def display_r(*skills):
    print(skills)
    for skill in skills:
        print(skill)

display_r('html', 'css', 'js', 'bootstrap', 'php', 'mysql')
print("=" * 50)
display_r(*mySkills)

print("=" * 50)
# ------------------------
# Function ... & Pack & Unpack Keyword arguments#
# ------------------------
mySkills = {
    "html": "10%",
    "js": "20%",
    "php": "30%"
}

def display_r(**skills):
    print(skills)
    for skill, value in skills.items():
        print(skill + " => " + value)

display_r(js = "80%", jqurey = "90%")
print("=" * 50)
display_r(**mySkills)

print("=" * 50)
# ------------------------
# Function ... Lambda Function
# #### Anonymous Function #####
# ------------------------

def say_hello(name, job = "Developer"):
    return "Hello {} Eng.{}".format(job, name)

hello = lambda name, job = "Developer": f"Hello {job} Eng.{name}"

print(say_hello("Kareem"))
print(hello("El-Giushy"))

print(say_hello.__name__)
print(hello.__name__)

print(type(hello))

print("=" * 50)

# ------------------------
# Bult-in functions #
# ------------------------

a = (1, "hamada", True)

if all(a):
    print("All Elements is true")
else:
    print("There is a false elements")


b = (True, False, 0, [])

if any(b):
    print("There is a true element")
else:
    print("There is no true elements")


print(bin(1500))

print(id(a))
print(id(b))
print(id(c))


# ------------------------
# More Built-in functions#
# ------------------------

# sum()
a = [1, 2, 40, 60, 80]

print(sum(a))
print(sum(a, 5))
print(sum(a, 6))

# round()
print(round(1.5))
print(round(1.965))
print(round(1.165))
print(round(152.21564, 3))

# range(start, end, step) end:required step=1 default
print(list(range(0,10, 2)))

# print(step=" " , end="\n") Default
print("hello Kareem")
print("hello","Kareem", "how", "are", "you", "today")
print("hello","Kareem", "how", "are", "you", "today", sep="|")

stmt = "This is a long statment And I want a separator"

print(stmt)
print(*stmt.split(" "), sep=" @ ")

print("Hello Print Method", end="@This is End of a line")
print("hello world v0.2")
print("hello world v0.3")

print("=" * 50)
# ------------------------
# More Built-in functions
# abs(value)
# pow(value, exponant, modulus)
# min(value,value,value,value)
# max(value,value,value,value) #
# ------------------------

#slice(start, end, stp)
ilist = ["A", "B", "C", "D", "E", "F"]
print(ilist[:5])
print(ilist[slice(2,5)])

# ------------------------
# More Built-in functions
# map(func, iterator)#
# ------------------------

names = [("kareem", "Eng"), ("Kemoo", "Developer"), ("Karamila", "Accountant"), ("KOKO", "IT")]

vary = map(lambda dev: f"Welcome {dev[1]}.{dev[0]}", names)
print(vary)

for n in list(vary):
    print(n)

print("=" * 50)
# ------------------------
# More Built-in functions
# filter(func, iterator)#
# ------------------------

def checknum(n):
   if n > 10:
       return n

l = [1, 4, 10, 100, 200, 450]

r = filter(checknum, l)

print(r)

for n in r:
    print(n)

print("=" * 50)

def checknum(n):
   if n == 0:
       return n # return 0 which is false

l = [0, 0, 1, 4, 10, 100, 200, 450, 0, 0]

r = filter(checknum, l)

print(r)

for n in r:
    print(n) #don't print

print("=" * 50)
def checknum(n):
   return n > 10

l = [1, 4, 10, 100, 200, 450]

r = filter(checknum, l)

print(r)

for n in r:
    print(n)

print("=" * 50)
# ------------------------
# More Built-in functions
# reduce(func, iterator)#
# ------------------------

from functools import reduce

def sumall(n1, n2):
    return n1 + n2

l = [1, 4, 5, 8, 0, 6]

# ((((1+4)+5)+8)+0)+6
# r = reduce(sumall, l)
r = reduce(lambda n1, n2: n1 + n2, l)

print(sum(l))
print(r)

from random import random, randint
r = reduce(sumall, l)
print(random())
print(randint(10, 100))