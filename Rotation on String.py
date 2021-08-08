#Given a string and an integer 'n'. Rotate the string left or (anti-clockwise) if 'n' is odd else rotate the srtring right or (clockwise)
s=input().strip()
d=int(input())
if d%2==0:
    fright=s[0:len(s)-d]
    sright=s[len(s)-d:]
    print(sright+fright)
else:
    fleft=s[0:d]
    sleft=s[d:]
    print(sleft+fleft)
"""
Sample Input 0

HelloWorld
2
Sample Output 0

ldHelloWor"""
