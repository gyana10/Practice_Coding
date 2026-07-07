"""Develop a PIN Validation System that verifies whether the PIN entered by a user is correct. 
The system should prompt the user to enter a PIN number and compare it with the predefined PIN 1404. 
If the entered PIN matches the predefined PIN, an appropriate success message should be displayed; otherwise,
 an error message should be shown. After each validation attempt, the system should ask the user whether they wish to continue.
   If the user chooses to continue, the system should again prompt for a PIN number. 
   This process should repeat until the user decides to exit the system. 
   The program should terminate gracefully when the user chooses not to continue."""
choice="yes"
while choice.lower()=="yes":
    pin=int(input("Enter the PIN: "))
    if pin==1404:
        print("PIN is correct. Access granted.")
    else:
        print("Incorrect PIN. Access denied.")
    choice=input("Do you want to continue? (yes/no): ")
print("Exiting the system. Goodbye!")
    
"ALL Zeros Matrix: Write a program that takes an integer input n and creates an n x n matrix filled with zeros."
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
       rows=len(matrix)
       cols=len(matrix[0])

       rows_set=set()
       cols_set=set()

       for i in range(rows):
           for j in range(cols):
               if matrix[i][j]==0:
                   rows_set.add(i)
                   cols_set.add(j)

       for i in range(rows):
           for j in range(cols):
               if i in rows_set or j in cols_set:
                   matrix[i][j]=0    

" "           
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i = 0
        j = 0
        merge = []

        while i < len(nums1) and j < len(nums2):

            if nums1[i] > nums2[j]:
                merge.append(nums2[j])
                j += 1
            else:
                merge.append(nums1[i])
                i += 1

        while i < len(nums1):
            merge.append(nums1[i])
            i += 1

        while j < len(nums2):
            merge.append(nums2[j])
            j += 1

        n = len(merge)

        if n % 2 == 1:
            return merge[n // 2]
        else:
            return (merge[n//2 - 1] + merge[n//2]) / 2        