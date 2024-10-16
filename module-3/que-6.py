#  Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings.

list = ["abc" , "aba" , "cc" , "xyz" , "dd" ,"asd"]

count = 0

for l in list :
    if len(l) >= 2 and l[0] == l[-1] :
        count += 1
print(count)        