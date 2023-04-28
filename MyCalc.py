# Define a function to take two numbers as input and return the result of the operation
def calculate(num1, num2, operation):
  # Check if the operation is valid
  if operation == "+":
    # Return the sum of the two numbers
    return num1 + num2
  elif operation == "-":
    # Return the difference of the two numbers
    return num1 - num2
  elif operation == "*":
    # Return the product of the two numbers
    return num1 * num2
  elif operation == "/":
    # Check if the second number is zero to avoid division by zero error
    if num2 == 0:
      # Print an error message and return None
      print("Error: Cannot divide by zero")
      return None
    else:
      # Return the quotient of the two numbers
      return num1 / num2
  else:
    # Print an error message and return None
    print("Error: Invalid operation")
    return None

# Ask the user to enter two numbers and an operation
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter the operation (+, -, *, /): ")

# Call the calculate function and store the result in a variable
result = calculate(num1, num2, operation)

# Check if the result is not None
if result is not None:
  # Print the result with formatting
  print(f"{num1} {operation} {num2} = {result}")
