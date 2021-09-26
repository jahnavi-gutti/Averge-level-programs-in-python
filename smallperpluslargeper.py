n=input()
d=[int(x)  for x in n]
a=sorted(d)
b=sorted(d,reverse=True)
x=[str(x)  for x in a]
y=[str(x)  for x in b]
print(int("".join(x))+int("".join(y)))
"""
743
1090"""
