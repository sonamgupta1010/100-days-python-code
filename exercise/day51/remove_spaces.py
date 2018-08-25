print("Enter 'x' for exit.");
string = input("Enter any string to remove all spaces: ");
if string == 'x':
    exit();
else:
    new_string = string.replace(" ","");
    print("\nNew string after removing all spaces:");
    print(new_string);
