
chance=1
while chance<=3:
    x=int(input("enter an even number"))
    if x%2==0:
        print("you win")
        break
    chance+=1
else:
    print("you lost")

 
