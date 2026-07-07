"""81. One of the most common and essential applications in all the mobiles is the CLOCK. The app is designed
to capture time automatically according to their time zones. The display format can be 12hr or 24hr
based on convenience. The task here is to convert the time given as a string in 24 hour(00:00 to 23:59)
format to a 12 hour format(00:00 to12:00). The format for both input and output are H:MM:SS where
HH,MM,SS denotes hours, minutes and seconds respectively The output in 12 hour format shpuld denote
if the time is AM or PM.
Example 1:
Input:
15:15:22 -> Value of str
Output:
3:15:22 PM->Time in 12 hour format
Explanation:
From the input given above
Str = 15:15:22
The given time is in 24-hour format
After 12PM,
13 hours is 1:00 PM
---------------------------------------------------------------------------------------------------"""
time = input()

h, m, s = map(int, time.split(':'))

if h == 0:
    print(f"12:{m:02d}:{s:02d} AM")
elif h < 12:
    print(f"{h}:{m:02d}:{s:02d} AM")
elif h == 12:
    print(f"12:{m:02d}:{s:02d} PM")
else:
    print(f"{h-12}:{m:02d}:{s:02d} PM")

"""85. A box consists of N pieces of stones with each stone having certain weights assigned to it. The task is to
manage all stones into that both parts should have equal weight of stones. two-part such
Print "TRUE" if the partition is possible otherwise print "FALSE".

Example 1:
Input
4 à Value of N, represents size of Arr
2 à Value of Arr[0], represents
Weight of 1st stone
9 à Value of Arr[1], represents
Weight of 2nd stone
3 à Value of Arr[2], represents
Weight of 3rd
 stone
4 à Value of Arr[3], represents
-----------------------------------------------------------------------------------------------------------------"""
n = int(input())
arr = [int(input()) for _ in range(n)]

total = sum(arr)

if total % 2 != 0:
    print("FALSE")
else:
    target = total // 2

    dp = {0}

    for num in arr:
        dp.update({x + num for x in dp})

    print("TRUE" if target in dp else "FALSE")

"""84. A primary school teacher is trying creative methods to teach her students to recognise numbers. One of
the methods involves providing 'N' numbers to the students. She gives another special digit(S) whose
occurrences should be found in all the numbers up to N. The task here is to find the count of values
containing the special digit and also display all the numbers from 0 to N comprising the special digit.
Example1:
Input:
20 >> Value of N
3 -> Value of S
Output:
3 1 3---NUMBERS
 2 -- COUNT
the digit 3 and the count of numbers containing the digir 3
-----------------------------------------------------------------------------------------------------------------"""
n = int(input())
s = input()

result = []

for i in range(n + 1):
    if s in str(i):
        result.append(i)

print(*result)
print(len(result))


"""86. Few keys the keyboards are not working properly. While typing, there are few alphabets that gets
induced with multiple occurences. This is has caoused huge problem to the user.
Now they have to come up with up with a feature that remove all these duplicates alphabets within a
word. Only those alphabets have to be removed which have occurred more than once exactly adjacent to
each other.
Example
Input:
"abciijklma" >input string containing multiple occurences of adjacent duplciate .
output
"abcjklma" >output string without any adjacent duplicate alphabets.
Explanation:
Consider the above string, it contains 2 I's next to each other. These are the ones that need to be
removed. There are also 2 a's, but they are not adjacent to each other. Hence these should not be
removed from the original string.
------------------------------------------------------------------------------------------------"""
s = input()

result = []
i = 0

while i < len(s):
    if i < len(s)-1 and s[i] == s[i+1]:
        while i < len(s)-1 and s[i] == s[i+1]:
            i += 1
    else:
        result.append(s[i])

    i += 1

print("".join(result))

"""87. Maria is teaching her 2 years old Tina-English alphabets. Tina likes donuts a lot, and whenever she sees
anything which is even a little bit circular, she says donuts.maria didn't understand in the beginning, but
later she got it, that any alphabets which is enclosed shape, is Wed by Tina
Let say A, this has an enclosure of triangle. Then B, it has 2 enclosures. C has no enclosures. D has 1...and
so on
So, now Maria a taught Tina a new way, that if she finds any alphabets with enclosures sum up all the
enclosures For eg. the word TINA has only enclosure. The word MARIA has 3 enclosures
Given a word in all upper case, find the total number of enclosures in the entire word.
Example 1:
Input:
775031160 273
60 273
HOLLYWOOD -> Input string, S
Output:
4 Output"""

s = input().strip()

count = 0

for ch in s:
    if ch == 'B':
        count += 2
    elif ch in 'ADOPQR':
        count += 1

print(count)