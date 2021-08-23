#122333 1=1 2=2 3=3 then betyfu else 1233 1=1 2=1 33=1 not beutyful
n=input()
l=[c for c in n]
a=set(l)
g=[]
a1=list(a)
for i in a:
    g.append(l.count(i))
c=0
for i in range(len(a)):
    if(int(a1[i])==g[i]):
        c+=1
if c==len(a):
    print("beautiful")
else:
    print("not beutiful")
#1224444
    beatyful
        
        
    
    


