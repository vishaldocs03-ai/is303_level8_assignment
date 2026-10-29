from bank_account import BankAccount


def get_dollar_amount(prompt):
    """Keep asking until the user enters a valid number, then return it rounded to cents."""
    while True:
        user_input = input(prompt + "\n").strip().replace("$", "").replace(",", "")
        try:
            return round(float(user_input), 2)
        except ValueError:
            print("Please enter a valid dollar amount.")


def make_deposit(account):
    amount = get_dollar_amount("How much would you like to deposit?")
    account.deposit(amount)


def make_withdrawal(account):
    amount = get_dollar_amount("How much would you like to withdraw?")
    account.withdraw(amount)


def view_account_information(account):
    account.display_account_info()


def display_menu():
    print("\nPlease choose an option:\n")
    print("1. Make a deposit")
    print("2. Make a withdrawal")
    print("3. View account information")
    print("4. Quit\n")


def main():
    print("Welcome to the Bank of Spencer!\n")

    customer_name = input("Please enter your name:\n").strip()
    while customer_name == "":
        customer_name = input("Name cannot be blank. Please enter your name:\n").strip()

    account = BankAccount(customer_name)

    display_menu()
    while True:
        choice = input().strip()

        if choice == "1":
            make_deposit(account)
        elif choice == "2":
            make_withdrawal(account)
        elif choice == "3":
            view_account_information(account)
        elif choice == "4":
            print("\nThank you for your business!")
            break
        else:
            print("Invalid choice. Please try again.")
            continue

        display_menu()


if __name__ == "__main__":
    main()
