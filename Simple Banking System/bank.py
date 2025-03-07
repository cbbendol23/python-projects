# Banking Program (following Bro Code's yt tutorial)
import time

balance = 0
is_running = True

def show_balance():
    print(f"Your balance is ${balance:.2f}")
    time.sleep(2)

def deposit():
    global balance
    amount = float(input("Enter amount to deposit: $"))

    if amount <= 0:
        print("Invalid amount. Please try again.")
        time.sleep(2)
        return
    
    balance += amount
    print(f"Successfully deposited ${amount:.2f} into your account.")
    time.sleep(2)

def withdraw():
    global balance
    amount = float(input("Enter amount to withdraw: $"))

    if amount <= 0:
        print("Invalid amount. Please try again.")
        time.sleep(2)
        return
    
    if amount > balance:
        print("Insufficient funds. Please try again.")
        time.sleep(2)
        return
    
    balance -= amount
    print(f"Successfully withdrew ${amount:.2f} from your account.")
    time.sleep(2)


while is_running:
    print()
    print("Banking Program")
    print("1. Show Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    print()
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        show_balance()

    elif choice == "2":
        deposit()

    elif choice == "3":
        withdraw()

    elif choice == "4":
        print("Exiting program...")
        time.sleep(2)
        is_running = False

    else:
        print("Invalid input. Please try again.")


print("Have a nice day!")