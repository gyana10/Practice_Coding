"""Rakesh once had trouble finding the numbers in a string. The numbers are distributed across a string.You
need to parse only those numbers which do not contain 9. For eg, if the string contains “hello this is alpha
5051 and 9475 TCS Coding Questions”. You will extract 5051 and not 9475. Print the largest number.
Input: This is alpha 5057 and 97 Output: 5057
Algorithm:
1. The idea is to traverse string and check if it is a digit.
2. If digit has been encountered loop until character is found and form the number from these digits.
3. If the number doesn't contains 9 then find the maximum from current max and the number formed.
------------------------------------------------------------------------------------------------"""
s=input()
max_num=0
num=""
for i in s:
    if i.digit():
        num+=i
    else:
        if num and '9'not in num:
            max_num=max(max_num,int(num))
        num=""
if num and '9'not in num:
    max_num=max(max_num,int(num))
print(max_num)


"""58. Find the number of students whose height is less than the height of their adjacent students.
Problem Statement
A physical education teacher asks students to assemble in a straight line for the morning assembly.Given
an array of N in which each element represents the height of the student in that position. The task here is
to find the number of students whose height is less than the height of their adjacent students.
Input: 35, 15, 45,25,55 Output: 2 (35>15<45 and 45>25<55)
Algorithm
The idea is to traverse array and compare with its left and right adjacent elements.If it is less than both
the elements increment the count
-----------------------------------------------------------------------------------------------------"""
arr=list(map(int,input().split()))
count=0
for i  in range(1,len(arr)-1):
    if arr[i]<arr[i-1] and arr[i]<arr[i+1]:
        count+=1
print(count)   


"""57. Possible combinations of the coins that can be inserted to get rupees from the kiosk.
A ‘coin vend’ kiosk is installed all the major metro stations The machine allows one to obtain cash of ‘R’
rupees in exchange for coins. The machine operates with the following conditions:
1. Only coins of denomination 1 rupee and 2 rupee can be exchanged.
2. Coins of denomination 2 rupees should not be inserted successively twice.
The task here to find all the possible combinations of the coins that can be inserted to get rupees from
the kiosk.
Input: 3 (1 + 1 + 1), (2 + 1), (1 + 2), Output: 6
Algorithm:
The idea is to use recursion. If 1 is inserted then we can insert 1 and 2 both. But if we have inserted 2
then again 2 cannot be inserted so only 1 can be inserted. Thus, are recursion
becomes coinCombinations(n - 1) + coinCombinations(n - 3); [ As 2 comes in combination with 1 so 3 will
be subtracted instead of 1 ]
-----------------------------------------------------------------------------------------------------------"""


"""60. Order Management
Problem Statement:
A store has different categories of products in stock as shown below.
Item Number=[101, 102, 103, 108] Price=[42, 50, 500, 40] Stock =[10, 20, 15, 16]
User Inputs two values:
•Item number for item which user wish to buy
•Quantity for the item entered above
1. If quantity is less than stock and item is available display a notification message
showing Output: Total price in float with precision and updated stock for item after after
purchase
2. If the quantity and stocks less than quantity entered by the user while placing order,
then Output: NO STOCK and quantity left
3. If user enter character as input for item number and quantity or enter item number which is
not available Output: INVALID INPUT
Algorithm
The idea is to make hashmap with key as item number and value as price and stock. Check if item number
is present or not. If present return required result or else return Invalid input"""
stock={101:[42,10],102:[50,20],103:[500,15],108:[40,16]}
item=int(input())
quantity=int(input())
if item in stock:
    if quantity<=stock[item][1]:
        print("Total price: {:.2f}".format(stock[item][0]*quantity))
        stock[item][1]-=quantity
        print("Updated stock: ",stock[item][1])
    else:
        print("NO STOCK")
        print("Quantity left: ",stock[item][1])
else:
    print("INVALID INPUT")
    