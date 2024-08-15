try:
    width = float(input("What is the width of the rectangle: "))
    length = float(input("What is the length of the rectangle: "))
    if width == length:
        exit("Rectangle not square")

    area = width * length
    print(area)
except ValueError:
    print("Please enter a number")
