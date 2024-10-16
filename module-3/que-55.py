#  How can you get a random number in python?

import random

start = 1
end = 10

l1= random.randrange(start,end) #excluseive range to 1 to 9
l2 = random.randint(1, 10) #use range in randome number select

print(l2)
print(l1)