def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero is not allowed."
def historyf(x):
    print("Calculation History:")
    if len(history) == 0:
        print("No calculations yet.")
        return
    else:
        for entry in history[-x:]:
            print(entry)
    

history = []

while True:
    operation = input("Enter the operation (+, -, *, /, or 'history' to view past results): ")
    if operation == 'history':
       ammount = int(input("Enter the amount of history to view: "))
       historyf(ammount)
       continue

    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    if operation == '+':
        result = add(num1, num2)
    elif operation == '-':
        result = subtract(num1, num2)
    elif operation == '*':
        result = multiply(num1, num2)
    elif operation == '/':
        result = divide(num1, num2)
    print("Result:", result)
    history.append(f"{num1} {operation} {num2} = {result}")


