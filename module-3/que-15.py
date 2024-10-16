#  Write a Python program to get unique values from a list

list1 = [1,2,3,2,2,1,5,6,7,8,9,0]

uniqe = []

for i in list1:
    if i not in uniqe:
        uniqe.append(i)

print(uniqe)        

# set1 = set(list1)

# print(set1)