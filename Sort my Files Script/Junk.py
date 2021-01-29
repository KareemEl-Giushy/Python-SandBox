# ------------------------
# Make Junk Files#
# ------------------------
from os import path


myPath = input("Enter The Path: ").strip() + "/"



if bool(myPath) and not myPath.isspace() and path.isdir(myPath) and not myPath.endswith("."):
    pass
else:
    print("Not Executed. Double Check Your Path")
    exit()

for n in range(5):
    open(myPath + str(n) + ".txt", 'x')


for n in range(5):
    open(myPath + str(n) + ".doc", 'x')


for n in range(5):
    open(myPath + str(n) + ".jpg", 'x')


for n in range(5):
    open(myPath + str(n) + ".png", 'x')


for n in range(5):
    open(myPath + str(n) + ".mp4", 'x')


for n in range(5):
    open(myPath + str(n) + ".mp3", 'x')


for n in range(5):
    open(myPath + str(n) + ".zip", 'x')


for n in range(5):
    open(myPath + str(n) + ".rar", 'x')


for n in range(5):
    open(myPath + str(n) + ".mkv", 'x')
