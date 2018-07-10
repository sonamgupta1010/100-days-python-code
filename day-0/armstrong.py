for n in range(1001):
    s=0
    x=n
    
    
    while x!=0:
        
        r=x%10
        s=s+r**3
        x=x//10
    if(s==n):
        print(n)
 
     
        
        
            
    
          
