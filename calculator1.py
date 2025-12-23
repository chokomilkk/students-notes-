def Calculator():
    while True:
        try:
            x = int(input("Enter a number: "))
            y = int(input("Enter another number: "))
            operation = input("Enter operation: +, -, *, / ")
            if operation == "+":
                result = x + y
                print("The result is: ", result)
            elif operation == "-":
                result = x - y
                print("The result is: ", result)
            elif operation == "*":
                result = x * y
                print("The result is: ", result)
            elif operation == "/":
                if y != 0:
                    result = x / y
                    print("The result is: ", result)
                else:
                    print("you cannot divide by zero")
            повторить = input("do you want to continue? (y/n): ")
            if повторить == "n":
                break
        except ValueError:
            print("please enter a number")
Calculator()