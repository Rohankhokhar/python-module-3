#  Write a Python function to get the largest number, smallest num and sum of all from a list.

def lss(list1):
    if list is not None:
        largest = max(list1)
        smallest = min(list1)
        sum1 = sum(list1)
    return largest,smallest,sum1       
list = [1,2,16,4,12,6,7,19,9,10]
res = lss(list)

print(res)

