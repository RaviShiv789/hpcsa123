# Accept two numbers from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Perform the calculations
addition = num1 + num2
squared = num1 ** 2
power = num1 ** num2

# Print the results
print("The addition of", num1, "and", num2, "is", addition)
print(num1, "squared is", squared)
print(num1, "raised to the power of", num2, "is", power)
