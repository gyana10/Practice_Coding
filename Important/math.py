"""Happy Number"""
def square(n):
    total=0
    while n>0:
        digit=n%10
        total+=digit*digit
        n//=10
    return total
def happy(n):
    seen=set()
    while n!=1 and n not in seen:
        seen.add(n)
        n=square(n)
    return n==1
n = int(input())
if happy(n):
    print("Happy")
else:
    print("Not Happy")    

"""Given a number n.
Check every digit of n.
Count how many digits divide n completely
Important
If the same digit appears multiple times, count each occurrence separately. """

n=int(input())
temp=n
count=0
while temp!=0:
    digit=temp%10
    if digit!=0 and n%digit==0:
        count+=1
    temp//=10
print(count)      

"""UNO – Digit Sum Reduction
Question
Keep adding digits of the number until you get a single digit.
If the final single digit is:
1
Print:
UNO
Otherwise print:
Not UNO"""
n=int(input())
while n>9:
    total=0
    while n>0:
        total+=n%10
        n//=10
    n=total
if n==1:
    print("UNO")
else:
    print("Not UNO")    

"""Oddly Even – Digit Position Difference
Question
Given a number, find:
| Sum of digits at even positions - Sum of digits at odd positions |
Return the absolute difference.
Example
Input:
4567
Positions are counted from left to right:
Position	Digit
1 (Odd)	     4
2 (Even)	 5
3 (Odd)	     6
4 (Even)	 7
Odd Position Sum
4 + 6 = 10
Even Position Sum
5 + 7 = 12
Difference:
|12 - 10| = 2
Output:
2  """          
n=input()
odd=0
even=0
for i in range(len(n)):
    if (i+1)%2==1:
        odd+=int(n[i])
    else:
        even+=int(n[i])
print(abs(even-odd))          

"""Sweet Seventeen – Base-17 to Decimal
Question
Convert a Base-17 number into Decimal.
In Base-17:
0-9  => 0 to 9
A    => 10
B    => 11
C    => 12
D    => 13
E    => 14
F    => 15
G    => 16
Example
Input:
1A
Meaning:
1 × 17¹ + A × 17⁰
Since:
A = 10
Calculate:
1 × 17 + 10 × 1
17 + 10
27
Output:
27"""
s = input().strip()

power = len(s) - 1
decimal = 0

for ch in s:

    if '0' <= ch <= '9':
        value = ord(ch) - ord('0')

    elif 'A' <= ch <= 'G':
        value = ord(ch) - ord('A') + 10

    else:
        value = ord(ch) - ord('a') + 10

    decimal += value * (17 ** power)

    power -= 1

print(decimal)

"""Two-Wheeler & Four-Wheeler Count
This is one of the most repeated TCS NQT questions.
Question
You are given:
V = Total Vehicles
W = Total Wheels
Find:
TW = Number of Two-Wheelers
FW = Number of Four-Wheelers
Example
Input:
V = 200
W = 540
Output:
TW = 130
FW = 70"""
def vehicles(v,w):
    if w%2!=0 or w<2*v or w>4*v:
        print("INVALID INPUT")
    else:
        fw=(w-2*v)//2
        tw=v-fw
        print("Two wheller :",tw," Four wheller :",fw)
        
v=int(input())
w=int(input())
vehicles(v,w)

"""Count Numbers Without Repeated Digits
Question
Given:
n1
n2
Count how many numbers in the range:
[n1 , n2]
have no repeated digits.
Example 1
Input:
11
15
Numbers:
11
12
13
14
15
Check one by one.
11
Digits:
1 1
Repeated.
❌ Not counted.
12
Digits:
1 2
Unique.
✅ Count
13
Unique.
✅ Count
14
Unique.
✅ Count
15
Unique.
✅ Count
Answer:
4"""
def count_non_dupli(n1,n2):
    count=0
    for i in range (n1,n2+1):
        if len(str(i))==len(set(str(i))):
            count+=1
           
    print(count)        
n1=int(input())
n2=int(input())
count_non_dupli(n1,n2)
"""Mixed Fibonacci & Prime Series – Nth Term
Question
Series:
1, 2, 1, 3, 2, 5, 3, 7, 5, 11, 8, 13, ...
Find the Nth term.
First Observation
Let's write positions.
Position	Value
  1	         1
  2	         2
  3	         1
  4	         3
  5	         2
  6	         5
  7	         3
  8	         7
  9	         5
  10	     11
  11	     8
  12	     13
Odd Positions
Take:
1st
3rd
5th
7th
9th
11th
Values:
1, 1, 2, 3, 5, 8
This is:
Fibonacci Sequence
Even Positions
Take:
2nd
4th
6th
8th
10th
12th
Values:
2, 3, 5, 7, 11, 13
This is:
Prime Numbers"""
def fib(n):

    a = 1
    b = 1

    if n <= 2:
        return 1

    for _ in range(3, n+1):

        c = a + b

        a = b
        b = c

    return b


def prime(n):

    count = 0
    num = 2

    while True:

        is_prime = True

        for i in range(2, num):

            if num % i == 0:
                is_prime = False
                break

        if is_prime:

            count += 1

            if count == n:
                return num

        num += 1


n = int(input())

if n % 2 == 1:

    pos = n//2 + 1

    print(fib(pos))

else:

    pos = n//2

    print(prime(pos))

    """Mixed Geometric & Power Series – Nth Term

Question

Series:

1, 1, 2, 3, 4, 9, 8, 27, 16, 81, 32, 243, ...

Find the Nth term.

Step 1: Separate Odd and Even Positions
Position	Value
  1	          1
  2	          1
  3	          2
  4	          3
  5	          4
  6	          9
  7	          8
  8	          27
  9	          16
 10	          81"""
