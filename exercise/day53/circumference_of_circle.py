print("Enter 'x' for exit.");
rad = input("Enter radius of circle: ");
if rad == 'x':
    exit();
else:
    radius = float(rad);
    circumference = 2*3.14*radius;
    print("\nCircumference of Circle =",circumference);
