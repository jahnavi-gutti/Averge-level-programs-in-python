"""
Alex works at a clothing store. There is a large pile of socks that must be paired by color for sale. Given an array of integers representing the color of each sock, determine how many pairs of socks with matching colors there are.

For example, there are n=7 socks with colors ar = {1,2,1,2,1,3,2}. There is one pair of color 1 and one of color 2. There are three odd socks left, one of each color. The number of pairs is 2."""

def sockMerchant(n, ar):
    pairs = 0
    set_ar = set(ar)
    for i in set_ar:
        count = ar.count(i)
        pairs+=count//2
    return pairs
    
n = int(input())
ar = list(map(int, input().split()))
print(sockMerchant(n, ar))
"""
Sample Input
             9
             10 20 20 10 10 30 50 10 20
Sample Output
             3"""
