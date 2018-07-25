def recur_sum(n):
    if n<=1:
        return n
    else:
        return n+recur_sum(n-1)
num=int(input("please enter the number"))    
if num<0:
    print("enter a positive number")
else:
    print("the sum is",recur_sum(num))
    
