"""Generate All Substrings
Problem Statement
Given a string, print all possible non-empty substrings.
Example
Input:
muskan
Output:
m
mu
mus
musk
muska
muskan
u
us
usk
uska
uskan
s
sk
ska
skan
...
n"""
def generate_substrings(s):
    n = len(s)
    for i in range(n):
        for j in range(i + 1, n + 1):
            print(s[i:j])
s = input().strip()
generate_substrings(s)

"""Star-Hash Balance
Problem Statement
Given a string containing only:
*
#
Find the difference between the number of * and #.
Output:
(Number of *) - (Number of #)
Example 1
Input:
###***
Count:
* = 3
# = 3
Output:
0"""
def star_hash_balance(s):
    return s.count('*') - s.count('#')
s = input().strip()
print(star_hash_balance(s))
"""Keyword Checker
Given a word, determine whether it is a programming language keyword.
Keywords are predefined reserved words that have special meaning in a programming language.
Given keyword list:
break
case
continue
default
defer
else
for
func
goto
if
map
range
return
struct
type
var
Example 1
Input:
defer
Output:
defer is a keyword"""