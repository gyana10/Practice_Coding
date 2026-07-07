"""88. Sara has a box which has N chocolates in it. Sara decides to gift the box to Alice and Bob. Bob can have x
chocolates from the box and Alice gets the remaining chocolates, y. SincE chocolates, Sara tries to calm
them down by playing a game.
If Bob gets x chocolates and Alice gets y chocolates, and if x>y, Bob should put y chocolates back into the
box. The same rule applies to Alice as well. This continues until one of t equal number of chocolates.
Write a program to find out the number of chocolates in the box after the game is over.
Illustrate the scenario by reading the input from STDIN and writing the output to STDOUT.
You should not write arbitrary strings while reading the input and while printing as the
Constraints:
1)N 2
11) 0 < x <= N
Input Format:
A single line of input contains two integers, N and x, separated by a single whitespace.
Output Format:
Output contains the number of chocolates left in the box at the end of game.
Sample Input 1:
104
Sample Output 1:
6
Explanation 1:
Bob gets 4 chocolates and Alice gets 6 chocolates. So Alice has to put back 4 chocolates into the box. So
Bob will have 4 and Alice will have 2 chocolates. Now Bob has to put chocolates each. So, there will be
10-4-6 chocolates in the box. Therefore output is 6
Sample Input2:
174

--------------------------------------------------------------------------------"""
n,x=map(int,input().split())
a=x
b=n-x
while a!=b:
    if a>b:
        a=a-b
    else:
        b=b-a
print(n-2*a) 

"""18. GCD of Three Numbers
Definition of HCF (Highest common factor):
HFC is also called the greatest common divisor (gcd). HCF of two numbers is the largest positive
number which can divide both numbers without any remainder. For example, the HCF of two
numbers 4 and 8 is 2 since 2 is the largest positive number which can divide 4 as well as 8 without a
remainder.
The logic for writing program:
It is clear that any number is not divisible by greater than the number itself.
☆In the case of more than one number, a possible maximum number that can divide all of the
numbers must be a minimum of all of that numbers.
For example 10, 20, and 30
Min (10, 20, 30) =10 can divide all there numbers. So we will take one for loop which will start from
the min of the numbers and will stop the loop when it became one since all numbers are divisible by
one. Inside for loop, we will write one if conditions which will check divisibility of both the numbers.
----------------------------------------------------------------------------"""




"""23. A discrete Mathematics professor has a class of students. Frustrated with their lack of discipline,
decides to cancel class if fewer than some number of students are present when class starts.
Arrivel times go from on time ( arrival time<=0) to arrived late (arrivalTime> 0).
Given the arrival time of each student and a threshold number of attendees, determine if the class
is canceled.
----------------------------------------------------------------------------"""
n=int(input())
p=int(input())
arrivalTime=int(input())
if (p>=n//2) and (arrivalTime<=0):
    print("class happens")
else:
    print("No Class")    


"""38. You will be given an array of integers. All of the integers except one occur twice. That one is unique in the
array.
Given an array of integers, find and print the unique element.
For example a=[1,2,3,4,3,2,1] the unique element is 4.
Function Description
Complete the lonelyinteger function in the editor below. It should return the integer which occurs only
once in the input array.
lonelyinteger has the following parameter(s):
• a: an array of integers
Input Format
The first line contains a single integer n denoting the number of integers in the array.
The second line contains n space-separated integers describing the values in a.
Output Format
Print the unique integer in the array.
Sample Input 0
1
1
Sample Output 0
1
--------------------------------------"""

n=list(map(int,input().split()))
for i in set(n):
    if n.count(i)==1:
        print(i)
        break    



"""95. Arya has a crush on Sam, she wants to write him a secret letter to express her feelings, but now she is
worned it will be traced back to her thought the___ Ransom Note (formed from words or letters cut
randomly from a magazine or newspaper). She found a magazine and wants to know she __ to create an
untraceable replica of her ransom note.
The words in his note are case-sensitive and he must use only whole words available in the magazine. He
cannot use substrings concatenation to create the Given the words in the magazine and the words in the
ransom note, print Yes if he can replicate his ransom note exactly wing whole from the magazines
Note: All the special characters (ie full stop or comma) are space separated.
Read the input from STDIN and write the output to STDOUT You should not write arbitrary strings while
reading the input
Constraints:
1 >= n >= 100
10>= (str) >= 1000
Input Format:
First line of input consists of an integer n representing the number of messages that Arya decided to
write Second line of input consists of a random string from the magazine (Consist spaces). From third line
of input consists of an n-number of strings in n-number of lines that stores the message that arya wants
to type
Output Format:
N lines of output contain a string yes or no, depending on the possibility of writing a message.
Sample Input 1:
1 I can't say how much I like you and how special you are to me, but I can say my world is full of smiles
when I am with you. I like you and you are special to me.
Sample Output 1:
Yes                                            
                                 """
n=int(input())
mag=input().split()
for i in range(n):
    note=input().split()
    temp=mag.copy()
    flag=True
    for word in note:
        if word in temp:
            temp.remove(word)
        else:    
            flag=False
            break
    print("Yes" if flag else "No")