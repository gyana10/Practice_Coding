"""47. Problem Statement
A washing machine works on the principle of Fuzzy System, the weight of clothes put inside it for washing
is uncertain But based on weight measured by sensors, it decides time and water level which can be
changed by menus given on the machine control area.
For low level water, the time estimate is 25 minutes, where approximately weight is between 2000 grams
or any nonzero positive number below that.
For medium level water, the time estimate is 35 minutes, where approximately weight is between 2001
grams and 4000 grams.
For high level water, the time estimate is 45 minutes, where approximately weight is above 4000 grams.
Assume the capacity of machine is maximum 7000 grams
Where approximately weight is zero, time estimate is 0 minutes.
Write a function which takes a numeric weight in the range [0,7000] as input and produces estimated
time as output is: “OVERLOADED”, and for all other inputs, the output statement is
“INVALID INPUT”.
Input should be in the form of integer value –
Output must have the following format –
Time Estimated: Minutes
Example:
Input value
2000
Output value
Time Estimated: 25 minutes"""
n=int(input())
if n>0 and n<=2000:
    print("Time Estimated :25 minutes")
elif n>=2001 and n<=4000:
    print("Time Estimated :35 minutes")
elif n>4000 and n<=7000:
    print("Time Estimated :40 minutes")
elif n==0:
    print("TIme estimated :0 minutes")
elif n<0:
    print("INVALID INPUT")    
else:

    print("OVERLOADED")                

"""48. Problem Statement
The Caesar cipher is a type of substitution cipher in which each alphabet in the plaintext or messages is
shifted by a number of places down the alphabet.
For example,with a shift of 1, P would be replaced by Q, Q would become R, and so on.
To pass an encrypted message from one person to another, it is first necessary that both parties have the
‘Key’ for the cipher, so that the sender may encrypt and the receiver may decrypt it.
Key is the number of OFFSET to shift the cipher alphabet. Key can have basic shifts from 1 to 25 positions
as there are 26 total alphabets.As we are designing custom Caesar Cipher, in addition to alphabets, we are considering numeric digits
from 0 to 9. Digits can also be shifted by key places.
For Example, if a given plain text contains any digit with values 5 and keyy =2, then 5 will be replaced by
7, “-”(minus sign) will remain as it is. Key value less than 0 should result into “INVALID INPUT”
Example 1:
Enter your PlainText: All the best
Enter the Key: 1
The encrypted Text is: Bmm uif Cftu
Write a function CustomCaesarCipher(int key, String message) which will accept plaintext and key as
input parameters and returns its cipher text as output    """

def customCipher(key,message):
    if key<0:
        return "INVALID INPUT"
    cipher=""
    for i in message:
        if i.isalpha():
            if i.isupper():
                cipher+=chr((ord(i)+key-65)%26+65)
            else:
                cipher+=chr((ord(i)+key-97)%26+97)
        elif i.isdigit():
            cipher+=chr((ord(i)+key-48)%10+48)
        else:
            cipher+=i
    return  cipher
key=int(input())
message=input()
print(customCipher(key,message))

"""76. Given a binary string S of length N consisting of '0' and '1 A binary string is good if the total number of
consecutive ones in a string (wherever present) are equal
For eg. "011101110" There are 3 consecutive ones present at two positions.
"011101101". Here, consecutive ones are present at three positions having length 3, 2, and 1
respectively.
You are allowed to perform two types of operations
>You can choose any index i and insert '1' at that position. After this, the length of the string will increase
by 1.
> Choose any index i such that S[i] = '1' and remove S[I]. After this, the length of the string will decrease
by 1
Your task is to make a given string good using the minimum number of operations
----------------------------------------------------"""

s = input()

groups = []
count = 0

for ch in s:
    if ch == '1':
        count += 1
    else:
        if count > 0:
            groups.append(count)
        count = 0

if count > 0:
    groups.append(count)

if len(set(groups)) <= 1:
    print("Good")
else:
    print("Not Good")

"""JAN 31 2023
79. Mr. Rao is relocating from place A to B. The moving truck has a maximum capacity C. There are 'N' items
in the house where each item has a corresponding value (V)and weight(W). Mr.Rao has to carry only the
most Valuable items whose total weight does not exceed capacity of the truck. The task here is to find
those items (single or combination of items) whose total value(v) will be the maximum and their
corresponding weight(w) will not exceed truck capacity (C). Here
N=No. of items
C-Maximum capacity of the truck, an integer value.
W[O to N-1]- An array consisting weight of each item
V[0 to N-1] - An array consisting value of each item
--------------------------------------"""
n = int(input())
c = int(input())

w = list(map(int, input().split()))
v = list(map(int, input().split()))

max_value = 0

for i in range(1 << n):

    total_weight = 0
    total_value = 0

    for j in range(n):

        if i & (1 << j):
            total_weight += w[j]
            total_value += v[j]

    if total_weight <= c:
        max_value = max(max_value, total_value)

print(max_value)