n=int(input())
l=list(map(int,input().split()))[:n]
for i in range(1,n):
    key=l[i]
    j=i-1
    while(j>=0 and l[j]>key):
        l[j+1]=l[j]
        j-=1
    l[j+1]=key
print(l)