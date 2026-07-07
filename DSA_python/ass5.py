"""25. The Utopian Tree goes through 2 cycles of growth every year. Each spring, it doubles in height.
Each summer, its height increases by 1 meter. Laura plants a Utopian Tree sapling with a height
of 1 meter at the onset of spring. How tall will her tree be after growth cycles?
For example, if the number of growth cycles is n=5, the calculations are as follows:
Periods Height
• 1
• 2
• 3
• 6
• 7
• 14
------------------------------------------"""
n=int(input())
H=1
for i in range(1,n+1):
    if i%2==0:
        H+=1
    else:
        H*=2
print(H)



"""49. Problem Statement
We want to estimate the cost of painting a property. Interior wall painting cost is Rs.18 per sq.ft. and
exterior wall painting cost is Rs.12 per sq.ft.
Take input as
1. Number of Interior walls
2. Number of Exterior walls
3. Surface Area of each Interior 4. Wall in units of square feet
Surface Area of each Exterior Wall in units of square feet
If a user enters zero as the number of walls then skip Surface area values as User may don’t want to
paint that wall.
Calculate and display the total cost of painting the property
Example 1:
6
3
12.3
15.2
12.3
15.2
12.3
15.2
10.10
10.10
10.00
Total estimated Cost : 1847.4 INR
Note: Follow in input and output format as given in above example
-----------------------------------------------------"""
n=int(input())
m=int(input())
cost=0
if n!=0:
    for i in range(n):
        cost+=18*float(input())
if m!=0:
    for i in range(m):
        cost+=12*float(input())
print("Total estimated Cost : ",cost,"INR")

"""50. Problem Statement
A City Bus is a Ring Route Bus which runs in circular fashion.That is, Bus once starts at the Source Bus
Stop, halts at each Bus Stop in its Route and at the end it reaches the Source Bus Stop again.
If there are n number of Stops and if the bus starts at Bus Stop 1, then after nth Bus Stop, the next stop
in the Route will be Bus Stop number 1 always.
If there are n stops, there will be n paths.One path connects two stops. Distances (in meters) for all paths
in Ring Route is given in array Path[] as given below:
Path = [800, 600, 750, 900, 1400, 1200, 1100, 1500]
Fare is determined based on the distance covered from source to destination stop as Distance between
Input Source and Destination Stops can be measured by looking at values in array Path[] and fare can be
calculated as per following criteria:
•If d =1000 metres, then fare=5 INR
•(When calculating fare for others, the calculated fare containing any fraction value should be
ceiled. For example, for distance 900n when fare initially calculated is 4.5 which must be ceiled
to 5)
Path is circular in function. Value at each index indicates distance till current stop from the previous one.
And each index position can be mapped with values at same index in BusStops [] array, which is a string
array holding abbreviation of names for all stops as-
“THANERAILWAYSTN” = ”TH”, “GAONDEVI” = “GA”, “ICEFACTROY” = “IC”, “HARINIWASCIRCLE” = “HA”,
“TEENHATHNAKA” = “TE”, “LUISWADI” = “LU”, “NITINCOMPANYJUNCTION” = “NI”,
“CADBURRYJUNCTION” = “CA”
Given, n=8, where n is number of total BusStops.
BusStops = [ “TH”, ”GA”, ”IC”, ”HA”, ”TE”, ”LU”, ”NI”,”CA” ]
Write a code with function getFare(String Source, String Destination) which take Input as source and
destination stops(in the format containing first two characters of the Name of the Bus Stop) and calculate
and return travel fare.Example 1:
Input Values
ca
Ca
Output Values
INVALID OUTPUT
Example 2:
Input Values
NI
HA
Output Values
23.0 INR"""
def getFare(Source,Destination):
    BusStops = [ "TH", "GA", "IC", "HA", "TE", "LU", "NI","CA" ]
    Path = [800, 600, 750, 900, 1400, 1200, 1100, 1500]
    if Source.upper() not in BusStops or Destination.upper() not in BusStops:
        return "INVALID OUTPUT"
    
