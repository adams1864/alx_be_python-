num1 = int(input("Enter the first number:)"))
num2 = int(input("Enter the first number:)"))
operation = input("Choose the operation (+, -, *, /):")
match  operation:
    case "+":
        print("The result is:",num1 + num2)
    case "-":
        print("The result is:",num1 - num2)
    case "*":
        print("The result is:",num1 * num2)
    case "/":
        print("The result is:",num1 / num2)
    case _ :
        print("Invalid operation")
