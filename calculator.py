# Multiplication function
def multiply(x, y):
    return x * y

# Division function
def divide(x, y):
    return x / y

# Addition function
def add(x, y):
    return x + y

# Subtraction function
def subtract(x, y):
    return x - y


print("Select operation.")
print("For Multiply type 1")
print("For Divide type 2")
print("For Add type 3")
print("For Subtract type 4")

while True:
    # take input from the user
    choice = input("Enter choice(1/2/3/4): ")

    # check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == '1':
            print(num1, "x", num2, "=", multiply(num1, num2))

        elif choice == '2':
            print(num1, ":", num2, "=", divide(num1, num2))

        elif choice == '3':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '4':
            print(num1, "-", num2, "=", subtract(num1, num2))

        next_calculation = input("Do you want calculation again? (Y/N): ")
        if next_calculation == "N":
          break
    else:
        print("Invalid Input")
