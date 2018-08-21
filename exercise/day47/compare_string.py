print("Enter 'x' for exit.")
string1 = input("Enter first string: ")
if string1 == 'x':
    exit();
else:
    string2 = input("Enter second string: ")
    if string1 == string2:
        print("\nBoth strings are equal to each other.")
        print(string1,"==",string2);
    else:
        print("\nStrings are not equal.")
        print(string1,"!=",string2);
