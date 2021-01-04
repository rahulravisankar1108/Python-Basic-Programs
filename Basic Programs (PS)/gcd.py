def gcd(a,b):
    if(b==0):
        return 1
    else:
        return gcd(b,a%b)
a=int(input("Enter the first number "))
b=int(input("Enter the second number "))
print("The gcd of two number is ",gcd(a,b)) 
