for i in range(1,8):
    k=0
    if i<=4:
        k=k+1
    else:
        k=k-1
    for j in range(1,8):
        if j>=5-k and j<=3+k:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print("\n")        
            
