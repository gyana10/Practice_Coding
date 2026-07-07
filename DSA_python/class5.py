"""28. We define the distance between two array values as the number of indices between the two
values.
Given a, find the minimum distance between any pair of equal elements in the array. If no such
value exists, print-1.
----------------------------------------------------------------------------"""
def minimumDistances(arr):

    last_seen = {}

    ans = float('inf')

    for i in range(len(arr)):

        if arr[i] in last_seen:

            distance = i - last_seen[arr[i]]

            ans = min(ans, distance)

        last_seen[arr[i]] = i

    if ans == float('inf'):
        return -1

    return ans


arr = list(map(int, input().split()))

print(minimumDistances(arr))


"""31. Consider an array of numeric strings where each string is a positive number with anywhere from 1to
10^6 digits. Sort the array’s elements in non-decreasing, or ascending order of their integer values and
print each element of the sorted array on a new line."""
def bigSorting(arr):

    arr.sort(key=lambda x: (len(x), x))

    return arr


n = int(input())

arr = []

for i in range(n):
    arr.append(input())

result = bigSorting(arr)

for num in result:
    print(num)


"""SELECION SORT"""
def selection_sort(a):
    for i in range(len(a)):
        low=i
        for j in range(i+1,len(a)):
            if a[j]<a[low]:
                low=j
        a[i],a[low]=a[low],a[i]
    return a
a=[14,33,27,10,35,19,42,44]
print(selection_sort(a))
