"""1) While sitting in party, Tom came up with an idea of a quiz.
And the quiz is, Tom will spell out a number, and a person has to tell a number which is next to it. But this number has to be a perfect square.
Example 1
Input
5
Output
9
Explanation
After 5, we have 6, 7, 8 .... and so on.
Here 6 is not a perfect square, and so isn't 7 and 8.
If we proceed to next number, this is 9. This is a perfect square for 3, i.e. 3^2 = 9.Hence the answer is 9.
-------------------------------------------------------------"""
def next_square(n):
    i=1
    while True:
        if i*i>n:
            return i*i
        i+=1
n=int(input())
print(next_square(n))        

"""3) Given an unsorted integer array Arr of N elements. The task is to find the segment in which all elements are in increasing order and which have a maximum sum than the other segment. Print the sum as output.
For example:
Arr[] = {203, 202, 2, 3, 200, 4, 5}
Increasing order segments are:
{2, 3, 200} and 2 + 3 + 200 = 205
{4, 5} and 4 + 5 = 9
So we got a maximum sum of 205 and it's in increasing order.
Hence the output = 205
Constraints
0 < N <= 100
0 < Arr[i] < 1000
Example 1
Input
7
203
202
2
3
200
4
5
Output

205
---------------------------------------------------------------------"""
def max_sum(arr):
    curr_sum=arr[0]
    max_sum=arr[0]
    for i in range(1,len(arr)):
        if arr[i]>arr[i-1]:
            curr_sum+=arr[i]
        else:
            max_sum=max(max_sum,curr_sum)
            curr_sum=arr[i]
    max_sum=max(max_sum,curr_sum)
    return max_sum
            
arr=[203, 202, 2, 3, 200, 4, 5]
print(max_sum(arr))        


"""4) Some of the fastest typists are assigned to type a book written by a famous author. 
Say X can complete typing the book in x days, Y can complete typing the book in y days and so on. 
Given 'N' number of people and the time required by each typist to complete the work (a[]), 
the task here is to find the time required if all the people work together to type the book completely.
Note
Print the value in double/float (up to 2 decimal digits).
e.g. For value 2, print output as 2.00
For value 2.3478, print output as 2.35
Example 1
Input
2
6 2
Output
1.50
Explanation
From the inputs given above:
Assume the time taken is in hours
Number of typists: 2 (X, Y)
Time taken by X to complete a work = 6 hours
Time taken by Y to complete the same work = 2 hours
Work done by X in 1 hour = 1/6
Work done by Y in 1 hour = 1/2
So, total work done by them in 1 hour is 1/6 + 1/2
So, to complete the whole work when both the typists work together, the time taken will be 6/4.
i.e 3/2
Hence, the output is 1.5
-------------------------------------------------------------------"""
n=int(input())
arr=list(map(int, input().split()))
work=0
for i in arr:
    work+=1/i
time=1/work
print(f"{time:.2f}")



"""7) Given a non-negative integer array Arr having size N.
Each element of the array will carry a different value. This means no two elements can have same values. 
The candidate has to do this with minimal changes in the original value of elements,
making every element as least as much value as it originally had.
Find the minimum sum of all elements that can be set the array for.

Input format
The first line of input accept a single positive integer value for N representing the size of Arr[]
The next lines of input accept N number of integer values separated by a new line, 
representing the original values assigned to each element.
Output format
The output must be a non-negative integer only.
Example 1
Input
3
2
2
4
Output
9
Explanation
As two elements have the same value, max value for one of them needs to be incremented to 3.
He can set the array with 2+3+4=9.
Example 2
Input
2
3
4
5
Output
Wrong Input
Explanation
Here N=2, so we need to provide value of only two elements but we are providing value of three elements. So result is "Wrong Input".
Constraints
1 <= N <= 20
1 <= Arr[i] <= 100
-------------------------------------------------------------"""
n=int(input())
arr=[]
for j in range(n):
    arr.append(int(input()))
arr.sort()     
for i in range(1,n):
    while arr[i]<=arr[i-1]:
        arr[i]+=1
print(sum(arr))        


"""8) Write a program to print all the combinations of the given word with or without meaning (when unique characters are given).
Input format
The input consists of a string
Output format
The output prints the permutation of the string in new line
Example 1
Sample Input:
abc
Output:
abc
acb
bac
bca
cab
cba
-------------------------------------------------------"""
def permute(s, ans=""):
    if len(s)==0:
        print(ans)
        return
    for i in range(len(s)):
        ch=s[i]
        remaining=s[:i]+s[i+1:]
        permute(remaining,ans+ch)
s=input()
permute(s)        



"""9) There is a range given n and m in which we have to find the count of all the prime pairs whose difference is 6. We have to find how many sets are there within a given range.
Input format
The first line of input contains the starting range
The second line of input contains the ending range
Output format
The output consists of a single line, print the count prime pairs in a given range. Else print"No Prime Pairs".
Constraints:
2<=n<=1000
n<=m<=2000
Example 1
Input
4
30
Output:
6
Explanation:
(5, 11) (7, 13) (11, 17) (13, 19) (17, 23) (23, 29) . we have 6 prime pairs.
---------------------------------------------------------------------"""
def is_prime(n):
    if n<2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
n=int(input())
m=int(input())

count=0
for i in range(n,m-5):
    if is_prime(i) and is_prime(i+6):
        count+=1

if count>0:
    print(count)
else:
    print("No prime pairs")            
        
"""10) Given a two binary number (in 0 and 1). Find out whether there is a possibility whether these numbers can become equal by rearranging their respective 0’s or 1’s. for e.g 101 and 011 can be re-arranged within them-self to become either 101 or 011.
Example 1
Input
3
101
011
Output
Yes
Explanation
In the above string 101 can be re-arranged as 011 or 110, which matches to the other input which is 011. It means it is possible to make them same, by re-arranging the 0’s and / or 1’s.
So the result is Yes
------------------------------------------------------------------"""
s1=input()
s2=input()
one="1"
c1=0
c2=0
c3=0
c4=0
for i in s1:
    if i==one:
        c1+=1
    else:
        c2+=1
for j in s2:
    if j==one:
        c3+=1
    else:
        c4+=1
if((c1==c3) and (c2==c4)):
    print("Yes")
else:
    print("No")            

"""or"""

s1 = input()
s2 = input()

if s1.count('1') == s2.count('1'):
    print("Yes")
else:
    print("No")