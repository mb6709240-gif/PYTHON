balance = 1000   # starting balance

while True:
    print("\n--- ATM MENU ---")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Your balance is:", balance)

    elif choice == 2:
        amount = int(input("Enter amount to deposit: "))
        balance += amount
        print("Deposited successfully!")
        print("New balance:", balance)

    elif choice == 3:
        amount = int(input("Enter amount to withdraw: "))
        if amount <= balance:
            balance -= amount
            print("Please collect your cash.")
            print("Remaining balance:", balance)
        else:
            print("Insufficient balance!")

    elif choice == 4:
        print("Thank you for using ATM!")
        break

    else:
        print("Invalid choice. Try again.")
