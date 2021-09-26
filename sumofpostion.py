n=int(input())
l=list(map(int,input().split()))
h=[]
for i in range(len(l)):
    h.append(sum(l[:i+1]))
print(*h)
"""
5
1 4 2 6 3
1 5 7 13 16"""
