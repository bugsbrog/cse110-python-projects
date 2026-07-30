# Ask the user for the grade
grade = float(input("What is the grade percent? "))

letter = ""

# Figure out the letter grade
if grade >= 90:
    letter = "A"
elif grade >= 80:
    letter = "B"
elif grade >= 70:
    letter = "C"
elif grade >= 60:
    letter = "D"
else:
    letter = "F"

# Get the last digit of letter grade
last_digit = grade % 10

sign = ""
# Determine the sign (+ or -)
if last_digit >= 7:
    sign = "+"
elif last_digit < 3:
    sign = "-"
else:
    sign = ""

# Handle exceptions (A+, F+, F-)
if letter == "A" and sign == "+":
    sign = ""

if letter == "F":
    sign = ""

# Display the letter grade
print(f"You have earned the grade {letter}{sign}")

# Let user know if they passed the course
if grade >= 70:
    print("Congratulations! You have passed the course!")
else:
    print("Sorry, please try the course again.")
