#Write a code to perform merge sort
# Merge sort is a divide-and-conquer algorithm that works by recursively dividing the input array into smaller subarrays until 
# each subarray contains a single element. Then, it merges those subarrays back together in a sorted order to produce the 
# final sorted array.
def merge_sort(arr):
    if len(arr)>1:
        mid=len(arr)//2
        L=arr[:mid]
        R=arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i=j=k=0

        while i<len(L) and j<len(R):
            if L[i]<R[j]:
                arr[k]=L[i]
                i+=1
            else:
                arr[k]=R[j]
                j+=1
            k+=1

        while i<len(L):
            arr[k]=L[i]
            i+=1
            k+=1

        while j<len(R):
            arr[k]=R[j]
            j+=1
            k+=1
    return arr
arr=[38,27,43,3,9,82,10]
print(merge_sort(arr))


"""Time: O(n log n)
   Space: O(n)"""