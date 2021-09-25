n=input()
b=2
r=0
for i in range(len(n)):
    i1=i
    p=len(n)-i1-1
    d=int(n[i])
    r+=d*b**p
print(r)
"""
111
7"""
