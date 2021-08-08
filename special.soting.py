#Vishal is a competitive coder and he loves problems on sorting and searching. He is bored right now and decides to solve a sorting problem with a modification. He decides to sort the elements at the even indices of an array in ascending order and the elements at the odd indices in descending order. Vishal goes outside his room after coding the solution, but his laptop crashes and he is unable to show it to his teacher. Can you help Vishal by coding the solution to the problem?

n=int(input())
l=list(map(int,input().split()))
e=[l[x] for x in range(n) if x%2==0]
o=[l[x] for x in range(n) if x%2!=0]
E=sorted(e)
O=sorted(o,reverse=True)
El=len(E)
Ol=len(O)
m=min(El,Ol)
for i in range(m):
    print(E[i],O[i],end=" ")
if El>Ol:
    print(E[m])
elif Ol>El:
    print(O[m])

"""
Sample Input 0

10
9 8 7 1 2 3 6 5 4 10
Sample Output 0

2 10 4 8 6 5 7 3 9 1"""
