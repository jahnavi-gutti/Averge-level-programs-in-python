#Given an expression string x. Examine whether the pairs and the orders of “{“,”}”,”(“,”)”,”[“,”]” are correct in exp.
s=input()
x=list(s)
a1=x.count("{")
a2=x.count("}")
a3=x.count("[")
a4=x.count("]")
a5=x.count("(")
a6=x.count(")")
if a1==a2 and a3==a4 and a5==a6:
    print(1)
else:
    print(0)
"""
Sample Input 0

{([])}
Sample Output 0

1"""
