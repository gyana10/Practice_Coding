#Given two non-negative integers n1 and n2, count the number of integers in the inclusive range [n1, n2] whose digits are all distinct.
#A number is considered valid if no digit appears more than once in its decimal representation.
#Example 1
#Input:
#n1=11,n2=15
#Numbers in the range:
#11, 12, 13, 14, 15
#11 → Invalid (digit 1 repeats)
#12 → Valid
#13 → Valid
#14 → Valid
#15 → Valid
#Output:
#4
#Example 2
#Input:
#101 
#200
#Output:
#72
def count_unique(n1,n2):
    count=0
    for i in range(n1,n2+1):
        s=str(i)
        if len(s)==len(set(s)):
            count+=1
    return count  
n1=int(input())
n2=int(input())
result=count_unique(n1,n2)
print(result)      

#2. Count Numbers Having At Least One Repeated Digit
#Question:
#Count numbers in a range whose digits repeat at least once.
#Example:
#Input:
#11 15
#Output:
#1
def count_repeated(n1,n2):
    count=0
    for i in range(n1,n2+1):
        s=str(i)
        if len(s)!=len(set(s)):
            count+=1
    return count  
n1=int(input())
n2=int(input())
result=count_repeated(n1,n2)
print(result)   

