





def recur_factorial(n):
        if n==1:
            return n
        else:
            return n*recur_factorial(n-1)



n=int(input("please enter any number"))
if n<0:
    print("sorry,factorial does not exit for negative number")
elif n==0:
    print("factorial of 0 is 1")
else:
    print("the factorial of",n,"is",recur_factorial(n))


    

