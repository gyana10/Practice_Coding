"""34. Gary is an avid hiker. He tracks his hikes meticulously, paying close attention to small details like
topography. During his last hike he took exactly n steps. For every step he took, he noted if it was
an uphill U, or a downhill, D step. Gary’s hikes start and end at sea level and each step up or down
represents a 1 unit change in altitude. We define the following terms:
•A mountainis a sequence of consecutive steps above sea level, starting with a step up from sea
level and ending with a step down to sea level.
•A valleyis a sequence of consecutive steps below sea level, starting with a step down from sea
level and ending with a step up to sea level.
Given Gary’s sequence of up and down steps during his last hike, find and print the number of valleys he
walked through.
For example, if Gary’s path is s=[DDUUUUDD] he first enters a valley 2 units deep. Then he climbs out an
up onto a mountain 2 units high. Finally, he returns to sea level and ends his hike.
Function Description
Complete the countingValleys function in the editor below. It must return an integer that denotes the
number of valleys Gary traversed.
countingValleys has the following parameter(s):
•n: the number of steps Gary takes
•s: a string describing his path
Input Format
The first line contains an integer n , the number of steps in Gary’s hike.
The second line contains a single string s of n characters that describe his path.
Print a single integer that denotes the number of valleys Gary walked through during his hike.
Sample Input
8
UDDDUDUU
Sample Output
1"""
def alti(n,s):
    alt=0
    val=0
    for i in s:
        if i=="U":
            alt+=1
            if alt==0:
                val+=1
        if i=="D":
            alt-=1
    return val            
s="UDDDUDUU"
n=len(s)
print("The altitude is ",alti(n,s))

"""---------------------------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------------------------"""
"""35. You are in charge of the cake for your niece’s birthday and have decided the cake will have one candle for
each year of her total age. When she blows out the candles, she’ll only be able to blow out the tallest
ones. Your task is to find out how many candles she can successfully blow out.
For example, if your niece is turning 4 years old, and the cake will have 4 candles of height 4 ,1 ,1 ,3 she
will be able to blow out 1 candles successfully, since the tallest candles are of height 4 and there
are 2 such candles.
Function Description
Complete the function birthdayCakeCandles in the editor below. It must return an integer representing
the number of candles she can blow out.
birthdayCakeCandles has the following parameter(s):
•ar: an array of integers representing candle heights

Input Format
The first line contains a single integer n denoting the number of candles on the cake.
The second line contains n space-separated integers, where each integer i describes the height of
candle i .
Output Format
Return the number of candles that can be blown out on a new line.
Sample Input 0
4
3 2 1 3
Sample Output 0
2"""
a=[3,2,1,3]
for i in a:
    if i==max(a):
        print("The number of candles that can be blown out is ",a.count(i))


"""---------------------------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------------------------

39.Problem Statement – An automobile company manufactures both a two wheeler (TW) and a four
wheeler (FW). A company manager wants to make the production of both types of vehicle according to
the given data below:
•1st data, Total number of vehicle (two-wheeler + four-wheeler)=v
•2nd data, Total number of wheels = W
The task is to find how many two-wheelers as well as four-wheelers need to manufacture as per the given
data.
Example :
Input :
200 -> Value of V
540 -> Value of W
Output :
TW =130 FW=70
Explanation:
130+70 = 200 vehicles
(70*4)+(130*2)= 540 wheels
Constraints :
•2<=W
•W%2=0
•V<W
Print “INVALID INPUT” , if inputs did not meet the constraints.
The input format for testing
The candidate has to write the code to accept two positive numbers separated by a new line.
•First Input line – Accept value of V.
•Second Input line- Accept value for W.
The output format for testing
•Written program code should generate two outputs, each separated by a single space
character(see the example)
•Additional messages in the output will result in the failure of test case"""

a,b=map(int,input().split())
if b%2==0 and a<b and b>=2:
    fw=(b-2*a)//2
    tw=a-fw
    print("TW =",tw,"FW =",fw)



"""-------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------- 

40.Given a string S(input consisting) of ‘*’ and ‘#’. The length of the string is variable.
The task is to find the minimum number of ‘*’ or ‘#’ to make it a valid string. The string is considered valid
if the number of ‘*’ and ‘#’ are equal. The ‘*’ and ‘#’ can be at any position in the string.
Note : The output will be a positive or negative integer based on number of ‘*’ and ‘#’ in the input string.
•(*>#): positive integer
•(#>*): negative integer
•(#=*): 0
Example 1:
Input 1:
•###*** -> Value of S
Output :
•0 → number of * and # are equal
---------------------------------------------------------------------------------
-------------------------------------------------------------------------------"""
s=input()
if s.count("*")>s.count("#"):
    print(s.count("*")-s.count("#"))
elif s.count("*")<s.count("#"):
    print(s.count("*")-s.count("#"))
elif s.count("*")==s.count("#"):
    print(0)        

"""
A parking lot in a mall has RxC number of parking spaces. Each parking space will either be empty(0) or
full(1). The status (0/1) of a parking space is represented as the element of the matrix. The task is to find
index of the prpeinzta row(R) in the parking lot that has the most of the parking spaces full(1).
Note :
RxC- Size of the matrix
Elements of the matrix M should be only 0 or 1.
Example 1:

Input :
3 -> Value of R(row)
3 -> value of C(column)
[0 1 0 1 1 0 1 1 1] -> Elements of the array M[R][C] where each element is separated by new line.
Output :
3 -> Row 3 has maximum number of 1’s
Example 2:
input :
4 -> Value of R(row)
3 -> Value of C(column)
[0 1 0 1 1 0 1 0 1 1 1 1] -> Elements of the array M[R][C]
Output :
4 -> Row 4 has maximum number of 1’s"""

a,b=map(int,input().split())
m=[]
for i in range(a):
    row=list(map(int,input().split()))
    m.append(row)
max_row=0
max_count=0 
for i in range(a):
    count=m[i].count(1)
    if count>max_count:
        max_count=count
        max_row=i+1
print(max_row)

"""Given a number find the armstarong of it"""
def armstrong(n):
    temp=n
    sum=0
    while temp>0:
         digit=temp%10
         sum=sum+digit**len(str(n))
         temp=temp//10
    if sum==n:
        print("Armstrong")
    else:
        print("Not armstrong")   
n=int(input())
armstrong(n)  


            
