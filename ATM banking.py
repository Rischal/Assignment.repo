balance = 5000
print("welcome to the atm!")
print("1. Balance Inquiry")
print("2. Withdraw Cash")
print("3. Deposit cash")
print("4. Exit")
choice = int(input("Please inter your choice (1-4): "))
if choice == 1:
    print(f"Your current balance is: {balance}")
elif choice ==2:
    amount = int (input("Enter the amount to withdraw:"))
    if amount > balance:
        print("Insufficient balance.")
    else:
        balance -= amount
        print(f"Withdraw successful your new balance is: {balance}")
elif choice == 3:
    amount =int(input("Enter the amount to deposit:"))
    if amount <= 0:
        print("Invalid amount. Please enter a positive value.")
    else:
        balance += amount
        print(f"Deposit successful! Yournew balance is: {balance}")
elif choice == 4:
    print("Thank you for using the ATM. Goodbye!")
else:
    print("Invalid choice. Please try again.")