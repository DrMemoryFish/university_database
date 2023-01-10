# define the main balance variable
balance = 1000

# define a function to display the main menu
def display_menu():
  print("Welcome to the ATM")
  print("1. Withdraw")
  print("2. Deposit")
  print("3. Remove card")
  print("4. Display balance")

# Function to handle withdrawal
def withdraw(balance, amount):
    if amount > balance:
        print("Insufficient balance!")
    else:
        balance -= amount
    print(f"You have withdrawn ${amount}. Your new balance is ${balance}.")

# define a function to handle depositing money
def deposit(amount):
  global balance
  balance += amount
  print(f"You have deposited ${amount}. Your new balance is ${balance}.")

# define a function to handle removing the card
def remove_card():
  print("Thank you for using the ATM. Please make sure you take your card.")

# define a function to handle displaying the balance
def display_balance():
  global balance
  print(f"Your balance is ${balance}.")

def handle_withdrawal():
    # Define withdrawal options
    withdrawal_options = {
        1: 10,
        2: 20,
        3: 40,
        4: 60,
        5: 80,
        6: 100,
        7: None
    }
    # Keep prompting the user for input until a valid choice is made
    while True:
        # Display withdrawal options to the user
        display_withdrawal_options(withdrawal_options)
        withdrawal_choice = int(input())
        if withdrawal_choice == 8:
            break
        # Check if the user's choice is valid
        if not is_valid_withdrawal_choice(withdrawal_choice, withdrawal_options):
            print("Invalid choice. Please try again.")
            continue
        # Get the selected amount to withdraw
        amount = get_withdrawal_amount(withdrawal_choice, withdrawal_options)
        # Check if the withdrawal amount is valid
        if not is_valid_withdrawal_amount(amount):
            print("Invalid amount. Please try again.")
            continue
        # Withdraw the selected amount
        withdraw(balance, amount)
        break

def display_withdrawal_options(withdrawal_options):
    """
    Display the withdrawal options to the user.
    This function accepts a dictionary as a parameter and prints out
    the keys and values for the user to see.
    """
    print("Please select an amount to withdraw:")
    for key, value in withdrawal_options.items():
        if value:
            print(f"{key} - £{value}")
        else:
            print("7 - Other amount (must be multiple of 10)")
    print("8 - Return to main menu")

def is_valid_withdrawal_choice(choice, withdrawal_options):
    """
    Check if the user's choice is a valid option.
    This function accepts a choice and a dictionary of options as parameters,
    and checks if the choice is in the options.
    """
    return choice in withdrawal_options

def get_withdrawal_amount(choice, withdrawal_options):
    """
    Get the amount the user selected to withdraw.
    This function accepts a choice and a dictionary of options as parameters.
    If the choice is 7, it prompts the user to enter an amount and returns it.
    Otherwise, it returns the value corresponding to the choice from the options dictionary.
    """
    if choice == 7:
        return int(input("Enter amount to withdraw (must be multiple of 10): "))
    return withdrawal_options[choice]

def is_valid_withdrawal_amount(amount):
    """
    Check if the withdrawal amount is a multiple of 10.
    This function accepts an amount as a parameter, and checks if it is a multiple of 10.
    """
    return amount % 10 == 0

# main program loop
while True:
  # display the main menu
  display_menu()

  # ask the user to choose an option
  choice = int(input("Please enter your choice: "))

  # handle the user's choice
  if choice == 1:
      handle_withdrawal()
  elif choice == 2:
    amount = int(input("Enter amount to deposit: "))
    deposit(amount)
  elif choice == 3:
    remove_card()
    break
  elif choice == 4:
    display_balance()
  else:
    print("Invalid choice. Please try again.")