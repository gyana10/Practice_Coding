#covert the given decimal number to octal and print the octal number
def dec_oct(n):
    oct=" "
    while n>0:
        rem=n%8
        oct=str(rem)+oct
        n//=8
    return oct
n=int(input())
result=dec_oct(n)
print(result)    

#convert the given binary to octal and print the octal number
def bin_oct(n):
    dec=0
    i=0
    while n>0:
        rem=n%10
        dec+=rem*pow(2,i)
        n//=10
        i+=1
    oct=" "
    while dec>0:
        rem=dec%8
        oct=str(rem)+oct
        dec//=8
    return oct
n=int(input())
result=bin_oct(n)
print(result)
