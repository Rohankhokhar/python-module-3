#  Write a Python program to check whether a list contains a sub list

list = [1,2,3,4,5,6,[2,5],8]
sub_list = [2,5]

if sub_list in list:
    print("main list containt to sublist")
else :
    print("sub list not contain in main list")    
        
