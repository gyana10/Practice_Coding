"""946. Validate Stack Sequences
--------------------------------
Given two integer arrays pushed and popped each with distinct values, return truefalse
 Example 1:Input: pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
Output: true
Explanation: We might do the following sequence:
push(1), push(2), push(3), push(4),
pop() -> 4,
push(5),
pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1
Example 2:Input: pushed = [1,2,3,4,5], popped = [4,3,5,1,2]
Output: false
Explanation: 1 cannot be popped before 2.

 Constraints:
1 <= pushed.length <= 1000
0 <= pushed[i] <= 1000
All the elements of pushed are unique.
popped.length == pushed.length
popped is a permutation of pushed.
-----------------------------------------------------------------------"""
class Solution:
    def validateStackSequences(self, pushed, popped):

        stack = []

        j = 0

        for x in pushed:

            stack.append(x)

            while stack and stack[-1] == popped[j]:

                stack.pop()

                j += 1

        return len(stack) == 0
    
"""2. Balanced Parentheses
Given an expression string containing (, ), [, ], {, and }, write a program to determine if the input string is balanced.
 Every opening bracket must have a closing bracket of the same type and in the correct order. [1]
Traverse the string character by character.If it is an opening bracket (, [, {, push it to the stack.
If it is a closing bracket, check if the stack is empty. If not, pop the top element and see if it matches the current 
closing bracket.If the stack is empty at the end, it is balanced.
-----------------------------------------------------------------------------"""
def isBalanced(s):

    stack = []

    pairs = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    for ch in s:

        if ch in "([{":
            stack.append(ch)

        else:

            if not stack:
                return False

            top = stack.pop()

            if top != pairs[ch]:
                return False

    return len(stack) == 0



"""56) Tom has installed corrupted software and it is doing a very strange thing with all his text.
All of the text is changed and is now displayed in opposite case.
Let say, “Hello” is displayed as “hELLO”. Tom is curious to understand the algorithm behind it.
Help Tom to write the code. User will give one word as input and output comes as reverse-case letters as shown above.
Example 1
Input
Tom
Output
tOM
Explanation
In the above input ‘T’ is in upper-case, this will be converted to lowercase, and “om” is in lower case, which will be converted to upper-case. Combining together will make the output as “tOM”.
Example 2
Input
wORLD
Output
World
-------------------------------------------------------------------------"""
s = input()

result = ""

for ch in s:

    if ch.isupper():
        result += ch.lower()
    else:
        result += ch.upper()

print(result)
