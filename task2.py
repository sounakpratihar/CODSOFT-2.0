def calculator():
    print("Welcome to the Simple Calculator!")
    print("Operations:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    while True:
        try:
            # Input two numbers
            num1 = float(input("\nEnter the first number: "))
            num2 = float(input("Enter the second number: "))

            # Choose an operation
            print("\nChoose an operation:")
            print("1. Addition")
            print("2. Subtraction")
            print("3. Multiplication")
            print("4. Division")
            choice = input("Enter your choice (1/2/3/4): ")

            # Perform the calculation
            if choice == "1":
                result = num1 + num2
                print(f"The result of addition is: {result}")
            elif choice == "2":
                result = num1 - num2
                print(f"The result of subtraction is: {result}")
            elif choice == "3":
                result = num1 * num2
                print(f"The result of multiplication is: {result}")
            elif choice == "4":
                if num2 != 0:
                    result = num1 / num2
                    print(f"The result of division is: {result}")
                else:
                    print("Error: Division by zero is not allowed.")
            else:
                print("Invalid choice. Please select 1, 2, 3, or 4.")

            # Ask to continue or exit
            cont = input("\nDo you want to perform another calculation? (yes/no): ").strip().lower()
            if cont != "yes":
                print("Thank you for using the calculator. Goodbye!")
                break

        except ValueError:
            print("Invalid input. Please enter numeric values.")

if _name_ == "_main_":
    calculator()