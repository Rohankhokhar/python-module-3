#  Write a Python script to check if a given key already exists in a dictionary.

dict1 = {'a': 1,
         'b': 2,
         'c': 3, 
         'd': 4, 
         'e': 1, 
         'f': 2}

check = "c"

if dict1.get(check) is not None:
    print("key exist in dictionary")
else:
    print("given key is not exist in dictionary")

# if check in dict1 :
#     print("key exist in dictionary")
# else:
#     print("given key is not exist in dictionary")    


