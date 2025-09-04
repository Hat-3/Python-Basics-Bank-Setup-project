class bankacount :
        def __init__(self,name , amount):
                self.name = name
                self.amount = amount
               
        def balancecheck(self):
            print(f"{self.name} bank accound balance is {self.amount}")
        def deposit(self):
            add = int(input("Add the amound of money you want to Deposit = "))
            self.amount += add
        def withdrawal(self):
            withdraw = int(input("Enter the amount you want to Withdraw = "))
            if withdraw>self.amount :
                print("INSUFFICENT FUNDS")
            else:
                self.amount = self.amount - withdraw
                
            