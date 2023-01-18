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
def withdraw(amount):
  global balance
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

# main program loop
while True:
  # display the main menu
  display_menu()

  # ask the user to choose an option
  choice = int(input("Please enter your choice: "))

  # handle the user's choice
  if choice == 1:
      print("Please select an amount to withdraw:")
      print("1 - £10")
      print("2 - £20")
      print("3 - £40")
      print("4 - £60")
      print("5 - £80")
      print("6 - £100")
      print("7 - Other amount (must be multiple of 10)")
      print("8 - Return to main menu")
      withdrawal_choice = int(input())
      if withdrawal_choice == 1:
        withdraw(10)
      elif withdrawal_choice == 2:
        withdraw(20)
      elif withdrawal_choice == 3:
        withdraw(40)
      elif withdrawal_choice == 4:
        withdraw(60)
      elif withdrawal_choice == 5:
        withdraw(80)
      elif withdrawal_choice == 6:
        withdraw(100)
      elif withdrawal_choice == 7:
        amount = int(input("Enter amount to withdraw (must be multiple of 10): "))
        if amount % 10 == 0:
          withdraw(amount)
        else:
          print("Invalid amount. Please try again.")
      elif withdrawal_choice == 8:
        continue
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