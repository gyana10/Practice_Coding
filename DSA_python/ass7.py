"""43. Day 2 Slot 1 – Question 1
A party has been organised on cruise. The party is organised for a limited time(T). The number of guests
entering (E[i]) and leaving (L[i]) the party at every hour is represented as elements of the array. The task
is to find the maximum number of guests present on the cruise at any given instance within T hours.
Example 1:
Input :
•5 -> Value of T
•[7,0,5,1,3] -> E[], Element of E[0] to E[N-1], where input each element is separated by new line
•[1,2,1,3,4] -> L[], Element of L[0] to L[N-1], while input each element is separate by new line.
Output :
8 -> Maximum number of guests on cruise at an instance.
Explanation:
1st hour:
Entry : 7 Exit: 1
No. of guests on ship : 6
2nd hour :
Entry : 0 Exit : 2
No. of guests on ship : 6-2=4
Hour 3:
Entry: 5 Exit: 1
No. of guests on ship : 4+5-1=8
Hour 4:
Entry : 1 Exit : 3
No. of guests on ship : 8+1-3=6
Hour 5:
Entry : 3 Exit: 4
No. of guests on ship: 6+3-4=5
Hence, the maximum number of guests within 5 hours is 8.
Example 2:
Input:
4 -> Value of T
[3,5,2,0] -> E[], Element of E[0] to E[N-1], where input each element is separated by new line.
[0,2,4,4] -> L[], Element of L[0] to L[N-1], while input each element in separated by new line
Output:
6
Cruise at an instance
Explanation:
Hour 1:Entry: 3 Exit: 0
No. of guests on ship: 3
Hour 2:
Entry : 5 Exit : 2
No. of guest on ship: 3+5-2=6
Hour 3:
Entry : 2 Exit: 4
No. of guests on ship: 6+2-4= 4
Hour 4:
Entry: 0 Exit : 4
No. of guests on ship : 4+0-4=0
Hence, the maximum number of guests within 5 hours is 6.
The input format for testing
The candidate has to write the code to accept 3 input.
First input- Accept value for number of T(Positive integer number)
Second input- Accept T number of values, where each value is separated by a new line.
Third input- Accept T number of values, where each value is separated by a new line.
The output format for testing
The output should be a positive integer number or a message as given in the problem statement(Check
the output in Example 1 and Example 2)
Constraints:
•1<=T<=25
•0<= E[i] <=500
•0<= L[i] <=500
--------------------------------------------------------------------------------"""
t = int(input())

entry = []
exit = []

for i in range(t):
    entry.append(int(input()))

for i in range(t):
    exit.append(int(input()))

guests = 0
maximum = 0

for i in range(t):
    guests += entry[i] - exit[i]
    maximum = max(maximum, guests)

print(maximum)


"""51. Problem Statement
There are total n number of Monkeys sitting on the branches of a huge Tree. As travelers offer Bananas
and Peanuts, the Monkeys jump down the Tree. If every Monkey can eat k Bananas and j Peanuts. If total
m number of Bananas and p number of Peanuts are offered by travelers, calculate how many Monkeys
remain on the Tree after some of them jumped down to eat.
At a time one Monkeys gets down and finishes eating and go to the other side of the road. The Monkey
who climbed down does not climb up again after eating until the other Monkeys finish eating.
Monkey can either eat k Bananas or j Peanuts. If for last Monkey there are less than k Bananas left on the
ground or less than j Peanuts left on the ground, only that Monkey can eat Bananas(<k) along with the
Peanuts(<j).
Write code to take inputs as n, m, p, k, j and return the number of Monkeys left on the Tree.
Where, n= Total no of Monkeys
k= Number of eatable Bananas by Single Monkey (Monkey that jumped down last may get less than k
Bananas)
j = Number of eatable Peanuts by single Monkey(Monkey that jumped down last may get less than j
Peanuts)
m = Total number of Bananas
p = Total number of Peanuts
Remember that the Monkeys always eat Bananas and Peanuts, so there is no possibility of k and j having
a value zero
Example 1:
Input Values
20
2
3
12
12
Output Values
Number of Monkeys left on the tree:10
Note: Kindly follow the order of inputs as n,k,j,m,p as given in the above example. And output must
include the same format as in above example(Number of Monkeys left on the Tree:)
For any wrong input display INVALID INPUT
-------------------------------------------------------------------"""
n = int(input())
k = int(input())
j = int(input())
m = int(input())
p = int(input())

if n <= 0 or k <= 0 or j <= 0 or m < 0 or p < 0:
    print("INVALID INPUT")
else:
    down = 0

    down += m // k
    if m % k != 0:
        down += 1

    down += p // j
    if p % j != 0:
        down += 1

    print("Number of Monkeys left on the tree:", n - down)


"""63. A Sober Walk
Our hoary culture had several great persons since time immemorial and king Vikramaditya’s nava ratnas
(nine gems) belongs to this ilk. They are named in the following shloka:
Among these, Varahamihira was an astrologer of eminence and his book Brihat Jataak is recokened as the
ultimate authority in astrology. He was once talking with Amarasimha, another gem among the nava
ratnas and the author of the Sanskrit thesaurus, Amarakosha. Amarasimha wanted to know the final
position of a person, who starts from the origin 0 0 and travels per the following scheme.
•He first turns and travels 10 units of distance
•His second turn is upward for 20 units
•The third turn is to the left for 30 units
•The fourth turn is downward for 40 units
•The fifth turn is to the right(again) for 50 units
… And thus he travels, every time increasing the travel distance by 10 units.
Constraints:
2<=n<=1000
Input:
3
OUTPUT
-20 20---------------------------------------------------------------------------------------"""
n = int(input())

x = 0
y = 0

dist = 10

for i in range(1, n + 1):

    if i % 4 == 1:
        x += dist

    elif i % 4 == 2:
        y += dist

    elif i % 4 == 3:
        x -= dist

    else:
        y -= dist

    dist += 10

print(x, y)


"""64. #3: Word is the key
One programming language has the following keywords that cannot be used as identifiers:
break, case, continue, default, defer, else, for, func, goto, if, map, range, return, struct, type, var
Write a program to find if the given word is a keyword or not
Input #1:
defer
Output:
defer is a keyword
Input #2:
While
OUTPUT
while is not a keyword
MPCS
keyword = {"break", "case", "continue", "default", "defer", "else", "for","func", "goto", "if", "map", "range", "return", "struct", "type", "var"}"""
keyword = {
"break", "case", "continue", "default",
"defer", "else", "for", "func",
"goto", "if", "map", "range",
"return", "struct", "type", "var"
}

word = input()

if word.lower() in keyword:
    print(word, "is a keyword")
else:
    print(word, "is not a keyword")