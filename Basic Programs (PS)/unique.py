myList = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
#
# put your code here
#
l=list()
for i in range(0,len(myList)):
    if myList[i] in l:
        continue
    else:
        l.append(myList[i])
print("The list with unique elements only:")
print(l)
