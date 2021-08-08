#Rajesh was going through alternative array sorting. He wishes to print the array alternatively. Hence hired you. Your task is to help rajesh in printing the array alternatively.An alternative array is an array in which the first element is maximum of the whole array, the second element is minimum of the whole array.Third element is second largest. Fourth element is the second smallest And so on.print the array in the desired manner.

Input Format
n=int(input())
l=list(map(int,input().split()))
l=sorted(l)
if n%2==0:
    for i in range(len(s)//2):
        print(l[-(i+1)],l[i],end=" ")
elif n%2!=0:
    for i in range(len(l)//2):
        print(l[-(i+1)],l[i],end=" ")
print(l[n//2])
"""
Sample Input 0

5 
1 7 11 16 19
Sample Output 0

19 1 16 7 11"""