def series(n):
    if n%2==1:
        pos=(n+1)//2
        print(2**(pos-1))
    else:
        pos=n//2
        print(3**(pos-1))
n=int(input())
series(n)

"""Mixed Even & Half Series – Nth Term
Given Series
0, 0, 2, 1, 4, 2, 6, 3, 8, 4, 10, 5, ...
Find the Nth term.
First Step: Separate Odd and Even Positions
Position	Value
   1	      0
   2	      0
   3	      2
   4	      1
   5	      4
   6	      2
   7	      6
   8	      3
   9	      8
  10	      4
  11	     10
  12	      5"""
def series_even(n):
    if n%2==1:
        pos=(n+1)//2
        print(2*(pos-1))
    else:
        pos=n//2
        print(pos-1)
n=int(input())
series_even(n)

"""Alice's Triangle Area Problem
Don't get scared by the word Triangle.
Question
Given:
n
m
k
Calculate:
T = (n × m) / k
Determine whether T is an integer.
If yes:
YES
Otherwise:
NO"""
def alice_triangle(n,m,k):
    res=(n*m)/k 
    if res==int(res):
        print("Yes")
    else:
        print("No")
n,m,k=map(int,input().split())
alice_triangle(n,m,k)

"""Coin Vend Combinations
A vending machine accepts only ₹1 and ₹2 coins.
You need to find the number of ways to make a sum R using these coins.
Constraint
Two ₹2 coins cannot appear consecutively.
Return the total number of valid combinations.
Example 1
Input
3
Output
3
Explanation
Valid combinations:
1 + 1 + 1
1 + 2
2 + 1
Total:
3"""
def vending(n):
    if n==0:
        return 1
    if n==1:
        return 1
    if n==2:
        return 2
        
    a=1
    b=1
    c=2
    for i in range(3,n+1):
        d=c+a 
        a=b 
        b=c 
        c=d 
    return c    
n=int(input())
print(vending(n))
"""Minting Mints – Queue Sum
Problem Statement
There are N kids standing in a queue.
The first kid has S mints.
Every next kid gets:
(sum of all mints given to previous kids) - 1
Find the total number of mints possessed by all kids in the queue.
Example 1
Input
4 2
Meaning:
S = 4
N = 2
Output
7
Explanation
Kid 1:
4
Kid 2:
4 - 1
= 3
Total:
4 + 3 = 7"""
def mints(s,n):
    total=s
    for i in range(1,n):
         total=2*total-1
    return total
s,n=map(int,input().split())
print(mints(s,n))

"""Chocolate Game – Box Remainder
Problem Statement
A box contains N chocolates.
Bob takes X chocolates.
Alice gets the remaining chocolates:
Alice = N - X
Now a game starts.
Rules
If one person has more chocolates than the other, the person with more chocolates gives away chocolates equal to the 
amount held by the other person.
Repeat until:
both have equal chocolates, OR
one person reaches 0 chocolates.
Find the number of chocolates left in the box after the game.
Example 1
Input
10 4
Meaning:
N = 10
Bob = 4
Alice = 6
Output
6"""
def choco(n,b):
    a=n-b
    if a==b:
        print(n-(a+b))
        return
    while b!=a:
        if a>b:
            a=a-b

        else:
            b=b-a
    return (n-(a+b))
    
n=10
b=4
print(choco(n,b))

"""Count Even Sum Permutations
Problem Statement (TCS NQT Style)
Given three integers:
low, high, K
You can choose exactly K numbers from the range:
[low, high]
Repetition is allowed.
Count the number of permutations whose sum is even.
Print the answer modulo:
1000000007
Example 1
Input
4 5
3
Output
4
Explanation
Available numbers:
4, 5
Parity:
4 → Even
5 → Odd
Choose 3 numbers.
Valid permutations:
4 4 4
4 5 5
5 4 5
5 5 4
All have even sum.
Count:
4""" 
MOD = 1000000007

low, high = map(int, input().split())
K = int(input())

even = 0
odd = 0

for i in range(low, high + 1):

    if i % 2 == 0:
        even += 1
    else:
        odd += 1

even_sum = even
odd_sum = odd

for _ in range(K - 1):

    new_even = even_sum * even + odd_sum * odd

    new_odd = even_sum * odd + odd_sum * even

    even_sum = new_even % MOD
    odd_sum = new_odd % MOD

print(even_sum)
"""Derangements – Book Exchange
Problem Statement (TCS NQT Style)
There are N students and N books.
Each student originally owns exactly one book.
Now all books are shuffled and redistributed.
Find the number of ways such that:
No student gets his/her own book back.
This is called a Derangement.
Print the answer modulo:
100000007
Example 1
Input
4
Output
9
Example 2
Input
3
Output
2"""
MOD = 100000007

def derangement(n):

    if n == 1:
        return 0

    if n == 2:
        return 1
    a = 0     
    b = 1      
    for i in range(3, n + 1):

        c = ((i - 1) * (a + b)) % MOD

        a = b
        b = c

    return b

n = int(input())
print(derangement(n))
"""Round Table Seating Arrangements
Problem Statement (TCS NQT Style)
There are R round tables and N attendees.
Find the number of unique seating arrangements.
Important Rule
For a round table:
Rotations are considered identical.
That means:
A B C
and
B C A
and
C A B
are considered the same arrangement.
If N is not divisible by R:
Distribute attendees as equally as possible.
Example
Input
R = 2
N = 5
Output
10
"""
def fact(n):
    ans = 1
    for i in range(2,n+1):
        ans *= i
    return ans
n = int(input())
print(fact(n-1))

