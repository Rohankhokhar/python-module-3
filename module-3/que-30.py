#  Write a Python program to convert a list of tuples into a dictionary.

tuple1 = [("name" , "rohan") , ("age" , 20)]

dictionary = dict(tuple1)

dictionary2 = {key : value for key , value in tuple1}

print(dictionary)
print(dictionary2)



