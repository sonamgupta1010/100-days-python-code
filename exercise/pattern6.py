for i in range (1,4):
    k=1
    for j in range (1,7):
        if j>=5-i and j<=3+i:
            print(k,end="\t")
            j<4?k=k+1:k=k-1
        else:
            print(" ",end="\t")
            
