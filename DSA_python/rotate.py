#Give a string as an input.we need to write a program that will print all non empty substrings of that given string
#Non empty string
s="ABC"
for i in range(len(s)):
    for j in range(i+1,len(s)+1):
        print(s[i:j],end=" ")
