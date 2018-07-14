x=121
temp=x
y=0
r=0
while temp>0:
    r=temp%10
    y=y*10+r
    temp//=10
if(y==x):
    print(y,"is palindrome")
else:
    print(y,"is not palindrome")
