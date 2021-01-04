import re
s=input()
words=list()
words=s.split(" ")
newwords=[word[::-1] for word in words]
newsentence=" ".join(newwords)
print(newsentence)
l=list()
l=newsentence.split(" ")
for i in l:
    if(re.search("[0-9]",i) and re.search("[a-z]",i)):
        a=i[::-1]
        b=a[-1:]+a[1:-1]+a[:1]
        print(b.capitalize(),end=" ")
    elif(re.search("[0-9]",i)):
        print(i[::-1],end=" ")
    else:
        print(i.capitalize(),end=" ")