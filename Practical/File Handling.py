# ------------------------
# File Handling In Python
# ------------------------
# "a" => Append - Open File For Appending Values, Create File If Not Exists
# "r" => Read -[Default Value] Open File for Reading And Give Error If File Not Exists
# "w" => Write - Open File For Writing, Create File If not Exists
# "x" => Create - Create File, Gives Error If File Exists #
# ------------------------

# System Os Module Exercise
# import os
# from os import path

# # Current Working Directory
# print(os.getcwd())

# # Current File Name And Path
# print(__file__)

# # Absolute File Path
# print(path.abspath(__file__))

# # Directory Name
# print(path.dirname(path.abspath(__file__)))


myfile = open(r"C:\Users\AUC\Documents\PyProjects\files\demo.txt", "r")

print(myfile.read())
print("=" * 2)
print(myfile.readline())