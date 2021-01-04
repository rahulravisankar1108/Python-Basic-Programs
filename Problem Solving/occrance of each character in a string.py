s=input()
for i in range(len(s)):
    if(len(s)==0):
        break
    ch=s[0]
    if(ch==' ' or ch=='\t'):
        continue
    count=1
    for j in range(1,len(s)):
        if(ch==s[j]):
            count+=1
    s=s.replace(ch,'').strip()
    print(s)
    print(ch," ",count)

#aliter (advanced)
from collections import Counter
s=input()
s1=""
for i in s:
    if(i!=" "):
        s1+=''.join(i)
    else:
        continue
coun=Counter(s1)
for k,v in coun.items():
    print(k,v,sep=" ")