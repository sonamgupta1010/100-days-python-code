
def isPrime(n):
    if (n<2):
        return 0
    for i in range (2,n//2+1):
        if (n%i==0):
            return 0
    return 1
a=int(input("enter lower range"))
b=int(input("enter higer range"))
for x in range(a,b):
    if isPrime(x):
        print(x,end=' ')
    
