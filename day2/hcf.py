x=int(input("enter first number"))
y=int(input("enter second number"))
if x>y:
    smaller=y
else:
    smaller=x
    for i in range(1,smaller+1):
    
        if x%i==0and y%i==0:
            hcf=i
            
    print(hcf)        
             
