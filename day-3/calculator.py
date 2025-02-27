while True:  # Loop to run the calculator multiple times
    print("📌 \nChoose Operation:")
    print("1️⃣. Addition (+)")
    print("2️⃣. Subtraction (-)")
    print("3️⃣. Multiplication (*)")
    print("4️⃣. Division (/)")
    print("5️⃣. Exit")  # Exit option added

    choice = input("📝Enter your choice (1-5): ")

    if choice == '5':  # Exit condition
        print("Exiting Calculator... Goodbye!")
        break  # Proper indentation

    num1 = int(input("✅ Enter first number: "))
    num2 = int(input("✅ Enter second number: "))

    if choice == '1':
        result = num1 + num2
        operation = "+"

    elif choice == '2':
        result = num1 - num2
        operation = "-"

    elif choice == '3':
        result = num1 * num2
        operation = "*"

    elif choice == '4':
        if num2 == 0:
            print(" ❌ Error: Division by zero is not allowed!")
            continue  # Skip this iteration and restart loop
        
        result = num1 / num2
        operation = "/"

    else:
        print("Invalid choice! Please enter a number between 1-5.")
        continue  # Restart loop for valid input

    result = round(result, 2)  # Round-off to 2 decimal places

    print("\nCalculating...")
    print(f"{num1} {operation} {num2} = {result}")
