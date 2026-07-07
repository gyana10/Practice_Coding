#A CHOCOLATE FACTORY PACKING A CHOCOLATE INTO PACKETS ,THE CHOCOLATE PACKETS HERE REPRESENTS AN ARRAY OF "n" NUMBER OF INTEGERS, THE TASK IS TO FIND EMPTY PACKETS AND PUSH INTO the end of AN ARRAY
arr=[int(i) for i in input().split()]
empty=[]
new=[]
for i in arr:
    if i==0:
        empty.append(i)
    else :   
        new.append(i)
arr[:]=new+empty        
print(arr)       
