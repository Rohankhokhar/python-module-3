#  How will you set the starting value in generating random numbers?

import random

seed1 = 42
seed = random.seed(seed1)
num1 = random.randint(1, 100)

print(num1)
