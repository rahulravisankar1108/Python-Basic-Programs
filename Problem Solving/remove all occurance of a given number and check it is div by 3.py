s=(input())
ch=(input())
dig=int(ch)
l=list()
ch1=" "
for i in range(0,len(s)):
    if(s[i]!=ch):
        ch1=s[i]
        l.append(ch1)

res=int("".join(map(str,l)))
print(res)
if(res%dig==0):
    print("Divisible")
else:
    print("Not divisible")