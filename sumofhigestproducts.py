n=int(input())
l=list(map(int,input().split()))
c=1
k=1
for i in range(len(l)):
    for j in range(i+1,len(l)):
        if abs(l[i]*l[j])>c:
            c=abs(l[i]*l[j])
            k=l[i]+l[j]
print(k)
"""o/p
7
9 -3 8 -6 -7 8 10
19"""
        

