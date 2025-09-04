from bankbalance import *



def create_account():
    choice = input("Hello user, would you like to add an account? (yes/no): ").lower()
    if choice == "yes":
        name = input("Enter your name: ")
        amount = int(input("Enter initial deposit amount: "))
        account = bankacount(name, amount)
        print(f"Account created for {name} with balance {amount}")
        return account
    else:
        print("Bye!")
        return None
account = create_account()

while True :
    print()
    print("1.Show Balance")
    print("2.Deposit")
    print("3.Withdraw")
    print("4.Exist")
    
    print()
    Choice = int(input("How can we help you \n 1-4 == "))
    print()
    if Choice == 1:
        account.balancecheck()
    elif Choice == 2 :
        account.deposit()
    elif Choice == 3 :
        account.withdrawal()
    elif Choice == 4 :
        print("Thank you For working with us")
        break
    else : 
        print("INVALID OPTION")
        print("try again")