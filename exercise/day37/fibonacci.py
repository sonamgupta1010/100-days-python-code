a=0
b=1
c=0
x=int(input("Enter the size of fibonacci series="))
print(a," ",end="")
for i in range(x-1):
    if(i<=x):
        a=b
        b=c
        c=a+b
        print(c," ",end="")

# output:

# Enter the size of fibonacci series=10
# 0  1  1  2  3  5  8  13  21  34
