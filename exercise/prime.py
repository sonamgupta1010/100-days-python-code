a=int(input("enter smaller number"))
b= int(input("enter greatest number"))
s=range(a,b)
for x in s:
    for num in range(2,x):
        if x%num==0:
           break
    else:
        print (x," is prime in range")
        
    
