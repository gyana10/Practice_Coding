"Selection Sort"
def selection_sort(arr):
    n=len(arr)
    for i in range(n):
        min_index=i
        for j in range(i+1,n):
            if arr[j]<arr[min_index]:
                min_index=j
        arr[i],arr[min_index]=arr[min_index],arr[i]
    return arr
arr=list(map(int,input().split()))
print(selection_sort(arr))
"""Count Element Frequencies
Exact Exam Question
Given an array that may contain duplicate elements, print every element along with its frequency (number of occurrences).
Example
Input:
8
10 20 20 10 10 20 5 20
Output:
10 -> 3
20 -> 4
5 -> 1"""
n = int(input())
arr = list(map(int,input().split()))
freq = {}
for num in arr:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1
for key in freq:
    print(key, freq[key])
    """Push All Zeros to End
Exact Exam Question
Given an array of integers, move all the zeros to the end of the array while maintaining the relative order of the non-zero elements.
Example 1
Input:
5
1 0 2 0 3
Output:
1 2 3 0 0"""
n = int(input())
arr = list(map(int,input().split()))
pos = 0
for i in range(n):
    if arr[i] != 0:
        arr[pos], arr[i] = arr[i], arr[pos]
        pos += 1
print(*arr)
"""Leaders in an Array
Exact Exam Question
Given an array of integers, print all the leaders in the array.
An element is called a leader if it is greater than all the elements to its right.
The rightmost element is always a leader.
Example
Input:
6
16 17 4 3 5 2
Output:
17 5 2"""
n = int(input())
arr = list(map(int, input().split()))
leaders = []
max_right = arr[-1]
leaders.append(max_right)
for i in range(n - 2, -1, -1):
    if arr[i] > max_right:
        leaders.append(arr[i])
        max_right = arr[i]
leaders.reverse()
print(*leaders)
"""Remove Duplicates from Sorted Array
Exact Exam Question
Given a sorted array, remove the duplicate elements such that each element appears only once.
Print the unique elements (or the count of unique elements depending on the platform).
Example 1
Input:
7
1 1 2 2 3 4 4
Output:
1 2 3 4"""
n = int(input())
arr = list(map(int,input().split()))
j = 0
for i in range(1,n):
    if arr[i] != arr[j]:
        j += 1
        arr[j] = arr[i]
print(*arr[:j+1])
"""Find Missing Number in Array
Exact Exam Question
Given an array containing N-1 numbers from the range:
1 to N
Exactly one number is missing.
Find the missing number.
Example 1
Input:
5
1 2 4 5
Output:
3
Example 2
Input:
6
1 2 3 5 6
Output:
4"""
n = int(input())
arr = list(map(int,input().split()))
expected = n * (n + 1) // 2
actual = sum(arr)
print(expected - actual)
"""Second Largest Element in Array
Exact Exam Question
Given an array of integers, find the second largest element in the array.
If the second largest element does not exist, print:
-1
Example 1
Input:
5
10 20 30 40 50
Output:
40"""
n = int(input())
arr = list(map(int,input().split()))
largest = float('-inf')
second = float('-inf')
for num in arr:
    if num > largest:
        second = largest
        largest = num
    elif num > second and num != largest:
        second = num
if second == float('-inf'):
    print(-1)
else:
    print(second)

"""Maximum Difference (arr[j] - arr[i]) where j > i
Exact Exam Question
Given an array of integers, find the maximum value of:
arr[j] - arr[i]
such that:
j > i
If no positive difference exists, return the maximum difference (which may be negative).
Example 1
Input:
7
2 3 10 6 4 8 1
Output:
8
Explanation
Choose:
10 - 2 = 8
This is the largest possible difference."""    
n = int(input())
arr = list(map(int,input().split()))
min_so_far = arr[0]
max_diff = arr[1] - arr[0]
for i in range(1,n):
    if arr[i] - min_so_far > max_diff:
        max_diff = arr[i] - min_so_far
    if arr[i] < min_so_far:
        min_so_far = arr[i]
