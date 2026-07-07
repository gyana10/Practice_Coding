# a super market maintains pricing format for all it's products , a value 'n' is printed on all thhe products, when the scanner reads the value, the prodct of all the value n is th price of the product
num=int(input())
price=1
while num!=0:
    digit=num%10
    price=price*digit
    num=num//10
print(price)    
