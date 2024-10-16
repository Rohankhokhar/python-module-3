#  How can you pick a random item from a list or tuple?
import random

list1 = [1,2,3,4,5,6]
tuple1 = (1,2,3,4,5,6)

r1 = random.choice(list1)
r2 = random.choice(tuple1)

print(r1)
print(r2)