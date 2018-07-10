x=12

for num in range(2,x+1):
    if(x%num==0):
        break
if(num==x):
    print(x,"is prime")
else:
    print(x,"is not prime")
    
