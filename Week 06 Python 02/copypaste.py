def display_menu():
  print("Welcome to the ATM")
  print("1. Withdraw")
  print("2. Deposit")
  print("3. Remove card")
  print("4. Display balance")

def handle_withdrawal():
    withdrawal_options = {
        1: 10,
        2: 20,
        3: 40,
        4: 60,
        5: 80,
        6: 100,
        7: None
    }
    print("Please select an amount to withdraw:")
    for key,value in withdrawal_options.items():
        if value:
            print(f"{key} - £{value}")
        else:
            print("7 - Other amount (must be multiple of 10)")
    print("8 - Return to main menu")
    withdrawal_choice = int(input())
    if withdrawal_choice in withdrawal_options:
        if withdrawal_choice == 7:
            amount = int(input("Enter amount to withdraw (must be multiple of 10): "))
            if amount % 10 == 0:
                withdraw(amount)
            else:
                print("Invalid amount. Please try again.")
        else:
            withdraw(withdrawal_options[withdrawal_choice])
    elif withdrawal_choice == 8:
        pass
    else:
        print("Invalid choice. Please try again.")

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
