#  Write a Python program to create and display all combinations of letters,
# selecting each letter from a different key in a dictionary.
# Sample data: {'1': ['a','b'], '2': ['c','d']}
# Expected Output:
# ac ad bc bd

data = {'1': ['a', 'b'], '2': ['c', 'd']}

keys = list(data.keys())

lists = [data[key] for key in keys]

result = [] 
 
for l1 in lists[0] :
    for l2 in lists[1]:
        result.append(l1+l2) 

for combo in result:
    print(combo)        
# import itertools

# data = {'1': ['a', 'b'], '2': ['c', 'd']}

# letter_lists = data.values()

# combinations = itertools.product(*letter_lists)

# for combo in combinations:
#     print(''.join(combo))

# print(combinations)