print(max_diff)
"""Kadane's Algorithm (Maximum Subarray Sum)
Exact Exam Question
Given an array of integers (may contain positive and negative numbers), find the maximum sum of any contiguous subarray.
A subarray must contain consecutive elements.
Example 1
Input:
8
-2 -3 4 -1 -2 1 5 -3
Output:
7
Explanation
The maximum sum subarray is:
4 -1 -2 1 5
Sum:
4 + (-1) + (-2) + 1 + 5
= 7"""
n = int(input())

arr = list(map(int,input().split()))

current_sum = arr[0]
max_sum = arr[0]

for i in range(1,n):

    if current_sum + arr[i] > arr[i]:
        current_sum = current_sum + arr[i]
    else:
        current_sum = arr[i]

    if current_sum > max_sum:
        max_sum = current_sum

print(max_sum)

"""Count Elements Greater Than All Previous
Given an array of N integers, count how many elements are strictly greater than all the elements before them.
The first element always counts because there are no previous elements.
Example 1
Input
5
7
4
8
2
9
Output
3
Explanation
The elements are:
7 4 8 2 9
The qualifying elements are:
7  → First element ✅
8  → Greater than 7 ✅
9  → Greater than 8 ✅
Answer:
3"""
n = int(input())
max_so_far = -10**18
count = 0
for i in range(n):
    num = int(input())
    if num > max_so_far:
        max_so_far = num
        count += 1
print(count)
"""Cyclic Array Rotation
Given an array of N integers and a positive integer K, perform a right circular rotation of the array by K positions.
After the rotation, print the resulting array.
Example 1
Input
N = 5
Array = 10 20 30 40 50
K = 2
Output
40 50 10 20 30
Example 2
Input
N = 7
Array = 1 2 3 4 5 6 7
K = 3
Output
5 6 7 1 2 3 4"""
n = int(input())
arr = list(map(int, input().split()))
k = int(input())
k = k % n
ans = []
for i in range(n-k, n):
    ans.append(arr[i])
for i in range(n-k):
    ans.append(arr[i])
print(*ans)
"""Right Circular Rotation Queries
You are given:
An array of N integers.
An integer K representing the number of right circular rotations.
Q queries.
After rotating the array K times to the right, answer each query by printing the element present at the given index.
Example
Input
N = 5
K = 2
Q = 3
Array:
1 2 3 4 5
Queries:
0
2
4
Output
4
1
3"""
n, k, q = map(int, input().split())
arr = list(map(int, input().split()))
k = k % n
for i in range(q):
    idx = int(input())
    original = (idx - k + n) % n
    print(arr[original])
"""Count Occurrences in Sorted Array
Given a sorted array and an integer X, count the number of times X appears in the array.
Your solution should have an expected time complexity of:
O(log N)
Example 1
Input
7
1 1 2 2 2 2 3
2
Output
4
Because:
2 appears four times.
Example 2
Input
7
1 1 2 2 2 2 3
4
Output
-1
Because:
4 does not exist in the array."""   
def first(arr,k):
    low=0
    high=len(arr)-1
    ans=-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==k:
            ans=mid
            high=mid-1
        elif arr[mid]<k:
            low=mid+1
        else:
            high=mid-1     
    return ans          
def last(arr,k):
    low=0
    high=len(arr)-1
    ans=-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==k:
            ans=mid
            low=mid+1
        elif arr[mid]<k:
            low=mid+1
        else:
            high=mid-1
    return ans    

n = int(input())
arr = list(map(int, input().split()))
x = int(input())
f = first(arr, x)
if f == -1:
    print(-1)
else:
    l = last(arr, x)
    print(l-f+1)            

"""Between Two Arrays – Common Factors (TCS NQT Medium)
You are given two arrays:
Array A of size n
Array B of size m
Find the number of integers X such that:
Every element of Array A divides X.
X divides every element of Array B.
Print the count of such integers.
Constraints
1 ≤ Elements ≤ 100
Example
Input
2 3
2 4
16 32 96
Here,
A = [2,4]
B = [16,32,96]
Output
3"""    
def common_factors(a,b):
    count=0
    for i in range(1,101):
        valid=True
        for num in a:
            if i%num!=0:
                valid=False
                break
        if valid:
            for num in b:
                if num%i!=0:
                    valid=False
                    break 
        if valid:
            count+=1
    return count
