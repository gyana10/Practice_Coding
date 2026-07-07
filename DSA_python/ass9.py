"""20) Given an array Arr[] of N integer numbers. The task is to rewrite the array by putting all multiples of 10 at the end of the given array.
Note: The order of the numbers which are not multiples of 10 should remain unaltered, and similarly, the order of all multiples of 10 should be unaltered.
For e.g. Suppose N = 9 and Arr[]={10, 12, 5, 40, 30, 7, 50, 9, 10}
You have to push all multiple of 10 at the end of the Arr[]
Hence, the output is 12 5 7 9 10 40 30 50 10.
Constraints:
1 < N < = 100
.100 < = Arr[i] < = 100
Input Format for Testing:
1. First input line: Accept a single positive integer value for N representing the size of Arr[].
2. Second Input line: Accept N number of integer values separated by a new line.
Output Format for Testing:
1. The output must be N integer numbers separated by a single space character (See the output
format in examples).
2. Additional messages in the output will result in the failure of test cases.
Example 1
Input
9 …. Value of N
10 12 5 40 30 7 50 9 10 … Elements of Arr[]
Output
12 5 7 9 10 40 30 50 10
Example 2
Input
9 ….. Value of N
100 21 5 6 3 7 11 89 10…. Elements of Arr[]
Output
21 5 6 3 7 11 89 100 10
--------------------------------------------------------------"""

n=int(input())
arr=list(map(int,input().split()))
arr1=[]
arr2=[]
for i in arr:
    if i%10==0:
        arr1.append(i)
    else:
        arr2.append(i)
arr[:]=arr2+arr1
print(*arr)            

"""29)
In a mathematics class, a number system is being taught to students. Before teaching them 10's and 100's place, 
they will be taught the number positions. The positions will be starting from sequence number 1, 
and the direction will be from left to right.
So if I want to find the second position of a digit in the number 90876, it will be 0. 
If the Kth digit exceeds the number position return -1.
Write a program to find the Kth digit in a given number.
Example 1
Input
956781
3
Output
6
Explanation
The input by the user is 956781, where 9 is the first digit, 5 is the second digit, 6 is the third digit and so on. The user is asking for the third (3rd) digit in the given number, which is 6.
Input Format
The first line of input contains an integer N
The second line of input contains an integer K
Output Format
The output prints an integer denoting the Kth digit in a given number
-------------------------------------------------------------------------------"""
n=int(input())
p=int(input())
s=str(n)
if p>len(s):
    print(-1)
else:
    print(int(s[p-1]))

"""32) For hiring a car, a travel agency charges R1 rupees per hour for the first N hours and then R2 rupees per hour. 
Given the total time of travel in minutes is X. The task is to find the total traveling cost in rupees.
Note: While converting minutes into hours, ceiling value should be considered as the total number of hours.
For example: If the total travelling time is 90 minutes,
i.e. 1.5 hours, it must be considered as 2 hours.
Example 1
Input
20 ---Value of R1
4 --- Value of N in hours
40 --- Value of R2
300 --- Value of X in minutes
Output
120
Explanation
Total travelling hours = 300/60 = 5 hours
Rupees 20/hours for first 4 hours = 20 * 4 = 80 rupees
Rupees 40/hours in 5th hour = 40 * 1 = 40 rupees
Hence, the total travelling cost = 80 + 40 = 120 rupees
Example 2
Input
30 --- Value of R1
5 --- Value of N in hours.
35 --- Value of R2
500 -- Value of X in minutes
Output
290
Explanation
Total travelling hours = 500/60 = 8.33, Ceiling value of 8.33 = 9 hours
Rupees 30/hours for first 5th hours = 30 * 5 = 150 rupees
Rupees 35/hours in 5th hour = 35 * 4 = 140 rupees
Hence, the total travelling cost = 150 + 140 = 290 rupees
-------------------------------------------------------------------------"""
r1=int(input())
n=int(input())
r2=int(input())
x=int(input())
x1=x/60
if x1==int(x1):
    x1=int(x1)
else:
    x1=int(x1)+1
if x1<=n:
    print(r1*n)
else:
    b1=r1*n
    b2=r2*(x1-n)
    print(b1+b2)    

"""33) There is a bag with three types of gemstones: Ruby of type R, Garnet of type g, and Topaz of type T.
Write a program to find the total number of possible arrangements to make a series of gemstones where no two
gemstones of the same type are adjacent to each other.
Example 1
Input
1-Count of R i.e. Ruby
1-Count of G i.e. Garnet
0-Count of T i.e.
Output
2
Explanation
Arrangements are RG and GR
Example 2
Input
1-Count of R i.e. Ruby
1-Count of G i.e .Garnet
1-Count of T i.e. TopazOutput
6
Explanation
Arrangements are RGTR, GRTR, RGRT, RTGR, RTRG AND TRGR"""
def arrange(r,g,t,last):
    if r==0 and g==0 and t==0:
        return 1
    count=0
    if r>0 and last!='R':
        count+=arrange(r-1,g,t,'R')
    if g>0 and last!='G':
        count+=arrange(r,g-1,t,'G')
    if t>0 and last!='T':
        count+=arrange(r,g,t-1,'T')
    return count             
