#print the count of a given char from a string of char
I/p
hello there
e
3
o/p
10


s=input()
#rev=s[::-1]
#print(rev)
key=input()
count=0
num=int(input())
for i in range(0,len(s)):
    if(key==s[i]):
        count+=1
    if(count==num):
        print(i+2)