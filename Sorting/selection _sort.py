#write program to implement selection sort
# Selection sort is a simple comparison-based sorting algorithm that works by repeatedly selecting the smallest (or
# largest) element from the unsorted portion of the list and swapping it with the first unsorted element until the entire
#  list is sorted.
def selection_sort(arr):
    n=len(arr)
    for i in range(n):
        min_index=i
        for j in range(i+1,n):
            if arr[j]<arr[min_index]:
                min_index=j
        arr[i],arr[min_index]=arr[min_index],arr[i]
    return arr