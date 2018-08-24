print("Enter 'x' for exit.");
hexdec = input("Enter a number in Hexadecimal Format: ");
if hexdec == 'x':
    exit();
else:
    dec = int(hexdec, 16);
    print(hexdec,"in Octal =",oct(dec));
