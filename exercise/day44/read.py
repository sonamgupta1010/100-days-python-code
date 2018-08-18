print("Enter 'x' for exit.");
filename = input("Enter file name (with extension) to read: ");
if filename == 'x':
    exit();
else:
    c = open(filename, "r");
    print("\nThe file,",filename,"opened successfully!");
    print("The file",filename,"contains:\n");
    print(c.read())
    c.close()
