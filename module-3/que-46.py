#  Write a Python program to combine values in python list of dictionaries.
# Sample data: [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount':
# 300}, o {'item': 'item1', 'amount': 750}]
# Expected Output:
# Counter ({'item1': 1150, 'item2': 300})

data = [
    {'item': 'item1', 'amount': 400},
    {'item': 'item2', 'amount': 300},
    {'item': 'item1', 'amount': 750}
]
amounts = {}
for i in data :
    item = i["item"]
    amount = i["amount"]
    if item in amounts:
        amounts[item] += amount
    else :
        amounts[item] = amount  
print(amounts)          
