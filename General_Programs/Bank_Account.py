class Account():
    
    def __init__(self,owner,balance):
        self.owner =owner
        self.balance = balance
              
        
    def __str__(self):
        #Has to print Account Owners name and the balance in the persons account
        return f"Account Owner: {self.owner} \nAccount Balance: ${self.balance}"
    
    def deposit(self,amount):
        self.balance = self.balance + amount 
        print (f"You have successfully deposited ${amount} to your account \n Account balance = ${self.balance}")
    
    
    def withdraw(self,amount):
        #withdrawal amount should not exceed the total balance available
        if self.balance >= amount:
            self.balance = self.balance - amount
            print (f"Withdrawal of ${amount} Accepted\nAccount balance = ${self.balance}")
        else: 
            print (f"Oops! your requested cannot be processed\nAccount Balance: ${self.balance}")
    
   