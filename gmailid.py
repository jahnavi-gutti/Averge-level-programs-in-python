n=int(input())
l=[]
r=[]
h=[" ","_"]
for i in range(n):
    s=input()
    l.append(s)
for i in l:
    if "@" in i:
        x,y=i.split("@")
        if x not in h  and "." in y:
            print("True")
        else:
            print("False")
    else:
        print("False")
    
        
            
    
