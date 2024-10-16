#  Differentiate between append () and extend () methods?

list = [1,2,3,4,5]
list2 = [6,7,8]

list.append(list2) #append add list2 in one singe element
print(list)

list.extend(list2) #extend add list2 all element individually
print(list)
