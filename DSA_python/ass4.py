"""32. Write a program to check whether a given number is a happy number or an unhappy number.
Happy number: Starting with any positive integer, replace the number by the sum of the squares of its
digits, and repeat the process until the number equals 1, or it loops endlessly in a cycle which does not
include 1.
-----------------------------------------------------"""
def happy(n):
    seen=set()
    while n!=1 and n not in seen:
        seen.add(n)
        total=0
        while n>0:
            digit=n%10
            total+=digit*digit
            n//=10
        n=total
    if n==1:
        return "Happy Number"
    else:
        return "Unhappy Number"
n=int(input("Enter a number: "))
result=happy(n)    
print(result)

"""20. You are choreographic a circus shows with various animals. For one act, you are given two
kangaroos on a number line ready to jump in the positive (i.e towards positive infinity).• The first kangaroos start at location x1 and move at a rate of v1 meter per jump.
• The second kangaroos start at location x2 and move at a rate of v2 meters per jump.
You have to figure out a way to get both kangaroos at the same location at the same time as part of
the shows. If it is possible, return YES, otherwise return NO.
For example: – kangaroos 1 starts at x1=2 with a jump distance v1=1 and kangaroos 2 starts at x2=1
with a jump distance of v2. After on jump, they are both at x=3. (x1+v1=2 x2+v2=1+2), So our answer
is YES.
-----------------------------------------------------------"""
def kangaroo(x1, v1, x2, v2):

    for _ in range(10000):

        if x1 == x2:
            return "YES"

        x1 += v1
        x2 += v2

    return "NO"


print(kangaroo(2, 1, 1, 2))

"""24. Anna and Brian are sharing a meal at a restaurant and they agree to split the bill equally. Brian
wants to order something that Anna is allergic to though, and they agree that Anna won’t pay for
that item. Brian gets the check and calculates Anna’s portion. You must determine if his
calculation is correct.
For example, assume the bill has the following prices:bill=[2,4,6]. Anna declines to eat item k=bill[2]
which costs 6. If Brian calculates the bill correctly, Anna will pay (2+4)/2=3. If he includes the cost of
bill[2],he will calculate (2+4+6)/2 = 6. In the second case, he should refund 3 to Anna
--------------------------------------------------------------"""
def bon_appetit(bill, k, charged):

    actual_share = (sum(bill) - bill[k]) // 2

    if actual_share == charged:
        print("Bon Appetit")
    else:
        print(charged - actual_share)


bill = [2, 4, 6]
k = 2
charged = 6

bon_appetit(bill, k, charged)


"""25. The Utopian Tree goes through 2 cycles of growth every year. Each spring, it doubles in height.
Each summer, its height increases by 1 meter. Laura plants a Utopian Tree sapling with a height
of 1 meter at the onset of spring. How tall will her tree be after growth cycles?
For example, if the number of growth cycles is n=5, the calculations are as follows:
Periods Height
• 1
• 2
• 3
• 6
• 7
• 14-------------------------------------------------------------"""
def utopian_tree(n):

    height = 1

    for i in range(n):

        if i % 2 == 0:
            height *= 2
        else:
            height += 1

    return height


print(utopian_tree(5))

"""26. John Watson knows of an operation called a right circular rotation on an array of integers. One
rotation operation moves the last array element to the first position and shifts all remaining
elements right one. To test Sherlock’s abilities, Watson provides Sherlock with an array of
integers. Sherlock is to perform the rotation operation a number of times then determine the
value of the element at a given position.
For each array, perform a number of right circular rotations and return the value of the element at
a given index.
For example, array a=[3,4,5], number of rotation, k=2 and indices to check, .
m=[1,2] First we perform the two rotations:
[3,4,5]à [5,3,4]à [4,5,3]
Now return the values from the zero-based indices 1 and 2 as indicated in the m array.
a[1]=5
a[2]=3    """


def circular_rotation(arr, k, queries):

    n = len(arr)

    k = k % n

    rotated = arr[-k:] + arr[:-k]

    for q in queries:
        print(rotated[q])


arr = [3, 4, 5]
k = 2
queries = [1, 2]

circular_rotation(arr, k, queries)