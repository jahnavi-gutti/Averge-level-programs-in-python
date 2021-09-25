a,b=map(int,input().split())
l=list(map(int,input().split()))
for i in range(len(l)):
    for j in range(i+1,len(l)):
        if l[i]+l[j]==b:
            print(i,j)
            break
        
"""
7 7
1 2 4 5 8 9 1
1 3
"""
