import datetime;
print("Want to print Today's Date and Time ? (y/n): ");
check = input();
if check == 'n':
    exit();
else:
    print("\nToday's date and time:");
    print(datetime.datetime.today());
