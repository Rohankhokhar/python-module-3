# Write a Python function that takes two lists and returns true if they have at least one common member.

list1 = [1,2,3,4,5,6,7,8,9,0]
list2 = ["a","b","c","d",0,"e","o"]

result = False

for i in list1 :
    if i in list2 :
        result = True
        break

print(result)
        