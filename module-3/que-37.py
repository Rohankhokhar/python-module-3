#  Write a Python script to print a dictionary where the keys are numbers
# between 1 and 15

dict1 = {1 : "a" , 2 : "c" , 3 : "d" , 4 : "h" , 19 : "k" , 32 : "p" ,7 : "o" , -5 : "y"}

result = []

for keys , value in dict1.items() :
    if keys >= 1 and keys <= 15  :
        print(f"key {keys} : values {value}")

print(result)        

# dict1 = { i : i**2 for i in range (1 , 16)}
# print(dict1)

