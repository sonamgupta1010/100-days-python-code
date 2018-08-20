print("Enter 'x' for exit.");
string = input("Enter any string to sort in alphabetical order: ")
if string == 'x':
    exit();
else:
    print("\nString after sorted in alphabetical order:");
    print(''.join(sorted(string)));
