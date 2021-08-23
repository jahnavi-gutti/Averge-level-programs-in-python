from itertools import permutations
n = int(input())  
a=[]
for num in range(1,n + 1):  
   if num > 1:  
       for i in range(2,num):  
           if (num % i) == 0:  
               break  
       else:  
           a.append(num)
p=permutations(a,2)
c=[]
for i in p:
    c.append("".join([str(value) for value in i]))
co=0
for k in c:
    for i in range(2,num):  
           if (int(k )% i) == 0:  
               break  
    else:  
        co+=1
print(co)
"""
10
4"""
    
    

    
