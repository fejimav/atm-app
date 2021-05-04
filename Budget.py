class Budget: # class budget has been created
    
    def __init__(self, category): #initializer that can be used to instantiate objects. this is the init method
        self.category = category
        self.database = [
        
        ]

    def deposit(self, amount, description):
        self.database.apppend([amount, description]) 
        """This is a deposit method that accepts an amount and description then stores in the database
    
        """
    
    def withdrawal(self, amount, description):
        if(self.checkfunds (amount)):
            self.database.append([amount, description])
            return True 
        return False

    def getbalance(self):
        total = 0
        for item in self.database:
            total = total  + item [0]
        return total 

    def transfer(self, amount, category):
        if (self.checkfunds(amount)):
            self.withdraw(amount, "Transfer to" + category.category)
            category.deposit(amount, "transfer from" + self.category)
            return True
        return False
    def checkfunds(self, amount):
        """
        checkfunds method accpts an amount as an arguement. it return false if the amount is greater than the balance of the budget
        category and returns true otherwise. this method should be used by both the withdrawal method and transfer method
        """
        if (self.getbalance()>=amount):
            return True
        return False 
   