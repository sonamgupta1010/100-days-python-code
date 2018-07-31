for i in range(1,5):
    k=1
    for j in range(1,6):
        if (j<=5-k and j>=3+k):
            while(i<=4):
                k=k+1
            else:
                 k=k-1
                 print("*",end=" ")
        else:
             print(" ",end=" ")


    print("\n")       
