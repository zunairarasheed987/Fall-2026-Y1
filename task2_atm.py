balance = 50000

while True:
    print("\n====== ATM Menu ======")
    print("1. Check balance")
    print("2. Deposit money")
    print("3. Withdraw money")
    print("4. Exit")

    try:
        choice = int(input("Enter your choice (1-4): "))
    except ValueError:
        print("Invalid input! Please enter a number between 1 and 4.")
        continue

    if choice == 1:
        print(f"Your current balance is Rs. {balance}")

    elif choice == 2:
        try:
            amount = float(input("Enter amount to deposit: "))
        except ValueError:
            print("Invalid amount!")
            continue

        if amount <= 0:
            print("Deposit amount must be greater than zero.")
        else:
            balance += amount
            print(f"Rs. {amount} deposited successfully. New balance: Rs. {balance}")

    elif choice == 3:
        try:
            amount = float(input("Enter amount to withdraw: "))
        except ValueError:
            print("Invalid amount!")
            continue

        if amount <= 0:
            print("Withdrawal amount must be greater than zero.")
        elif amount > balance:
            print("Insufficient balance! Withdrawal rejected.")
        else:
            balance -= amount
            print(f"Rs. {amount} withdrawn successfully. Remaining balance: Rs. {balance}")

    elif choice == 4:
        print("Thank you for using our ATM. Goodbye!")
        break

    else:
        print("Invalid choice! Please select 1, 2, 3 or 4.")