n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
print(common_factors(a,b))  

"""Kangaroo Jump – Same Location Check
Two kangaroos are on a number line.
Kangaroo 1 starts at position x1 and jumps v1 meters every jump.
Kangaroo 2 starts at position x2 and jumps v2 meters every jump.
Determine whether they will land at the same position after the same number of jumps.
If yes, print:
YES
Otherwise, print:
NO
Example 1
Input
0 3 4 2
Meaning
x1 = 0
v1 = 3
x2 = 4
v2 = 2
Output
YES"""
def speed(x1,v1,x2,v2):
    if v1<=v2:
        return "NO"
    if (x2-x1)%(v1-v2)==0:
        return "YES"
    return "NO"
    
x1,v1,x2,v2=map(int,input().split())
print(speed(x1,v1,x2,v2))
"""Bon Appétit (Bill Division)
Anna and Brian went to a restaurant.
They ordered N food items. The cost of each item is given in an array.
Anna did not eat one particular item (at index k), so she should not pay for that item.
Brian calculated Anna's share and charged her b rupees.
Determine whether Brian charged Anna correctly.
If the amount is correct, print:
Bon Appetit
Otherwise, print the amount Brian overcharged Anna.
Example 1
Input
4 1
3 10 2 9
12
Explanation
There are 4 items.
3 10 2 9
Anna didn't eat the item at index 1.
So she didn't eat:
10
Remaining bill:
3 + 2 + 9 = 14
Anna should pay:
14 / 2 = 7
But Brian charged:
12
He overcharged:
12 - 7 = 5
Output
5"""    
def food(arr,k,b):
    total=sum(arr)
    anna=(total-arr[k])//2
    if anna==b:
        return "Bone appetiete"
    else:
        return b-anna
n,k=map(int,input().split())
arr=list(map(int,input().split()))
b=int(input())
print(food(arr,k,b))

"""Migratory Birds (Most Frequent Element)
Given an array of bird IDs, determine which bird type is seen most frequently.
If two or more bird IDs have the same highest frequency, print the smallest bird ID.
Example 1
Input
6
1 4 4 4 5 3
Output
4
Explanation
Frequency table:
Bird ID	Count
1	   1
3	   1
4	   3
5	   1

Bird 4 appears the most.
Example 2
Input
6
1 1 2 2 3 3
Output
1
Explanation
All three bird IDs appear 2 times.
Since there is a tie, print the smallest ID, which is 1."""
def migrat(arr):
    freq={}
    for num in arr:
        if num in freq:
            freq[num]+=1
        else:
            freq[num]=1
    max_count=0
    ans=-1
    for key in freq:
        if freq[key]>max_count:
            max_count=freq[key]
            ans=key
        elif freq[key]==max_count and key<ans:
            ans=key
    return ans

n=int(input())
arr=list(map(int,input().split()))
print(migrat(arr))
          
"""Picking Numbers (TCS NQT Medium)
Given an array of integers, find the length of the longest subarray where the absolute difference between 
any two elements is less than or equal to 1.
Print only the maximum length.
Example 1
Input
6
4 6 5 3 3 1
Output
3
Why?
Possible groups are:
4 5      → Difference = 1 → Length = 2
3 3 4    → Difference = 1 → Length = 3 ✅
5 6      → Difference = 1 → Length = 2
1        → Length = 1
The largest valid group is
3 3 4
Length = 3"""    
def picking_numbers(arr):
    freq = {}
    for num in arr:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    ans = 0
    for num in freq:
        current = freq[num]
        if num + 1 in freq:
            current += freq[num + 1]
        if current > ans:
            ans = current
    return ans
n = int(input())
arr = list(map(int, input().split()))
print(picking_numbers(arr))

