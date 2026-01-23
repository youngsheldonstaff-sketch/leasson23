dictionery = {"codingal": 2, "is" : 2, "best": 2}

print("original dictionary: " +
       str(dictionery))


k= 2

res=0

for key in dictionery:
    if dictionery[key]==k:
        res+=1

print("the number of k is: " + str(res))
