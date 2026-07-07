"""60) There was a programming quiz. Alena and Vincent were participated in the same.
Alena got a very simple problem. But Vincent got a bit tricky question, hence struggling in solving the same.
The problem statement was “To find second most frequent character appeared in the string”.
Help Vincent by writing a program.
Note: In the case of more than one character are found as second most frequent character then print the character
that appear first in string character order
Example 1
Input
bbccccnnddee
Output
E
Explanation
Given a string bbccccnnddeee which has repeating characters. Character “c” frequency is 4 and character “e” frequency is 3. 
As per problem statement, second most frequent character occurrence is “e”. Hence output is “e”.
Example 2
Input
aaaccc
Output
Invalid String
------------------------------------------------------------------------------"""
s=input()
freq={}
for i in s:
    freq[i]=freq.get(i,0)+1
f=sorted(set(freq.values()),reverse=True)    
if len(f)<2:
    print("Invalid String")
else:
    second=f[1]
    for i in s:
        if freq[i]==second:
            print(i)
            break    


"""59) There was a Grocery shop. Shopkeeper would like to keep transactions as simple as he can.
Hence, he used to take money as whole number. To optimize transactions, he decided if someone buys groceries from 
his shop, he will round money to the nearest whole number having zero as last digit.
Write a program to help Shopkeeper to make transactions much simple.
Example 1
Input
7659
Output
7660
Explanation
Given integer “7659” which is near to 7660, the whole number having zero as last digit. Hence output is 7660
Example 2
Input
50
Output
50
(edited)
A grocery shopkeeper wants to simplify cash transactions. 
Therefore, every bill amount should be rounded to the (i.e., the nearest multiple of 10).
Given an integer amount , write a program to find and print the nearest multiple of 10.
If the amount is already a multiple of 10, print it as it is.
Input Format
A single integer representing the bill amount.
Output Format
Print the nearest multiple of .
Constraints
0 ≤ N ≤ 10^9
Example 1
7659
7660
The nearest multiple of 10 to 7659 is 7660.
Example 2
50
50
50 already ends with 0, so no rounding is required.
Example 3
7654
7650
The nearest multiple of 10 to 7654 is 7650.
Example 4
7655
7660
When the last digit is 5 or greater, round up to the next multiple of 10.
------------------------------------------------------------------------------"""
n=int(input())
last=n%10
if last>=5:
    n=n+(10-last)
else:
    n=n-last
print(n)        
"""58) Roman Numerals have been used across the school curriculum. Mona would like to convert Decimal numbers
 to Roman numerals. Write a program to help Mona in converting decimal numbers in to Roman numerals
Example 1
Input
9
Output
IX
Explanation
Roman representation of integer “9” would be “IX”. Hence output will print “IX”.
Example 2
Input
904
Output
CMIV
Explanation
Roman representation of integer “904” will be “CMIV”. Hence output will print “CMIV”.
------------------------------------------------------------------------------"""
n = int(input())
values = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
symbols = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
ans = ""
for i in range(len(values)):
    while n >= values[i]:
        ans += symbols[i]
        n -= values[i]

print(ans)

"""57) Michael wants to check the parity of the given number. To find the parity, follow below steps:
1. Convert decimal number binary number
2. Count the number of 1’s or 0’s in the binary representation.
If it contains odd number of 1-bits, then it is “odd parity” and is “even parity” if it contains even number of 1-bits.
Write a program to validate the given number belongs to odd parity or even parity.
Example 1
Input
13
Output
Odd Parity
Explanation
Binary representation of integer 13 is “1101”. The count of 1’s in “1101” is 3 which is odd. Hence output is in string
“Odd Parity”.
Example 2
Input
15
Output
Even Parity
Binary representation of integer 15 is “1111” The count of 1’s in “1111” is 4 which is even. Hence output is in
string “Even Parity”.

------------------------------------------------------------------------------"""
n = int(input())
count = 0
while n > 0:
    if n % 2 == 1:
        count += 1

    n //= 2
if count % 2 == 0:
    print("Even Parity")
else:
    print("Odd Parity")


"""11) A shopkeeper in a nearby town always starts his business Rs. 0. He never uses the previous days money for
his transaction. Any item in his shop costs Rs. 30. There are ‘N’ numbers of customers waiting in the queue to buy
items. A customer can buy any number of items but worth only Rs. 30. 
The customers can transact with the shopkeeper only with the denominations Rs. 30, Rs. 60, Rs. 120.
The task here to find if the transaction between the customer and shopkeeper is possible. 
The customer should be able to buy the item. The amount each customer uses for his transaction is given as 
array elements.
The shopkeeper should be able to return the exact change.
Display ‘Transaction successful’ on a successful transaction with all the customers in the queue.
 Display ‘Transaction failed’ on an unsuccessful transaction with any one customer in the queue.
Example 1
Input
3
30 30 60
Output
Transaction successful
Explanation
From the input given above:
Initially, the shopkeeper has Rs. 0.
Number of customers: 3
Customer 1 wants to buy item worth: 30
Customer 2 wants to buy item worth: 30
Customer 3 wants to buy item worth: 60
When customer 1 arrives, he pays the shopkeeper Rs. 30
Now the shopkeeper has Rs. 30 with him.
When customer 2 arrives, he pays the shopkeeper Rs. 30
Now the shopkeeper has Rs. 60 with him.
When customer 3 arrives, he pays the shopkeeper Rs. 60
The shopkeeper returns Rs. 30 from the 1st customer. Now the shopkeeper has Rs. 30 with him.
Finally, all the customers in queue were able to buy the items.
Hence, the output is Transaction successful.
Example 2
Input
3
30 30 120
Output
Transaction failed
Explanation
From the input given above:
Initially the shopkeeper has Rs. 0
Number of customers: 3
Customer 1 wants to buy item worth: 30
Customer 2 wants to buy item worth: 30
Customer 3 wants to buy item worth: 120
When customer 1 arrives, he pays the shopkeeper Rs. 30.
Now the shopkeeper has Rs. 30 with him.
When customer 2 arrives, he pays the shopkeeper Rs. 30
Now the shopkeeper has Rs. 60 with him
When customer 3 arrives, he pays the shopkeeper Rs. 120
The customer needs to receive a change of Rs. 90
The shopkeeper returns Rs. 30 from the 1st customer
The shopkeeper returns Rs. 30 from the 2nd customer.
So, the shopkeeper can return a maximum change of Rs. 60 to the 3rd customer which fails the transaction and
 customer cannot buy the items."""
n = int(input())

arr = list(map(int, input().split()))

c30 = 0
c60 = 0

flag = True

for money in arr:

    if money == 30:
        c30 += 1

    elif money == 60:

        if c30 >= 1:
            c30 -= 1
            c60 += 1
        else:
            flag = False
            break

    elif money == 120:

        if c60 >= 1 and c30 >= 1:
            c60 -= 1
            c30 -= 1

        elif c30 >= 3:
            c30 -= 3

        else:
            flag = False
            break

print("Transaction successful" if flag else "Transaction failed")