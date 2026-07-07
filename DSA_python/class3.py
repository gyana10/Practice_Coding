"""33. John works at a clothing store. He has a large pile of socks that he must pair by color for sale. Given an
array of integers representing the color of each sock, determine how many pairs of socks with
matching colors there are.
Function Description:
Complete the sockMerchant() function in the editor below. It must return an integer representing the
number of matching pairs of socks that are available.
sockMerchant has the following parameter(s):
n: the number of socks in the pile
ar: the colors of each sock.
Input Format
The first line contains an integer, the number of socks represented in.
The second line contains space-separated integers describing the colors of the socks in the pile.
Output Format
Return the total number of matching pairs of socks that John can sell.
Sample Input
9
10 20 20 10 10 30 50 10 20
Sample Output
3"""
def sockMerchant(arr):

    freq = {}

    for sock in arr:
        freq[sock] = freq.get(sock, 0) + 1

    pairs = 0

    for count in freq.values():
        pairs += count // 2

    return pairs


n = int(input())
arr = list(map(int, input().split()))

print(sockMerchant(arr))





"""21. You will be given two arrays of integers and asked to determine all integer that satisfies the
following two conditions:
1. The elements of the first array are all factors of the integer being considered
2. The integer being considered is a factor of all elements of the second array.
These numbers are referred to as being between the two arrays. You must determine how much
such a number exists."""

def getTotalX(a, b):

    count = 0

    for x in range(max(a), min(b) + 1):

        valid = True

        for num in a:
            if x % num != 0:
                valid = False
                break

        for num in b:
            if num % x != 0:
                valid = False
                break

        if valid:
            count += 1

    return count


a = list(map(int, input().split()))
b = list(map(int, input().split()))

print(getTotalX(a, b))




"""46. Selection of MPCS exams include a fitness test which is conducted on ground. There will be a batch of 3
trainees, appearing for running test in track for 3 rounds. You need to record their oxygen level after
every round. After trainee are finished with all rounds, calculate for each trainee his average oxygen level
over the 3 rounds and select one with highest oxygen level as the most fit trainee. If more than one
trainee attains the same highest average level, they all need to be selected.
Display the most fit trainee (or trainees) and the highest average oxygen level.
Note:
• The oxygen value entered should not be accepted if it is not in the range between 1 and 100.
• If the calculated maximum average oxygen value of trainees is below 70 then declare the
trainees as unfit with meaningful message as “All trainees are unfit.
• Average Oxygen Values should be rounded.
Example 1:
----------
INPUT VALUES
95
92
95
------
92
90
92
-------------
90
92
90
-----------
OUTPUT VALUES
Trainee Number : 1
Trainee Number : 3
Note:
Input should be 9 integer values representing oxygen levels entered in order as
Round 1
• Oxygen value of trainee 1
• Oxygen value of trainee 2
• Oxygen value of trainee 3
Round 2
• Oxygen value of trainee 1
• Oxygen value of trainee 2
• Oxygen value of trainee 3
Round 3
• Oxygen value of trainee 1
• Oxygen value of trainee 2
• Oxygen value of trainee 3
Output must be in given format as in above example. For any wrong input final output should display
“INVALID INPUT”"""

oxygen = []

for i in range(9):

    x = int(input())

    if x < 1 or x > 100:
        print("INVALID INPUT")
        exit()

    oxygen.append(x)

avg = []

avg.append(round((oxygen[0] + oxygen[3] + oxygen[6]) / 3))
avg.append(round((oxygen[1] + oxygen[4] + oxygen[7]) / 3))
avg.append(round((oxygen[2] + oxygen[5] + oxygen[8]) / 3))

maximum = max(avg)

if maximum < 70:
    print("All trainees are unfit")
else:

    for i in range(3):

        if avg[i] == maximum:
            print("Trainee Number :", i + 1)




"""45) There is a JAR full of candies for sale at a mall counter. JAR has the capacity N, that is JAR can contain
maximum N candies when JAR is full. At any point of time. JAR can have M number of Candies where
M<=N. Candies are served to the customers. JAR is never remain empty as when last k candies are left.
JAR if refilled with new candies in such a way that JAR get full.
Write a code to implement above scenario. Display JAR at counter with available number of candies.
Input should be the number of candies one customer can order at point of time. Update the JAR after
each purchase and display JAR at Counter.
Output should give number of Candies sold and updated number of Candies in JAR.
If Input is more than candies in JAR, return: “INVALID INPUT”
Given,
N=10, where N is NUMBER OF CANDIES AVAILABLE
K =< 5, where k is number of minimum candies that must be inside JAR ever.
Example 1:(N = 10, k =< 5)
Input Value
3
Output Value
NUMBER OF CANDIES SOLD : 3
NUMBER OF CANDIES AVAILABLE : 7
Example : (N=10, k<=5)
Input Value
0
Output Value
INVALID INPUT NUMBER OF
CANDIES LEFT : 10"""


N = 10
K = 5

order = int(input())

if order <= 0 or order > (N - K):

    print("INVALID INPUT")
    print("NUMBER OF CANDIES LEFT :", N)

else:

    print("NUMBER OF CANDIES SOLD :", order)
    print("NUMBER OF CANDIES AVAILABLE :", N - order)


"""At a fun fair, a street vendor is selling different colours of balloons. He sells N number of different colours
of balloons (B[]). The task is to find the colour (odd) of the balloon which is present odd number of times
in the bunch of balloons.
Note: If there is more than one colour which is odd in number, then the first colour in the array which is
present odd number of times is displayed. The colours of the balloons can all be either upper case or
lower case in the array. If all the inputs are even in number, display the message “All are even”.
Example 1:
• 7 -> Value of N
• [r,g,b,b,g,y,y] -> B[] Elements B[0] to B[N-1], where each input element is sepārated by ṉew line.
Output :
• r -> [r,g,b,b,g,y,y] -> “r” colour balloon is present odd number of times in the bunch.
Explanation:
From the input array above:
• r: 1 balloon
• g: 2 balloons
• b: 2 balloons
• y : 2 balloons
Hence , r is only the balloon which is odd in number.
Example 2:
Input:
• 10 -> Value of N
• [a,b,b,b,c,c,c,a,f,c] -> B[], elements B[0] to B[N-1] where input each element is separated by new
line.
Output :
b-> ‘b’ colour balloon is present odd number of times in the bunch.
Explanation:
From the input array above:
• a: 2 balloons
• b: 3 balloons
• c: 4 balloons
• f: 1 balloons
Here, both ‘b’ and ‘f’ have odd number of balloons. But ‘b’ colour balloon occurs first.
Hence , b is the output.
Input Format for testing
The candidate has to write the code to accept: 2 input
• First input: Accept value for number of N(Positive integer number).
• Second Input : Accept N number of character values (B[]), where each value is separated by a
new line.
Output format for testing
The output should be a single literal (Check the output in example 1 and example 2)
Constraints:
• 3<=N<=50
• B[i]={{a-z} or {A-Z}}"""

def odd_balloon(arr):

    freq = {}

    for color in arr:
        freq[color] = freq.get(color, 0) + 1

    for color in arr:

        if freq[color] % 2 != 0:
            return color

    return "All are even"


n = int(input())

arr = []

for i in range(n):
    arr.append(input())

print(odd_balloon(arr))