n=int(input())
l=list(map(int,input().split()))[:n]
for i in range(n):
    mi=i
    for j in range(i+1,n):
        if(l[mi]>=l[j]):
            mi=j
    l[mi],l[i]=l[i],l[mi]
    print(l)