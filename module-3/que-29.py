#  Write a Python program to unzip a list of tuples into individual lists.

tuple1 = [('aaa', 12), ('bbb', 13), ('ccc', 14)]

names , age = zip(*tuple1)

print(list(names))
print(list(age))
        

