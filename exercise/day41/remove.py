print("Enter 'x' for exit.");
string = input("Enter any string to remove particular word: ");
if string == 'x':
    exit();
else:
    word = input("Enter word to be delete/remove: ");
    print("\nDeleting given word from the given string...");
    print("New String after successfully deleting",word);
    word_list = string.split();
    print(' '.join([i for i in word_list if i not in word]));
