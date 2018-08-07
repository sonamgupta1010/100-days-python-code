winning_number=29

pos=0

print("Number guessing game")

print("If the input number is equal to winning number then you win the game")

for i in range(1,6):
    if (i==1):
        input_number=int(input("Enter any number between 1 to 100\n"))
    else:
        input_number=int(input("Try again = "))

    if(input_number==winning_number):
        pos=1
        break
    
    elif(input_number < 20):
        print("Too Low")

    elif(input_number > 40):
        print("Too High")

    elif(input_number < 29):
        print("Too Close")

    else:
        print("Too Close")  

if(pos==0):
    print("You Loose")
else:    
    print("You Win.")
print("winning Number is ",winning_number)

# output:

# Number guessing game
# If the input number is equal to winning number then you win the game
# Enter any number between 1 to 100
# 26
# Too Close
# Try again = 19
# Too Low
# Try again = 39
# Too Close
# Try again = 42
# Too High
# Try again = 29
# You Win.
