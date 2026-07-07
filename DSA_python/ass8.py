"""4. Collision CourseProblem Description
On a busy road, multiple cars are passing by. A simulation is run to see what happens if brakes fail for all cars on the road.
The only way for them to be safe is if they don't collide and pass by each other. The goal is to identify whether any of the given
 cars would collide or pass by each other safely around a Roundabout. Think of this as a reference point O 
( Origin with coordinates (0,0) ), but instead of going around it, cars pass through it.
Considering that each car is moving in a straight line towards the origin with individual uniform speed. 
Cars will continue to travel in that same straight line even after crossing origin. 
Calculate the number of collisions that will happen in such a scenario.
Note : - Calculate collisions only at origin. Ignore the other collisions. 
Assume that each car continues on its respective path even after the collision without change of direction or speed for an 
infinite distance.Constraints
1<=C<=10^5
-10^9 <= x,y <= 10^9
0 < v < 10^9.Input Format
The first line contains an integer C, denoting the number of cars being considered that are passing by around the origin.
Next C lines contain 3 space delimited values, first two of them being for position coordinates (x,y) in 2D space and the third one for speed (v).Output
A single integer Q denoting the number of collisions at origin possible for given set of cars.Test Case
 Explanation
Example 1
Input
5
5 12 1
16 63 5
-10 24 2
7 24 2
-24 7 2
Output
4
Explanation
Let the 5 cars be A, B, C, D, and E respectively.
4 Collisions are as follows -
1) A & B.
2) A & C.
3) B & C.
4) D & E.
---------------------------------------------------------------------------"""
n = int(input())

arr = []

for _ in range(n):

    x, y, v = map(int, input().split())

    arr.append((x*x + y*y, v*v))

count = 0

for i in range(n):

    for j in range(i+1, n): 

        if arr[i][0] * arr[j][1] == arr[j][0] * arr[i][1]:
            count += 1

print(count)

"""5. Death BattleProblem Description
In a crossover fantasy universe, Houin Kyoma is up in a battle against a powerful monster Nomu that can kill him in a single blow.
However being a brilliant scientist Kyoma found a way to pause time for exactly M seconds. Each second, Kyoma attacks Nomu with
 certain power, which will reduce his health points by that exact power. Initially Nomu has H Health Points. 
Nomu dies when his Health Points reach 0. Normally Kyoma performs Normal Attack with power A. Besides from Kyoma’s brilliance,
 luck plays a major role in events of this universe. Kyoma’s Luck L is defined as probability of performing a super attack. 
 A super attack increases power of Normal Attack by C. Given this information calculate and print the probability that Kyoma 
 kills Nomu and survives. If Kyoma dies print “RIP”.Constraints
0 < T <= 50
1 <= A, H, C, L1, L2 <= 1000
1 <= M <= 20.
L1<=L2Input Format
First line is integer T denoting number of test cases.
Each test case consist of single line with space separated numbers A H L1 L2 M C.
 Where luck L is defined as L1/L2. Other numbers are, as described above.Output
Print probability that Kyoma kills Nomu in form P1/P2 where P1<=P2 and gcd(P1,P2)=1.
If impossible, print “RIP” without quotes.
Test Case
 Explanation
Example 1
Input
2
10 33 7 10 3 2
10 999 7 10 3 2
Output
98/125
RIP
------------------------------------------------"""
def gcd(a,b):
    while b:
        a,b=b,a%b
    return a
def comb(n,r):
    if r>n:
        return 0
    ans=1
    for i in range(r):
        ans = ans * (n - i) // (i + 1)
    return ans
t = int(input())

for _ in range(t):

    A, H, L1, L2, M, C = map(int, input().split())

    max_damage = M * (A + C)

    if max_damage < H:
        print("RIP")
        continue

    base_damage = M * A

    need = H - base_damage

    if need <= 0:
        print("1/1")
        continue

    req = (need + C - 1) // C

    num = 0
    den = L2 ** M

    for k in range(req, M + 1):

        ways = comb(M, k)

        num += ways * (L1 ** k) * ((L2 - L1) ** (M - k))

    g = gcd(num, den)

    print(f"{num//g}/{den//g}")


"""6. Work LifeProblem Description
Jay works for support project where he has to resolve some tickets each day (denoted by A[i]). He knows, ahead of time, 
the number of tickets for each day for N days. Let A be an array of length N. Each element A[i] (where i=1 to i=N) denotes
 number of tickets to resolve on ith day. Jay is struggling to balance his work life. On some days, workload is huge and on
   other days, it is very little. Now he can procrastinate and choose to postpone up to K tickets to next day. 
   However, tickets can only be postponed once. (Refer example 2 for more clarity). 
   Find optimal solution where workload can be distributed as evenly as possible with above constraints and print the 
   maximum number of tickets he needs to resolve on given days.Constraints
1 <= T <= 50
1 <= N <= 100
1 <= K <= 100
1 <= A[i] <= 10^9Input Format
First line is integer T denoting number of test cases.
For each test case:
First line is N K described above
Next line is N spaced integers denoting number of tickets for each dayOutput
For each test case, print a single integer per line denoting maximum number of tickets Jay needs to resolve after optimal 
rearrangement with above constraints.
Test Case
 Explanation
Example 1
Input
2
3 100
3 1 2
3 1532
28 31 37
Output
2
37
Explanation
Initially highest workload is on first day (3 tickets). Now 1 ticket should be postponed from day 1 to day 2. 
So array is [2,2,2] and maximum workload is 2. For second testcase, no rearrangement is required, hence the output is 37.
Example 2:
Input:
1
3 100
7 1 1
Output:
4
Explanation:  
Initially highest workload is on first day (7 tickets). Now we postpone 4 tickets from day 1 to day 2. 
Array now looks like [3,5,1]. Now on day 2, even K is 100, we can only postpone 1 ticket since tickets can only be postponed once. 
(In other words, 4 tickets out 5 which were postponed from day 1 has to be resolved on day 2. They cannot be postponed any further).
So after postponing 1 ticket array looks like [3,4,2] and maximum workload is 4, hence answer is 4."""