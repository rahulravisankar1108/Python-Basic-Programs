upp=int(input())
low=int(input())
if(low>1):
    for i in range(low,upp):
        for j in range(2,i//2):
            if(i%j==0):
                break
        else:
            print(i,end=" ")
            
'''n=int(input())
if(n>1):
    for i in range(2,n//2):
        if(n%i==0):
            print("not prime")
            break
    else:
        print("Prime")
        
else:
    print("not prime")
    
            
'''
