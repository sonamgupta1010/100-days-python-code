import os;
print("Enter 'x' for exit.");
filename = input("Enter name of file to delete: ");
if filename == 'x':
    exit();
else:
    print("\nRemoving the file....");
    os.remove(filename);
    print("\nFile,",filename,"successfully deleted!!");
