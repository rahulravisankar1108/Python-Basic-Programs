import re
s=input()
flag=0
while(True):
    if(len(s)<8):
        flag=-1
        break
    elif(not re.search("[a-z]",s)):
         flag=-1
         break
    elif(not re.search("[A-Z]",s)):
         flag=-1
         break
    elif(not re.search("[0-9]",s)):
         flag=-1
         break
    elif(not re.search("[!@#$%^&*()]",s)):
         flag=-1
         break
    else:
        flag=0
        print("Your password is Strong")
        break
if(flag==-1):
    print("Your password is not Strong")
