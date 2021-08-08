#A number is called 2050-number if it is 2050, 20500, ..., (2050⋅10^k for integer k≥0).
#Given a number n, you are asked to represent n as the sum of some (not necessarily distinct) 2050-numbers. Compute the minimum number of 2050-numbers required for that.
t=int(input())
tn=[]
for x in range(t):
    tn.append(int(input()))
for y in tn:
    if y % 2050!=0:
        print(-1)
    else:
        dl=list(map(int,str(int(y/2050))))
        print(sum(dl))
"""Sample Input 0

2
205
2050
Sample Output 0

-1
1
Sample Input 1

1
4100
Sample Output 1

2"""
