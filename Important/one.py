"""Q56   (Original #50)   City Bus Fare Calculator
Ring-route bus with 8 stops: [TH,GA,IC,HA,TE,LU,NI,CA]. Path distances:
[800,600,750,900,1400,1200,1100,1500].
Fare: £1000m=5 INR/1000m, ceil fractions. Handle circular route.
Example: Source=NI, Dest=HA fi 23.0 INR"""

def route(source,destination):
    stops = ["TH","GA","IC","HA","TE","LU","NI","CA"]
    dist = [800,600,750,900,1400,1200,1100,1500]
    if source not in stops or destination not in stops:
        print("Invalid Input")
    si=stops.index(source)
    di=stops.index(destination)
    total=0
    i=si
    while i!=di:
        total+=dist[i]
        i=(i+1)%8
        
    return (total*5+999)//1000

source=input().strip()
destination=input().strip()
print(route(source,destination))
    
"""Q59   (Original #54)   Doctor's Daily Earnings
Fees by age: <17 fi 200 INR, 17–40 fi 400 INR, >40 fi 300 INR. Max 20 patients/day. Input ages until empty
line. Print total.
Example: ages=[20,30,40,50,2,3,14] fi Total Income 2000 INR"""
def count_v(a, b):

    if len(a) == len(b):
        print("true")
    else:
        print(ord(b[-1]))

    ans = 0

    for ch in a:
        if ch.lower() in "aeiou":
            ans += 1

    for ch in b:
        if ch.lower() in "aeiou":
            ans += 1

    print(ans)

a = input()
b = input()

count_v(a, b)

""" First Odd-Count Balloon Color
Given N balloon colors, find the first color that appears an odd number of times. Print 'All are even' if none.
Example: [r,g,b,b,g,y,y] fi r (appears 1 time)
Example: [a,b,b,b,c,c,c,a,f,c] fi b (3 times, first odd-count)"""
n = int(input())
arr = list(map(int, input().split()))
freq = {}
for i in arr:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1

for i in arr:
    if freq[i] % 2 == 1:
        print(i)
        break
else:
    print("All are even")

"""Sober Walk – Final Position
A person starts at origin (0,0) and walks: right 10, up 20, left 30, down 40, right 50, ... 
(increasing by 10, rotating RULD). Find position after n steps.
Example: n=3 fi -20 20    """
n = int(input())
x = 0
y = 0
for i in range(1, n + 1):

    d = i * 10

    if i % 4 == 1:
        x += d

    elif i % 4 == 2:
        y += d

    elif i % 4 == 3:
        x -= d

    else:
        y -= d

print(x, y)
""" Doctor's Daily Earnings
Fees by age: <17 fi 200 INR, 17–40 fi 400 INR, >40 fi 300 INR. Max 20 patients/day. Input ages until empty
line. Print total.
Example: ages=[20,30,40,50,2,3,14] fi Total Income 2000 INR"""
def doctor_income():

    total = 0

    for _ in range(20):

        age = input().strip()

        if age == "":
            break

        age = int(age)

        if age < 0 or age > 120:
            print("INVALID INPUT")
            return

        if age < 17:
            total += 200

        elif age <= 40:
            total += 400

        else:
            total += 300

    print("Total Income", total, "INR")

doctor_income()