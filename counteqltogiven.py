s=input()
n=int(input())
w=s.split()
for i in set(w):
    if w.count(i)>=n:
        print(i,end=" ")
    
"""
cat batman latt matter cat matter cat cat latt latt
3
cat latt"""
