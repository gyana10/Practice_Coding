
"""Given an array of N integers and a target value K, find the index of K in the array. Return the 1-based index if
found, else return -1. The array may contain duplicate elements; return the first occurrence.
Example
Input
arr =[4, 7, 2, 9, 1] K = 9
Output4
Approach & Explanation
We scan through the array one element at a time from left to right. The moment we find an element equal to
K, we return its 1-based index. If we reach the end without a match, we return -1. This is the most
fundamental search technique used as a baseline in TCS NQT.
-------------------------------------------------------------------------------------------"""
n=int(input())
arr=list(map(int,input().split()))
k=int(input())
for i in range(n):
    if arr[i]==k:
        print(i+1)
        break
else:
    print(-1)

"""Problem Statement
Given a sorted array of N integers and a target K, return the index (0-based) of K using Binary Search. If K is
not present, return -1. This is a classic TCS NQT question testing divide-and-conquer searching.
Example
Input
arr = [1, 3, 5, 7, 9, 11, 13] K = 7
Output
3
Approach & Explanation
Binary Search works by repeatedly halving the search space. We maintain two pointers: low and high. We
compute the midpoint and compare arr[mid] with K. If they match, we return mid. If K is smaller, we search
the left half; otherwise, the right half. This reduces time complexity from O(N) to O(log N)
-------------------------------------------------------------------------------------------"""
n=int(input())
arr=list(map(int,input().split()))
k=int(input())
low=0
high=n-1
while low<=high:
    mid=(high+low)//2
    if arr[mid]==k:
        print(mid)
        break
    elif k<arr[mid]:
        high=mid-1
    else:
        low=mid+1    
else:
    print(-1)        

"""Problem Statement
Given a sorted array with possible duplicates and a target K, find the first and last positions of K. Return [-1,
-1] if K is not found. TCS NQT frequently tests this variation to check whether candidates can modify
standard binary search.
Example
Input
arr = [2, 4, 4, 4, 6, 8] K = 4
Output[1, 3]
Approach & Explanation
We run binary search twice — once biased to find the leftmost occurrence (first position) and once biased to
find the rightmost occurrence (last position). When arr[mid] == K, instead of returning immediately, we record
the index and continue searching left (for first) or right (for last).
-------------------------------------------------------------------------------------"""
def first(arr, k):

    low = 0
    high = len(arr) - 1

    ans = -1

    while low <= high:

        mid = (low + high) // 2

        if arr[mid] == k:
            ans = mid
            high = mid - 1

        elif arr[mid] < k:
            low = mid + 1

        else:
            high = mid - 1

    return ans


def last(arr, k):

    low = 0
    high = len(arr) - 1

    ans = -1

    while low <= high:

        mid = (low + high) // 2

        if arr[mid] == k:
            ans = mid
            low = mid + 1

        elif arr[mid] < k:
            low = mid + 1

        else:
            high = mid - 1

    return ans


arr = list(map(int, input().split()))
k = int(input())

print([first(arr, k), last(arr, k)])



"""Problem Statement
A peak element is an element greater than its neighbors. Given an array where arr[-1] = arr[N] = -infinity
(boundaries), find any peak element's index. The array may have multiple peaks. TCS NQT tests this to
check creative application of binary search.
Example
Input
arr = [1, 3, 5, 4, 2]
Output
2 (arr[2] = 5 is a peak)
Approach & Explanation
We use binary search creatively here. At the midpoint, if arr[mid] > arr[mid+1], a peak must exist on the left
half (including mid). Otherwise, a peak exists on the right half. This works because we are guaranteed
boundaries are -infinity."""
arr = list(map(int, input().split()))

low = 0
high = len(arr) - 1

while low < high:

    mid = (low + high) // 2

    if arr[mid] > arr[mid + 1]:
        high = mid

    else:
        low = mid + 1

print(low)