#  Write a Python program to convert a tuple to a string.

tuple = ("hello" , "world" , "good" , "morning")

string = ""

for i in tuple :
    string += i + " "
print(string)