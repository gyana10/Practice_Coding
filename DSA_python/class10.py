"""Chain Marketing Organization has has a scheme for income generation, through which its members
generate income for themselves. The scheme is such that suppose A joins the scheme and makes R and V
to join this scheme then A is Parent Member of R and V who are child Members. When any member
joins the scheme then the parent gets total commission of 10% from each of its child members.
Child members receive commission of 5% respectively. If a Parent member does not have any member
joined under him, then he gets commission of 5%.
Take name of the members joining the scheme as input.
Display how many members joined the scheme including parent member.Calculate the Total commission
gained by each members in the scheme. The fixed amount for joining the scheme is Rs.5000 on which
commission will be generated
SchemeAmount = 5000
Example 1: When there are more than one child members
Input : (Do not give input prompts.Accept values as follows. )
Amit //Enter parent Member as this
Y //Enter Y if Parent member has child members otherwise enter N
Rajesh,Virat //Enter names of child members of Amit in comma separated
Output:(Final Output must be in format given below.)
TOTAL MEMBERS:3
COMISSION DETAILS
Amit: 1000 INR
Rajesh :250 INR
Virat: 250 INR
Example 2: When there is only one child member in the hierarchy
Input :
Amit
Y
Rajesh
Output:
Total Members: 2
Comission Details
Amit: 500 INR
Rajesh: 250 INR
parent = i
----------------------------------------------------------"""
def calculate_commission():
    parent_member = input()
    has_child = input()
    if has_child == 'Y':
        child_members = input().split(',')
        total_members = 1 + len(child_members)
        print(f'TOTAL MEMBERS:{total_members}')
        print('COMISSION DETAILS')
        print(f'{parent_member}: {5000 * 0.10 * len(child_members)} INR')
        for child in child_members:
            print(f'{child.strip()}: {5000 * 0.05} INR')
    elif has_child == 'N':
        print('TOTAL MEMBERS:1')
        print('COMISSION DETAILS')
        print(f'{parent_member}: {5000 * 0.05} INR')
    else:
        print('INVALID INPUT')
name = input()

calculate_commission(name)          



"""53. Problem StatementFULLY AUTOMATIC VENDING MACHINE – dispenses your cuppa on just press of button. A vending
machine can serve range of products as follows:
Coffee
1. Espresso Coffee
2. Cappuccino Coffee
3. Latte Coffee
Tea
1. Plain Tea
2. Assam Tea
3. Ginger Tea
4. Cardamom Tea
5. Masala Tea
6. Lemon Tea
7. Green Tea
8. Organic Darjeeling Tea
Soups
1. Hot and Sour Soup
2. Veg Corn Soup
3. Tomato Soup
4. Spicy Tomato Soup
Beverages
1. Hot Chocolate Drink
2. Badam Drink
3. Badam-Pista Drink
Write a program to take input for main menu & sub menu and display the name of sub menu selected
in the following format (enter the first letter to select main menu):
Welcome to CCD
Enjoy your
Example 1:
Input:
c
1
Output
Welcome to CCD!
Enjoy your Espresso Coffee!
Example 2:
Input:
t
9
Output
INVALID OUTPUT!
-----------------------------------------------------------------------------"""
def vending_machine():
    print("Welcome to CCD!")
    main_menu = input()
    sub_menu = int(input())
    
    if main_menu == 'c':
        if sub_menu == 1:
            print("Enjoy your Espresso Coffee!")
        elif sub_menu == 2:
            print("Enjoy your Cappuccino Coffee!")
        elif sub_menu == 3:
            print("Enjoy your Latte Coffee!")
        else:
            print("INVALID OUTPUT!")
    elif main_menu == 't':
        if sub_menu == 1:
            print("Enjoy your Plain Tea!")
        elif sub_menu == 2:
            print("Enjoy your Assam Tea!")
        elif sub_menu == 3:
            print("Enjoy your Ginger Tea!")
        elif sub_menu == 4:
            print("Enjoy your Cardamom Tea!")
        elif sub_menu == 5:
            print("Enjoy your Masala Tea!")
        elif sub_menu == 6:
            print("Enjoy your Lemon Tea!")
        elif sub_menu == 7:
            print("Enjoy your Green Tea!")
        elif sub_menu == 8:
            print("Enjoy your Organic Darjeeling Tea!")
        else:
            print("INVALID OUTPUT!")
    elif main_menu == 's':
        if sub_menu == 1:
            print("Enjoy your Hot and Sour Soup!")
        elif sub_menu == 2:
            print("Enjoy your Veg Corn Soup!")
        elif sub_menu == 3:
            print("Enjoy your Tomato Soup!")
        elif sub_menu == 4:
            print("Enjoy your Spicy Tomato Soup!")
        else:
            print("INVALID OUTPUT!")
    elif main_menu == 'b':
        if sub_menu == 1:
            print("Enjoy your Hot Chocolate Drink!")
        elif sub_menu == 2:
            print("Enjoy your Badam Drink!")
        elif sub_menu == 3:
            print("Enjoy your Badam-Pista Drink!")
        else:
            print("INVALID OUTPUT!")
    else:
        print("INVALID OUTPUT!")
vending_machine()




"""51. Problem Statement
There are total n number of Monkeys sitting on the branches of a huge Tree. As travelers offer Bananas
and Peanuts, the Monkeys jump down the Tree. If every Monkey can eat k Bananas and j Peanuts. If total
m number of Bananas and p number of Peanuts are offered by travelers, calculate how many Monkeys
remain on the Tree after some of them jumped down to eat.
At a time one Monkeys gets down and finishes eating and go to the other side of the road. The Monkey
who climbed down does not climb up again after eating until the other Monkeys finish eating.
Monkey can either eat k Bananas or j Peanuts. If for last Monkey there are less than k Bananas left on the
ground or less than j Peanuts left on the ground, only that Monkey can eat Bananas(<k) along with the
Peanuts(<j).Write code to take inputs as n, m, p, k, j and return the number of Monkeys left on the Tree.
Where, n= Total no of Monkeys
k= Number of eatable Bananas by Single Monkey (Monkey that jumped down last may get less than k
Bananas)
j = Number of eatable Peanuts by single Monkey(Monkey that jumped down last may get less than j
Peanuts)
m = Total number of Bananas
p = Total number of Peanuts
Remember that the Monkeys always eat Bananas and Peanuts, so there is no possibility of k and j havinga value zero
Example 1:
Input Values
20
2
3
12
12
Output Values
Number of Monkeys left on the tree:10
Note: Kindly follow the order of inputs as n,k,j,m,p as given in the above example. And output must
include the same format as in above example(Number of Monkeys left on the Tree:)
For any wrong input display INVALID INPUT"""
def monkeys_on_tree():
    n = int(input())
    k = int(input())
    j = int(input())
    m = int(input())
    p = int(input())
    
    if k <= 0 or j <= 0:
        print("INVALID INPUT")
        return
    
    monkeys_eaten = 0
    
    while monkeys_eaten < n and (m >= k or p >= j):
        if m >= k:
            m -= k
        else:
            m = 0
        
        if p >= j:
            p -= j
        else:
            p = 0
        
        monkeys_eaten += 1
    
    monkeys_left = n - monkeys_eaten
    print(f"Number of Monkeys left on the Tree:{monkeys_left}")
monkeys_on_tree()