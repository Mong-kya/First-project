import math

def calculator():
    print("Welcome to the calculate App")
    print("Choose from the following options.")
    print("1. Basic Calculator")
    print("2. Scientific Calculator")
    print("3. Unit conversion")
    print("4. Veiw History")
    print("5. Exit")

    History = []
    
    while True:
        try:
            choice = input("\nEnter the choice (1-2-3-4-5): ")
            
            if choice == "1":
                # Basic calculator
                num1_input = input("Enter first numbers: ")
                num1 = float(num1_input) if '.' in num1_input else int(num1_input)
                num2_input = input("Enter second numbers: ")
                num2 = float(num2_input) if '.' in num2_input else int(num2_input)

                operator = input("Enter the operator (+, -, *, /): ")

                if operator == "+":
                    result = num1 + num2
                elif operator == "-":
                    result = num1 - num2
                elif operator == "*":
                    result = num1 * num2
                elif operator == "/":
                    if num2  != 0:
                        result = num1 / num2
                    else:
                        print("Error: Division by zero is not Allowed.")
                        continue
                else:
                    print("Invalid operation. Please try again.")
                    continue

                print(f"The result is: {result}")
                History.append(f"{num1} {operator} {num2} = {result}")
            
            elif choice == "2":
                # Scientific calculator
                print("\nScientific Operations: ")
                print("1. sin(x)")
                print("2. cos(x)")
                print("3. tan(x)")
                print("4. log(x)")
                print("5. x^y")
                sci_choice = input("Choose and operation (1-2-3-4-5): ")

                num = float(input("Enter the number (or base number for x^y)"))

                if sci_choice == "1":
                    result = math.sin(math.radians(num))
                    print(f"sin({num}) = {result}")
                elif sci_choice == "2":
                    result = math.cos(math.radians(num))
                    print(f"cos({num}) = {result}")
                elif sci_choice == "3":
                    result = math.tan(math.radians(num))
                    print(f"tan({num}) = {result}")
                elif sci_choice == "4":
                    if num > 0:
                        result = math.log(num)
                        print(f"log({num}) = {result}")
                    else:
                        print("Error: logarithm is not defind for no-positivi numbers.")
                        continue

                elif sci_choice == "5":
                    power = float(input("Enter the power: "))
                    result = math.pow(num, power)
                    print(f"{num}^{power} = {result}")
                else:
                    print("Invalid scientific operation. please try agian.")
                
                History.append(f"Scientific Calculation Result: {result}")

            elif choice == "3":
                # Unit conversion
                print("\nUnit Conversion")
                print("1. Kilometers to Miles.")
                print("2. Kilograms to pounds.")
                print("3. Celsius to Fahrenheit")
                unit_choice = input("Choose an option (1-2-3): ")

                value = float(input("Enter the value of convert: "))

                if unit_choice == "1":
                    result = value * 0.6211371
                    print(f"{value} km = {result} miles.")
                elif choice == "2":
                    result = value * 2.20462
                    print(f"{value} kg = {result} lbs")
                elif choice == "3":
                    result = (value * 9/5) + 32
                    print(f"{value}°C = {result}°F")
                else:
                    print("Invalid unit conversion. Please try again.")
                    continue

                History.append(f"Unit Conversion: result = {result}")


            elif choice == "4":
                # veiw history
                print("\nCalculation History.")
                if History:
                    for record in History:
                        print(record)
                else:
                    print("No calculation yet.")
            
            elif choice == "5":
                # Exit
                print("Thank you for using the Advaced Calculator App.")
                break

            else:
                print("Invalid choice. Please select from the menu options.")
            

        except ValueError:
            print("Invalid input ! Please enter numeric numbers.")

        choice = input("Do you want to calculate again.?(yes/no): ").lower()
        if choice != "yes":
            print("Thank you for using the calculate App. ")
            break

calculator()
