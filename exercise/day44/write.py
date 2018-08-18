print("Enter 'x' for exit.");
filename = input("Enter file name to create and write content: ");
if filename == 'x':
    exit();
else:
    c = open(filename, "w");
    print("\nThe file,",filename,"created successfully!");
    print("Enter 3 sentences to write on the file: ");
    sent1 = input();
    sent2 = input();
    sent3 = input();
    c.write(sent1);
    c.write("\n");
    c.write(sent2);
    c.write("\n");
    c.write(sent3);
    c.close();
    print("\nContent successfully placed inside the file.!!");
