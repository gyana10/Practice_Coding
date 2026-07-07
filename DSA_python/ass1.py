"""66. Consider the following series: 1,1,2,3,4,9,8,27,16,81,32,243,64,729,128,2187....
This series is a mixture of 2 series : all the odd terms in this series form a geometric series and all the
even terms form yet another geometric series.
Write a program to find the Nth term in the series.
Explantion : The value N is a positive integer that should be read from STDIN. The Nth term that is
calculated by the program should be written to STDOUT. Other than the value of the nth term, no other
character/string or message should be written to STDOUT.
For example: if N=16, the 16th term in the series is 2187, so only value 2187 should be printed to
STDOUT."""
n=int(input())
if n%2!=0:
    print(2**(n//2))
else:
    print(3**((n//2)-1))

"""68. Consider the following series: 0,0,2,1,4,2,6,3,8,4,10,5,12,6,14,7,16,8
This series is a mixture of 2 series, all the odd terms in this series form even numbers in ascending order and every even terms is derived from the previous term using the formula (x/2).Write a program to find
the nth term in this series.
Explantion : The value of n is a positive integer that should be read from STDIN and the nth term that is
to be calculated by the program should be written to STDOUT. Other than the value of the nth term, no
other characters /strings or message should be written to STDOUT.
For example:If n=10, the 10th term in the series is to be derived from the 9th term in the series. The 9th
term is 8 so the 10th term is (8/2)=4. Only the value 4 should be printed to STDOUT.
You can assume that the n will not exceed 20,000.
// Find the Nth term in the series
-----------------------------------------------------------"""
n = int(input())

if n % 2 == 1:
    print(2 * (n // 2))
else:
    print((n // 2) - 1)



"""77. Alice had to go to play with his friends. But his brother is
not leaving. So, he thought to ask a question so that in the meantime he can go. So, The problem is as
follows: He will be given Numbers n.m and k. Calculate T.(T=(nm)/k).His brother has to find the three
coordinates of the XX plane (2D points) such that the area of the triangle formed by those points should
be equal to T. If there is any solution print YES. else NO.
NOTE: 1 ≤x1,y1, x2,y2, x3, y3 ≤ 109
Example 1:
Input:
4 3 3
Output:
YES
Explanation:
One possible way is (1,0), (2.3) and (4.1) are the points where there area is equal to T
Example - 2
Input:
447
-----------------------------------------------------------"""
n, m, k = map(int, input().split())

if (n * m) % k == 0:
    print("YES")
else:
    print("NO")

"""54. Problem Statement
A doctor has a clinic where he serves his patients. The doctor’s consultation fees are different for
different groups of patients depending on their age. If the patient’s age is below 17, fees is 200 INR. If the
patient’s age is between 17 and 40, fees is 400 INR. If patient’s age is above 40, fees is 300 INR. Write a
code to calculate earnings in a day for which one array/List of values representing age of patients visited
on that day is passed as input.
Note:
•Age should not be zero or less than zero or above 120
•Doctor consults a maximum of 20 patients a day
•Enter age value (press Enter without a value to stop):
Example 1:
Input
20
30
40
50
2
3
14
Output Total Income 2000 INR
Note: Input and Output Format should be same as given in the above example.
For any wrong input display INVALID INPUT
Output Format
Total Income 2100 INR
--------------------------------------------------"""
income = 0

while True:
    try:
        age = input()

        if age == "":
            break

        age = int(age)

        if age <= 0 or age > 120:
            print("INVALID INPUT")
            exit()

        if age < 17:
            income += 200
        elif age <= 40:
            income += 400
        else:
            income += 300

    except:
        break

print("Total Income", income, "INR")

"""58. Find the number of students whose height is less than the height of their adjacent students.
Problem Statement
A physical education teacher asks students to assemble in a straight line for the morning assembly.Given
an array of N in which each element represents the height of the student in that position. The task here is
to find the number of students whose height is less than the height of their adjacent students.
Input: 35, 15, 45,25,55 Output: 2 (35>15<45 and 45>25<55)
-------------------------------------------------------"""
arr = list(map(int, input().split()))

count = 0

for i in range(1, len(arr) - 1):
    if arr[i] < arr[i - 1] and arr[i] < arr[i + 1]:
        count += 1

print(count)

"""given 2 strings of lowercase english letters p and q. the following operations:
lengths are true if the two string are equalelse print the ASCII value of last letter of second string.
Count the vowels for each string and print the sum of all vowels(from both the strings). """

def count_vowels(s):
    c=0
    vowels="aeiou"
    for i in s.lower():
        if i in vowels:
            c+=1
    
    return c            
def equal(s1,s2):
    if len(s1)==len(s2):
        return True
    else:
        return (ord(s2[-1]))        

s1="Gyana"
s2="Ranjan"
c1=(count_vowels(s1))
c2=(count_vowels(s2))
print("Total vowels : ",c1+c2)
print(equal(s1,s2))

     