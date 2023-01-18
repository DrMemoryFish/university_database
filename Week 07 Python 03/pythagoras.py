import math

# Shows the main menu to the user
def display_menu():
    print("Welcome to the Pythagoras Calculator")  # welcome message
    print("1. Calculate length of side A, Given B and C")  # option 1
    print("2. Calculate length of side B, Given A and C")  # option 2
    print("3. Calculate length of side C (Hypotenuse), Given A and B")  # option 3
    print("4. Exit")  # option 4

# Gets user's choice
def get_user_choice():
    while True:
        try:
            choice = int(input("Enter option: "))  # get user input
            return choice  # return user choice if it's valid
        except ValueError:
            # if the input is not a valid integer, display an error message
            print("Invalid input. Please enter a valid option.")

# checks that the user input is a positive float greater than zero
def get_length(side):
    while True:
        try:
            length = float(input(f"Enter length of side {side}: "))
            if length > 0:
                return length
            else:
                raise ValueError(
                    "Invalid input. Please enter a positive number.")
        except ValueError:
            print("Invalid input. Please enter a positive number.")
        except:
            print("Invalid input. Please enter a valid number.")

# define a function to calculate the length of side a
def length_a(b, c):
    if b >= c:
        # error message
        print("Error: Length of side B must be less than length of side C.")
        return
    a = math.sqrt(c**2 - b**2)  # use Pythagorean theorem
    print("Length of side A:", a)  # print result

# define a function to calculate the length of side b
def length_b(a, c):
    b = math.sqrt(c**2 - a**2)  # use Pythagorean theorem
    print("Length of side B:", b)  # print result

# define a function to calculate the length of side c
def length_c(a, b):
    if a <= 0 or b <= 0:
        print("Error: Invalid values for sides A or B.")  # error message
        return
    c = math.sqrt(a**2 + b**2)  # use Pythagorean theorem
    print("Length of side C:", c)  # print result


# main program loop
if __name__ == "__main__":
    while True:
        # displays main menu
        display_menu()
        # gets the users choice
        choice = get_user_choice()
        if choice == 1:
            b = float(input("Enter length of side B: "))
            c = float(input("Enter length of side C: "))
            length_a(b, c)
        elif choice == 2:
            a = float(input("Enter length of side A: "))
            c = float(input("Enter length of side C: "))
            length_b(a, c)
        elif choice == 3:
            a = float(input("Enter length of side A: "))
            b = float(input("Enter length of side B: "))
            length_c(a, b)
        elif choice == 4:
            print("Exiting Pythagoras's Calculator.")
            break
        else:
            print("Invalid option.")
