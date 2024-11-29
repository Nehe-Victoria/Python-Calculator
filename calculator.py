def calculator():
    print("Welcome to Vicky Python Calculator!")
    print("Select an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    while True:
        try:
            # Get user input
            choice = input("Enter choice (1/2/3/4): ")
            if choice not in ('1', '2', '3', '4'):
                print("Invalid input. Please select 1, 2, 3, or 4.")
                continue

            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            # Perform the chosen operation
            if choice == '1':
                print(f"{num1} + {num2} = {num1 + num2}")
            elif choice == '2':
                print(f"{num1} - {num2} = {num1 - num2}")
            elif choice == '3':
                print(f"{num1} * {num2} = {num1 * num2}")
            elif choice == '4':
                if num2 != 0:
                    print(f"{num1} / {num2} = {num1 / num2}")
                else:
                    print("Error: Division by zero is undefined.")
            
            # Ask the user if they want to perform another calculation
            next_calculation = input("Do you want to perform another calculation? (yes/no): ").lower()
            if next_calculation != 'yes':
                print("Thank you for using the Python Calculator. Goodbye!")
                break
        except ValueError:
            print("Invalid input. Please enter numeric values.")

# Run the calculator
if __name__ == "__main__":
    calculator()