"""Divisible Sum Pairs (TCS NQT Medium)
Given an array of N integers and an integer K, count the number of pairs (i, j) such that:
i < j
(arr[i] + arr[j]) % K == 0
Print the total number of such pairs.
Example 1
Input
6 3
1 3 2 6 1 2
Here,
N = 6
K = 3
Array:
1 3 2 6 1 2
Output
5"""
def divisible_pairs(arr, k):
    count = 0
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if (arr[i] + arr[j]) % k == 0:
                count += 1
    return count
n, k = map(int, input().split())
arr = list(map(int, input().split()))
print(divisible_pairs(arr, k))

"""Sales by Match (Sock Merchant)
John has a pile of socks.
Each sock has a color represented by an integer.
Two socks having the same color form one pair.
Find the total number of matching pairs.
Example 1
Input
9
10 20 20 10 10 30 50 10 20
Output
3"""
def sock_pairs(arr):
    freq = {}
    for num in arr:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    pairs = 0
    for key in freq:
        pairs += freq[key] // 2
    return pairs
n = int(input())
arr = list(map(int, input().split()))
print(sock_pairs(arr))

"""Birthday Chocolate (Subarray Division)
Lily has a chocolate bar.
Each square has a number written on it.
Your task is to find how many contiguous segments of length m have a sum equal to d.
Print the number of such segments.
Example 1
Input
5
1 2 1 3 2
3 2

Meaning
Array = [1,2,1,3,2]
d = 3
m = 2
Output
2"""
def birthday(arr, d, m):
    count = 0
    window_sum = sum(arr[:m])
    if window_sum == d:
        count += 1
    for i in range(m, len(arr)):
        window_sum = window_sum - arr[i-m] + arr[i]
        if window_sum == d:
            count += 1
    return count
n = int(input())
arr = list(map(int, input().split()))
d, m = map(int, input().split())
print(birthday(arr, d, m))

"""Breaking the Records (TCS NQT Medium)
Maria is playing a game and her scores for each game are given in an array.
Whenever she scores higher than her highest score so far, she breaks her highest record.
Whenever she scores lower than her lowest score so far, she breaks her lowest record.
Find:
Number of times she breaks her highest score record.
Number of times she breaks her lowest score record.
Print both values.
Example
Input
9
10 5 20 20 4 5 2 25 1
Output
2 4"""
def breaking_records(arr):
    highest = arr[0]
    lowest = arr[0]
    high_count = 0
    low_count = 0
    for i in range(1, len(arr)):
        if arr[i] > highest:
            highest = arr[i]
            high_count += 1
        elif arr[i] < lowest:
            lowest = arr[i]
            low_count += 1
    return high_count, low_count
n = int(input())
arr = list(map(int, input().split()))
high, low = breaking_records(arr)
print(high, low)
"""Apple and Orange (TCS NQT Medium)
Sam's house is located on a number line.
The house starts at position s and ends at position t.
There is:
An apple tree at position a
An orange tree at position b
Apples and oranges fall at different distances from their trees.
A positive distance means the fruit falls to the right of the tree.
A negative distance means the fruit falls to the left of the tree.
Find:
Number of apples that fall on Sam's house.
Number of oranges that fall on Sam's house.
Example
Input
7 11
5 15
3 2
-2 2 1
5 -6
Meaning
House:
7 to 11
Apple Tree:
5
Orange Tree:
15
3 Apples
2 Oranges
Apple Distances:
-2 2 1
Orange Distances:
5 -6
Output
1
1"""
def count_fruits(s, t, a, b, apples, oranges):
    apple_count = 0
    orange_count = 0
    for i in apples:
        position = a + i
        if s <= position <= t:
            apple_count += 1
    for i in oranges:
        position = b + i
        if s <= position <= t:
            orange_count += 1
    return apple_count, orange_count
s, t = map(int, input().split())
a, b = map(int, input().split())
m, n = map(int, input().split())
apples = list(map(int, input().split()))
oranges = list(map(int, input().split()))
apple, orange = count_fruits(s, t, a, b, apples, oranges)
print(apple)
print(orange)

