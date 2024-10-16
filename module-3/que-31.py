#  How will you create a dictionary using tuples in python?

tuple1 = [("name" , "rohan") , ("age" , 20)]

dictionary = {}

for key , value in tuple1 :
    dictionary[key] = value

print(dictionary)    

# dictionary = dict(tuple1)

# print(dictionary)