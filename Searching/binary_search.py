"""Binary Search is an efficient searching algorithm used to find an element in a sorted array.
Instead of checking every element one by one, it repeatedly divides the search space into half.
Example
Array:
[10, 20, 30, 40, 50, 60, 70]
Find: 50
Middle = 40
50 > 40 → Search right half
Middle = 60
50 < 60 → Search"""
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

"""Average Case
O(log n)"""