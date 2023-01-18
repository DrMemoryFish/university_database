

# get user input for the first number
def get_first_number():
    try:
        first_num = int(input("Pick a First number:"))
        print(first_num)
    except ValueError:
        print("Please enter a valid number.")
    return first_num

# get user input for the second number
def get_second_number():
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
        print(operator)
        
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
        result = first_num / second_num
    else:
        print("Invalid operator. Please try again.")
    return result
# print the result of the math operation
print(result())