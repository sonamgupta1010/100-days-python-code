print("Enter 'x' for exit.");
string = input("Enter any string to copy: ");
if string == 'x':
    exit();
else:
    print("Copying string 1 (string) into string 2 (cstring)...");
    cstring = string;
    print("\nString 2 after successfully copied =",cstring);
    print("\nString 1 =",string,"\nString 2 =",cstring);
