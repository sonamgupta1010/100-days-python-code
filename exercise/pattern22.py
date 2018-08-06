k=0
for i in range(1,6):
    if i%2==1:
        k=k+1
    else:
        k=k-1
        k=k+i
    flag=1
    p=k
    
    for j in range(1,10):
        if j<= 2*i-1:
            if flag==1 :
                print(p,end=" ")
                if i%2:
                    k=k+1
                    p=p+1
                else:
                    p=p+1
            else:
                print("*",end="")
            flag=1-flag
                
                
        else:
            print(" ",end=" ")
    print("\n")
