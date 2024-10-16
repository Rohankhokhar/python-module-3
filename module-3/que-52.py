# #  How Many Basic Types Of Functions Are Available In Python?

# Built-in Functions: Predefined functions like len().
result = len("Hello, World!")
print(result)
# User-defined Functions: Custom functions created by the user.
def formate(name):
    return f"Hello, {name}!"

print(format("rohan"))
# Lambda Functions: Small anonymous functions for quick use.
add = lambda x, y: x + y
print(add(5,3))
# Recursive Functions: Functions that call themselves.
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))

# others :-
# positional :-
def add(a, b):
    print(a + b)
add(10, 20)

def add(a, b, c):
    print(a + b + c)
add(10, 20, 30) 

# default/keyword parameter

def bill(tomato, potato=100):
    print("Total = ", tomato + potato)

bill(50, 30)

# variable length parameter
# *args
# **kwargs

def add(*nums):
    # print(type(nums))
    print(sum(nums))

add(653, 4567, 23, 7, 384, 678446)


def bill(**products):
    # print(type(products))
    total = 0
    for item, price in products.items():
        print(f"{item} : {price}")
        total += price
    print("-"*40)
    print("Total amount: ", total)
    # GST 5% apply
    print("GST: ", total * 0.05)
    print("Final amount: ", total + (total * 0.05))

bill(pen=100, book=30, milk=33)

# map function
# print(list(map(lambda num:num*num, [1,2,3,4,5,6,7,8,9,10])))
