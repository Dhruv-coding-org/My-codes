# Ask the user to enter a number
num = float(input("Enter a number: "))

# Using nested if
if num >= 0:
    if num == 0:
        print("The number is zero.")
    else:
        print("The number is positive.")
else:
    print("The number is negative.")
