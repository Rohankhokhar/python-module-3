# Write a Python function that takes a list and returns a new list with unique
# elements of the first list.

def unique(list):
    uniquelist = []
    for i in list:
        if i not in uniquelist:
            uniquelist.append(i)
    return uniquelist        
    
list1 = [1,2,2,3,4,5,5,6,5,4,3,2,6,7,8,9]    
res = unique(list1)
print(res)