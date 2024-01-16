print("Welcome to the Shape Calculator!!")

while True:
    print("1. Triangle")
    print("2. Rectangle")
    print("3. Square")
    print("4. Circle\n")
    
    option = int(input("Enter the number for the shape you want to calculate: "))
    
    if option == 1:
        a = float(input("Enter the length of side A: "))
        b = float(input("Enter the length of side B: "))
        c = float(input("Enter the length of side C: "))
        perimeter = a + b + c
        area = 0.5 * a * b  # This is a simple way to approximate triangle area
        print("The perimeter of the triangle is:",perimeter)
        print("\nThe area of the triangle is:",area)
    elif option == 2:
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))
        perimeter = 2 * (length + width)
        area = length * width
        print("The perimeter of the rectangle is:",perimeter)
        print("\nThe area of the rectangle is:",area)
    elif option == 3:
        side = float(input("Enter the length of the square's side: "))
        perimeter = 4 * side
        area = side ** 2
        print("The perimeter of the square is:",perimeter)
        print("\nThe area of the square is:",area)
    elif option == 4:
        radius = float(input("Enter the radius of the circle: "))
        circumference = 2 * 3.14159 * radius
        area = 3.14159 * radius ** 2
        print("The circumference of the circle is:",circumference)
        print("\nThe area of the circle is:",area)
    else:
        print("Invalid choice. Please select a valid option.")
