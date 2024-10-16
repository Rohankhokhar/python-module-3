#  Write a Python program to remove duplicates from a list.

list = [1,2,3,2,3,4,5,8,5,5,7,9,0]

list1 = []

for l in list :
    if l not in list1 :
        list1.append(l)
print(list1)        