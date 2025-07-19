def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

def display(a, b, op, ans):
    print(f"The value of {a} {op} {b} = {ans}")

def get_second_value():
    val = int(input("Enter the second value: "))
    return val

def calculate(first_val):
    operation = str(input("Enter the operation to be done: \n+\n-\n*\n/\n"))
    if operation == "+":
        second_val = get_second_value()
        answer = add(first_val, second_val)
        display(first_val, second_val, '+', answer)

    elif operation == "-":
        second_val = get_second_value()
        answer = sub(first_val, second_val)
        display(first_val, second_val, '-', answer)

    elif operation == "*":
        second_val = get_second_value()
        answer = mul(first_val, second_val)
        display(first_val, second_val, '*', answer)

    elif operation == "/":
        second_val = get_second_value()
        answer = div(first_val, second_val)
        display(first_val, second_val, '/', answer)

    else:
        print("Invalid Entry!")

    first_val = answer

    continue_choice = input(f"Do you wish to continue calculating with {first_val}? \nType 'y' for yes, 'n' for no: ").lower()
    if continue_choice == 'y':
        calculate(answer)
    elif continue_choice == 'n':
        print("\n" * 20)
        new_calculate()
    else:
        print("Byeee")

def new_calculate():
    print("Welcome to the Pythonista Calculator!!")
    first_val = int(input("Enter the first value: "))
    calculate(first_val)

new_calculate()