"""Electronics Shop (TCS NQT Medium)
Monica wants to buy one keyboard and one USB drive.
You are given:
An array of keyboard prices.
An array of USB drive prices.
A budget B.
Find the maximum amount Monica can spend without exceeding her budget.
If she cannot buy both items, print:
-1
Example 1
Input
Budget = 60
Keyboards:
40 50 60
USB Drives:
5 8 12
Output
58"""
def elec(k,u,b):
    ans=-1
    for i in k:
        for j in u:
            total=i+j
            if total<=b and total>ans:
                ans=total
    return ans
b = int(input())
n = int(input())
k = list(map(int, input().split()))
m = int(input())
u = list(map(int, input().split()))
print(elec(k,u,b))

"""Cats and a Mouse (TCS NQT Easy–Medium)
Two cats, Cat A and Cat B, are chasing a mouse.
You are given:
Position of Cat A → x
Position of Cat B → y
Position of Mouse C → z
Determine which cat reaches the mouse first.
If Cat A reaches first, print:
Cat A
If Cat B reaches first, print:
Cat B
If both reach at the same time, the mouse escapes. Print:
Mouse C
Example 1
Input
1 2 3
Output
Cat B"""
def cat_mouse(x, y, z):
    d1 = abs(z - x)
    d2 = abs(z - y)
    if d1 < d2:
        return "Cat A"
    elif d2 < d1:
        return "Cat B"
    else:
        return "Mouse C"
x, y, z = map(int, input().split())
print(cat_mouse(x, y, z))

"""Drawing Book (TCS NQT Easy)
A book has n pages.
You need to reach page p.
You can turn pages:
From the front
Or from the back
Find the minimum number of page turns required.
Example 1
Input
6
2
Output
1"""
def page_count(n,p):
    front=p//2
    back=n//2-p//2
    return min(front,back)
n=int(input())
p=int(input())
print(page_count(n,p))

"""Counting Valleys (TCS NQT Medium)
A hiker starts at sea level (0).
He takes N steps.
Each step is represented by:
U → One step Up
D → One step Down
A valley is a sequence of consecutive steps below sea level, starting with a step down from sea level
 and ending with a step up back to sea level.
Find the number of valleys traversed.
Example 1
Input
8
UDDDUDUU
Output
1
Step 1: Understand the Question
The hiker starts at height 0.
Let's follow each step.
Step	Move	Height
Start		      0
U	    +1	      1
D	    -1	      0
D	    -1	     -1
D	    -1	     -2
U	    +1	     -1
D	    -1	     -2
U	    +1	     -1
U	    +1	      0
Visual representation:
Height
 1      /
 0 ----/ \___________/
-1           \     /
-2            \___/
The hiker goes below sea level once and returns to sea level once.
So,
Valleys = 1"""
def counting_valleys(path):
    level = 0
    valleys = 0
    for step in path:
        if step == 'U':
            level += 1
            if level == 0:
                valleys += 1
        else:
            level -= 1
    return valleys
n = int(input())
path = input()
print(counting_valleys(path))
"""Angry Professor (TCS NQT Easy)
A professor is angry because students keep arriving late.
A class is cancelled if fewer than k students arrive on time.
You are given:
n → Total number of students.
k → Minimum number of students required to conduct the class.
An array containing each student's arrival time.
Arrival Time Rules:
Arrival ≤ 0 → Student is on time.
Arrival > 0 → Student is late.
Determine whether the class is cancelled.
Print:
"YES" → If the class is cancelled.
"NO" → If the class is not cancelled.
Example 1
Input
4 3
-1 -3 4 2
Output
YES"""
def angry_professor(arr, k):
    on_time = 0
    for time in arr:
        if time <= 0:
            on_time += 1
    if on_time < k:
        return "YES"
    return "NO"
n, k = map(int, input().split())
arr = list(map(int, input().split()))
print(angry_professor(arr, k))
"""Beautiful Days at the Movies (TCS NQT Easy–Medium)
Lily likes numbers that are beautiful.
A number is called beautiful if:
Reverse the digits of the number.
Find the absolute difference between the original number and the reversed number.
If this difference is perfectly divisible by k, then the number is beautiful.
You are given:
i → Starting number.
j → Ending number.
k → Divisor.
Count how many beautiful numbers are present in the range [i, j].
Print the count.
Example
Input
20 23 6
Output
2"""