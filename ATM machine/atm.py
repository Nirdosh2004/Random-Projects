from cardHolder import cardHolder

def print_menu():
    # print options to the user 
    print("Please choose from one of the following options.....")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Show Balance")
    print("4. Exit")

def deposit(account):
    try:
        deposit_amt = float(input("How much $$ do you like to deposit: "))     
        account.set_balance(account.get_balance() + deposit_amt)  
        print("Thank you for your $$ . Your new balance is: ", str(account.get_balance()))
    except ValueError:
        print("Invalid input")


def withdraw(cardHolder):
    try:
        withdraw_amt = float(input("How much $$ do you like to withdraw: ")) 
        if cardHolder.get_balance() < withdraw_amt:
            print("Insufficient Balance :( ")
        else:
            cardHolder.set_balance(cardHolder.get_balance() - withdraw_amt)
            print("You're good to go! Thank you :) ")
    except ValueError:
        print("Invalid input")

def check_balance(cardHolder):
    print("Your current balance is: ", cardHolder.get_balance())

if __name__ == "__main__":
    current_user = cardHolder("", "", "", "", "")

    list_of_cardHolders = [
        cardHolder("3434343434", 1234, "John", "Noida", 150.44),
        cardHolder("5857585958", 7645, "Rohan", "fazilnagar", 102.99),
        cardHolder("343984949", 3434, "Mohan", "mahason", 110.34),
        cardHolder("3434343348880", 9098, "Sohan", "gurwalia", 80.84),
        cardHolder("343434349004", 1877, "Shyam", "padrauna", 120.47)
    ]

    # prompt user for debit card number
    debitCardNum = ""
    while True:
        try:
            debitCardNum = input("Please insert your debit card number: ")
            # check against repository
            debitMatch = [holder for holder in list_of_cardHolders if holder.cardNum == debitCardNum]
            if len(debitMatch) > 0:
                current_user = debitMatch[0]
                break
            else:
                print("Card number not recognized. Please try again.")  
        except ValueError:
            print("Card number not recognized. Please try again.")      

    # prompt for pin
    while True:
        try:
            userPin = int(input("Please enter your pin: ").strip())   
            if current_user.get_pin() == userPin:
                break
            else:
                print("Invalid pin. Please try again.")
        except ValueError:
            print("Invalid pin. Please try again.")

    print("Welcome", current_user.get_firstname(), ":)")
    option = 0
    while True:
        print_menu()
        try:
            option = int(input())
        except ValueError:
            print("Invalid input. Please try again.")

        if option == 1:
            deposit(current_user)
        elif option == 2:
            withdraw(current_user)
        elif option == 3:
            check_balance(current_user)
        elif option == 4:
            break
        else:
            print("Invalid option. Please try again.")

    print("Thank you. Have a nice day :)")
    print("Created by `Nirdosh Kushwaha`")
