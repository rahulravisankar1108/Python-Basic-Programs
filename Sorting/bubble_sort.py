n=int(input())
l=list(map(int,input().split()))
for i in range(n):
    for j in range(0,n-i-1):
        if(l[j]>=l[j+1]):
            l[j],l[j+1]=l[j+1],l[j]        
print(l)