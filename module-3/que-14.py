#  Write a Python program to find the second smallest number in a list.

list = [1,22,4,5,55,3,78,90,6,7,8]

flag = False

while not flag :
    flag = True
    for index , i in enumerate(list) :
        if index < len(list)-1 :
            if list[index] > list[index+1] :
                list[index] , list[index+1]= list[index+1] , list[index]
                flag = False
            
         
print(list[1])            


# list.sort()

# second_smallest = list[1]

# print(second_smallest)
         