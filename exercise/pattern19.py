rows=int(input("enter no of rows"))
n=(rows+1)/2
k=0
for i in range(1,rows):
    
    if rows%2==0:
        if i<=n:
            k=k+1
        if i>n+1:
            k=k-1
    else:
        if i<=n:
            k=k+1
        else:
            k=k-1
            
    for j in range(1,rows):
        if j>=n+1-k and j<=n-1+k:
            print("*",end=" ")
        else:
            print(" ")
    print("\n")         
    
        
    
