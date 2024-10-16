#  Write a Python program to create a tuple with different data types.

tuple = (1,1.2,1.00,1+2j,"r",2)

print(tuple)

for i in tuple :
    print(f"element : {i} type : {type(i)}")