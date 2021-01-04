n=int(input())
l=list()
while(n>0):
    dig=n%2
    l.append(dig)
    n=n//2
print(l)
rev=l[::-1]
print(rev)
i=0
temp=rev[i]
rev[i]=rev[i+1]
rev[i+1]=temp
temp1=rev[i+2]
rev[i+2]=rev[i+3]
rev[i+3]=temp
count=0
for i in range(0,len(rev)):
    if(rev[i]==1 and i==0):
        count+=8
    elif(rev[i]==1 and i==1):
        count+=4
    elif(rev[i]==1 and i==2):
        count+=2
    elif(rev[i]==1 and i==3):
        count+=1
print(count)