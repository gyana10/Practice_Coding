"""22. You have been asked to help study the population of birds migrating across the continent. Each
type of bird you are interested in will be identified by an integer value. Each time a particular kind
of bird is spotted, its id number will be added to your array of sightings.
You would like to be able to find out which type of bird is most common given a list of sightings. Your
task is to print the type number of that bird and if two or more types of birds are equally common,
choose the type with the smallest ID number.
For example, assume your bird sightings are of types arr = [ 1,1,2,2,3]. There are two each of types 1
and 2, and one sighting of type 3. Pick the lower of the two types seen twice: type 1.
--------------------------------------------------------"""
a=int(input())
b=list(map(int,input().split()))
out=[]
for i in range(1,6):
    out.append(b.count(i))
print(out.index(max(out))+1)






"""37. Two cats and a mouse are at various positions on a line. You will be given their starting positions. Your
task is to determine which cat will reach the mouse first, assuming the mouse doesn’t move and the cats
travel at equal speed. If the cats arrive at the same time, the mouse will be allowed to move and it will
escape while they fight.
You are given q queries in the form of x ,y and ,z representing the respective positions for
cats A and B and for mouse C .
Complete the function catAndMouse to return the appropriate answer to each query, which will be
printed on a new line.
•If cat A catches the mouse first, print Cat A.
•If cat B catches the mouse first, print Cat B.
•If both cats reach the mouse at the same time, print Mouse Cas the two cats fight and mouse
escapes.
For example, cat A is at position x=2 and cat B is at y=5 . If mouse C is at position z=4,It is 2 units from
cat A and 1 unit from cat B. Cat B will catch the mouse.
Function Description
Complete the catAndMouse function in the editor below. It should return one of the three strings as
described.
catAndMouse has the following parameter(s):
•x: an integer, Cat A‘s position
•y: an integer, Cat B’s position
•z: an integer, Mouse C‘s position
Input Format
The first line contains a single integer q, denoting the number of queries.
Each of the q subsequent lines contains three space-separated integers describing the respective values
of x (catA ‘s location) ,y (catB ‘s location), and z (mouse C’s location).
Output Format
For each query, return Cat A if cat A catches the mouse first, Cat B if cat B catches the mouse first,
or Mouse C if the mouse escapes.
Sample Input 0
2
1 2 3
1 3 2
Sample Output 0
Cat B
Mouse C
-----------------------------------------------------------------------------------"""
for i in range(int(input())):
    a,b,c=map(int,input().split())
    x="Cat A"
    y="Cat B"
    z="Mouse C"
    if abs(a-c)<abs(b-c):
        print(x)
    elif abs(a-c)>abs(b-c):
        print(y)
    else:
        print(z)

"""38. You will be given an array of integers. All of the integers except one occur twice. That one is unique in the
array.
Given an array of integers, find and print the unique element.
For example a=[1,2,3,4,3,2,1] the unique element is 4.
Function Description
Complete the lonelyinteger function in the editor below. It should return the integer which occurs only
once in the input array.
lonelyinteger has the following parameter(s):
•a: an array of integers
Input Format
The first line contains a single integer n denoting the number of integers in the array.
The second line contains n space-separated integers describing the values in a.
Output Format
Print the unique integer in the array.
Sample Input 0
1
1
Sample Output 0
1
------------------------------------------------------------------------------"""
n = int(input())
a = list(map(int, input().split()))

for num in set(a):
    if a.count(num) == 1:
        print(num)
        break







"""70. Q1) Given an array of integers where every element appears even number of times except one element
which appears odd number of times, write a program to find that odd occurring element in O(log n)
time. The equal elements must appear in pairs in the array but there cannot be more than two
consecutive occurrences of an element.
For example :
3
2 3 2
It doesn't have equal elements appear in pairs
7
1 1 2 2 2 3 3
It contains three consecutive instances of an element.
5
2 2 3 1 1
It is valid and the odd occurring element present in it is 3.
Enter only valid inputs.
Sample Input :
5
2 2 3 1 1
Sample Output :
3.
----------------------------------------------------------------------------------------"""
def find_odd(arr):
    low = 0
    high = len(arr) - 1

    while low < high:
        mid = (low + high) // 2

        if mid % 2 == 1:
            mid -= 1

        if arr[mid] == arr[mid + 1]:
            low = mid + 2
        else:
            high = mid

    return arr[low]

n = int(input())
arr = list(map(int, input().split()))

print(find_odd(arr))





