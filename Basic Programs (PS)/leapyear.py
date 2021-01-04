"""def isYearLeap(year):
#
# your code from LAB 4.1.3.6
#
    if(year%4==0 and ((year%400==0) or (year%100!=0))):
        return 1
    else:
        return 0

def daysInMonth(year, month):
#
# put your new code here
#   
    y=isYearLeap(year)
    if(month>=1 and month <=7):
        if(month == 2 and y==0):
            a=28
            return a
        elif(month ==2 and y!=0):
            b=29
            return b
        elif(month%2==0 and month!=2):
            c=30
            return c
        elif(month%2!=0):
            d=31
            return d
    elif(month>=8 and month <=12):
        if(month%2==0):
            c=31
            return c
        elif(month%2!=0):
            d=30
            return d
        

testYears = [1900, 2000, 2016, 1987]
testMonths = [2, 2, 1, 11]
testResults = [28, 29, 31, 30]
for i in range(len(testYears)):
	yr = testYears[i]
	mo = testMonths[i]
	print(yr, mo, "->", end="")
	result = daysInMonth(yr, mo)
	if result == testResults[i]:
		print("OK")
	else:
		print("Failed")
"""
#isprime
"""
def isPrime(n):
#
# put your code here
#
    if(n>1):
        for i in range(2,n):
            if(n%i==0):
                break
        else:
            print(n)
for i in range(1, 20):
	if isPrime(i + 1):
			print(i + 1, end=" ")
print()
"""
#fib
"""def fib(n):
    a=0
    b=1
    for i in range(0,n):
        print(a,end=" ")
        c=a+b
        a=b
        b=c
for i in range(0,10):
    print(i,"-",end=" ")
    fib(i)
    print()
    """
def bincoeff(n,k):
    c=[[0 for i in range(k)] for i in range(n)]
    for i in range(0,n):
        for j in range(min(i,k)+1):
            if(j==0 or i==j):
                c[i][j]=1
            else:
                c[i][j]=c[i-1][j-1]+c[i-1][j]
    for i in range(0,n):
        for j in range(0,k):
            if(c[i][j]!=0):
                print(c[i][j],end=" ")
        print()
        



n=int(input())
k=n
bincoeff(n,k)

        
    
