#Problem Statement:-
#Compute the nearest larger number by interchanging its digits updated.Siven 2 numbers a and b find the smallest number greater than b by interchanging the digits of a and if not possible
#print 1.Input Format -2 numbers a and b, separated by space.
#Output Format
#A single mumber greater than b.
#If not possible, print -1
#Example 1:
#Sample Input:
#459 500
#Sample Output: 549
#Example 2:
#Sample Input: 645757 457765
#Sample outputs
#465577
from itertools import permutations

a, b = map(int, input().split())

digits = list(str(a))

ans = float('inf')

for p in permutations(digits):

    num = int(''.join(p))

    if num > b:
        ans = min(ans, num)

if ans == float('inf'):
    print(-1)
else:
    print(ans)