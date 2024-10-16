#  Write a Python program to remove an empty tuple(s) from a list of tuples.

tuple_list = [(1,2),(),(3),(3),(),(7),(9)]

tup = []

for t in tuple_list :
    if t  :
        tup.append(t)

print(tup)        