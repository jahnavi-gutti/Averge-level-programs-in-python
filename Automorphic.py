n=input()
l=len(n)
g=int(n)*int(n)
h=g%10**l
if int(n)==h:
    print("Automorphic")
else:
    print("Not Automorphic")
"""
5
Automorphic"""
