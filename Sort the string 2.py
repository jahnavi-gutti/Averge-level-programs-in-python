#Given a string containing a mix of upper and lowercase characters, sort the letters in ascending order such that the positions of upper and lowercase letters do not change.


s=input()
s=list(s)
u=[x for x in sorted(s) if x.isupper()]
l=[x for x in sorted(s) if x.islower()]
i=0
j=0
for k in range(len(s)):
    if s[k].isupper():
        s[k]=u[i]
        i+=1
    elif s[k].islower():
        s[k]=l[j]
        j+=1
print("".join(s))
"""
Sample Input 0

HyDeRaBaD
Sample Output 0

BaDaDeHyR"""
