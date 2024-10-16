#  How Do You Check The Presence Of A Key In A Dictionary?

dict1 = {"a" : 5 ,"b" : 4 , "c" : 3 , "d" : 3 , "e" : 5} 

if "a" in dict1 :
    print("a key in dictonary ")
else :
    print("a key not in dictonary ")

ans = dict1.get("a")
if ans is not None :
    print("a key in dictonary ")
else :
    print("a key not in dictonary ")
