# get user input for the first number
def get_first_number():
    while True:
        try:
            first_num = int(input("Pick a First number:"))
            print(first_num)
        except ValueError:
            print("Please enter a valid number.")
        return first_num

# get user input for the second number
def get_second_number():
    while True:
        try:
            second_num = int(input("Pick a Second number:"))
            print(second_num)
        except ValueError:
            print("Please enter a valid number.")
        return second_num

# get user input for the operator
def get_operator():
    operator = input("Pick an operator (+, -, *, /): ")
    if operator not in ["+", "-", "*", "/"]:
        print("Invalid operator. Please enter a valid operator (+, -, *, /)")
    else:
        return operator

def result():
    first_num = get_first_number()
    second_num = get_second_number()
    operator = get_operator()
    # use an if statement to carry out the math operation using the user's choice of numbers and operator
    if operator == "+":
        result = first_num + second_num
    elif operator == "-":
        result = first_num - second_num
    elif operator == "*":
        result = first_num * second_num
    elif operator == "/":
        if second_num == 0:
            print("Cannot divide by zero")
            return None
        else:
            return first_num / second_num
    else:
        print("Invalid operator. Please try again.")
    return None

# print the result of the math operation
print(result())