x=12
pos=0
for num in range(2,x):
        
        if x%num==0:
           pos=1     
           break 
           
           
if pos==0:
         print(x, "is prime")
else:
         print(x, "is not prime")
 
     
