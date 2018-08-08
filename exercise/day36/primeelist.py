def isPrime(n):
    if (n<2):
        return 0
    for i in range (2,n//2+1):
        if (n%i==0):
            return 0
    return 1
l=[]
b=int(input("enter higer range"))
print("enter number")
for x in range(b):
    data=int(input())
    l.append(data)
print (l)
print("prime list")
for x in range(b):
    if isPrime(x):
        print(x,end=',')
    




