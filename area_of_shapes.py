import math
# Program to calculate the areas of square, rectangle and circle

# Square: s^2
# Ask for length of side
side_length = float(input("What is the length of a side of the square? "))

# Calculate the area of a square
calculate_square_area = side_length ** 2
# or side_length * side_length

# Print the area of a square
print(f"The area of the square is: {calculate_square_area}")

# Rectangle: l * w
# Ask for length
length_of_rectangle = float(input("What is the length of the rectangle? "))

# Ask for width
width_of_rectangle = float(input("What is the width of the rectangle? "))

# Calculate the area of a rectangle
calculate_rectangle_area = length_of_rectangle * width_of_rectangle

# Print the area of a rectangle
print(f"The area of the rectangle is: {calculate_rectangle_area}")

# Circle: Pi * r^2
# Ask for radius
radius_of_circle = float(input("What is the radius of the circle? "))

# Calculate the area of a circle
calculate_circle_area = math.pi * radius_of_circle ** 2

# Print the area of a circle
print(f"The area of the circle is: {calculate_circle_area}")


#### Square centimeters ####

# Square: s^2
# Ask for length of side in centimeters
side_length = float(input("What is the length of a side of the square (in cm)?  "))

# Calculate the area of a square
square_area = side_length ** 2
# or side_length * side_length

# Calculate m^2
square_area_in_meters = square_area / 10000

# Print the area of a square
print(f"The area of the square is: {calculate_square_area} cm^2 or {square_area_in_meters} m^2")

# Rectangle: l * w
# Ask for length
length_of_rectangle = float(input("What is the length of the rectangle (in cm)? "))

# Ask for width
width_of_rectangle = float(input("What is the width of the rectangle (in cm)? "))

# Calculate the area of a rectangle
rectangle_area = length_of_rectangle * width_of_rectangle

# Calculate m^2
rectangle_area_in_meters = rectangle_area / 10000

# Print the area of a rectangle
print(f"The area of the rectangle is: {rectangle_area} cm^2 or {rectangle_area_in_meters} m^2")

# Circle: Pi * r^2
# Ask for radius
radius_of_circle = float(input("What is the radius of the circle (in cm)? "))

# Calculate the area of a circle
circle_area = math.pi * radius_of_circle ** 2

# Calculate m^2
circle_area_in_meters = circle_area / 10000

# Print the area of a circle
print(f"The area of the circle is: {circle_area} cm^2 or {circle_area_in_meters} m^2")