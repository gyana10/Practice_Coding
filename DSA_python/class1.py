
"""An originally sorted array has been rotated at an unknown pivot. Given such an array and a target K, return
the index of K (0-based). Return -1 if K is absent. This is a top TCS NQT and interview question.
Example
Input
arr = [6, 7, 1, 2, 3, 4, 5] K = 3
Output
4
Approach & Explanation
Even in a rotated array, one half is always sorted. We check which half is sorted, then determine if K lies in
that half. If K is in the sorted half, we search there; otherwise, we search the other half. This allows us to keep
O(log N) complexity even after rotation.
-------------------------------------------------------------------------------"""
arr=list(map(int,input().split()))
k=int(input())
low=0
high=len(arr)-1
while low<=high:
    mid=(low+high)//2
    if arr[mid]==k:
        print(mid)
        break
    if arr[low]<=arr[mid]:
        if arr[low]<=k<arr[mid]:
            high=mid-1
        else:
            low=mid+1    
    else:
        if arr[mid]<k<=arr[high]:
            low=mid+1
        else:
            high=mid-1
else:
    print(-1)                       


"""Count Occurrences of Element
Problem Statement
Given a sorted array and a target K, count the number of times K appears. A naive approach scans the whole
array in O(N). TCS NQT expects you to use Binary Search for an O(log N) solution.
Example
Input
arr = [1, 2, 2, 2, 3, 4, 5] K = 2
Output
3
Approach & Explanation
We use the same technique as Q3 — find the first and last positions of K using two binary searches, then
compute: count = last - first + 1. If K is not found, return 0.
----------------------------------------------------------------------------------"""
def first_occ(arr, k):

    low = 0
    high = len(arr) - 1
    first = -1

    while low <= high:

        mid = (low + high) // 2

        if arr[mid] == k:
            first = mid
            high = mid - 1

        elif arr[mid] < k:
            low = mid + 1

        else:
            high = mid - 1

    return first

def last_occ(arr, k):

    low = 0
    high = len(arr) - 1
    last = -1

    while low <= high:

        mid = (low + high) // 2

        if arr[mid] == k:
            last = mid
            low = mid + 1

        elif arr[mid] < k:
            low = mid + 1

        else:
            high = mid - 1

    return last
arr = list(map(int, input().split()))
k = int(input())

first = first_occ(arr, k)

if first == -1:
    print(0)

else:
    last = last_occ(arr, k)
    print(last - first + 1)


"""Find Minimum in Rotated Sorted Array
Problem Statement
A sorted array has been rotated at some pivot. Find the minimum element of the array in O(log N) time.
Assume all elements are unique. This is a classic TCS NQT + FAANG question.
Example
Input
arr = [4, 5, 6, 7, 0, 1, 2]
Output
0
Approach & Explanation
The minimum element is always the inflection point — where the rotation happened. In a binary search, if
arr[mid] > arr[high], the minimum is in the right half. Otherwise, the minimum is in the left half (including mid).
We narrow down until low == high.
-----------------------------------------------------------------------------------"""
arr=list(map(int,input().split()))
low=0
high=len(arr)-1
while low<=high:
    mid=(low+high)//2
    if arr[mid]>arr[high]:
        low=mid+1
    else:
        high=mid

print(arr[low])        


"""Square Root using Binary Search
Problem Statement
Given a positive integer N, find the floor of its square root without using any built-in math functions. TCS NQT
uses this to test 'Binary Search on Answer' — searching in a value range instead of an array.
Example
Input
N = 37
Output
6 (floor of sqrt(37) = 6.08... = 6)
Approach & Explanation
Instead of searching in an array, we binary search over the answer range [1, N]. For each mid, we check if
mid*mid <= N. If yes, mid is a valid floor candidate; we record it and try for a larger answer. If mid*mid > N,
we reduce our search.
------------------------------------------------------------------------"""
n = int(input())
low = 1
high = n
ans = 0
while low <= high:

    mid = (low + high) // 2

    if mid * mid <= n:

        ans = mid
        low = mid + 1

    else:

        high = mid - 1
print(ans)


"""Search in a 2D Matrix
Problem Statement
Given an M x N matrix where each row is sorted left to right and the first element of each row is greater than
the last element of the previous row. Given a target K, return True if K exists in the matrix, else False. This
appears in TCS NQT to test multi-dimensional search skills.
Example
Input
matrix = [[1,3,5],[7,9,11],[13,15,17]] K =9
Output
True
Approach & Explanation
We treat the entire matrix as a virtual sorted array of size M*N. The index i in this virtual array maps to
matrix[i // N][i % N]. We then run a standard binary search on this virtual array, converting indices as needed.
---------------------------------------------------------------------"""
matrix = [
    [1, 3, 5],
    [7, 9, 11],
    [13, 15, 17]
]
k = int(input())
rows = len(matrix)
cols = len(matrix[0])
low = 0
high = rows * cols - 1
while low <= high:

    mid = (low + high) // 2

    row = mid // cols
    col = mid % cols

    val = matrix[row][col]

    if val == k:
        print(True)
        break

    elif val < k:
        low = mid + 1

    else:
        high = mid - 1
else:
    print(False)

"""Aggressive Cows (Maximize Minimum Distance)
Problem Statement
Given N stalls at positions in a sorted array and C cows, place the cows in the stalls such that the minimum
distance between any two cows is maximized. Return this maximum minimum distance. TCS NQT and
campus drives frequently include this to test advanced binary search thinking.
Example
Input
stalls = [1, 2, 4, 8, 9] C = 3
Output
3
Approach & Explanation
We binary search on the answer — the minimum distance — in the range [1, stalls[-1] - stalls[0]]. For each
candidate mid distance, we greedily check if we can place C cows such that every pair of cows is at least mid
distance apart. We find the largest such mid that still allows valid placement."""
def can_place(stalls, cows, dist):

    count = 1
    last = stalls[0]

    for i in range(1, len(stalls)):

        if stalls[i] - last >= dist:

            count += 1
            last = stalls[i]

        if count >= cows:
            return True

    return False