class InsufficientFundsError(Exception):
    """Custom exception for insufficient funds"""
    pass

class InvalidAmountError(Exception):
    """Custom exception for invalid amount"""
    pass

class BankAccount:
    """Bank Account Management System"""
    
    def __init__(self, account_holder, initial_balance=0):
        """Initialize bank account"""
        if initial_balance < 0:
            raise InvalidAmountError("Initial balance cannot be negative")
        self.account_holder = account_holder
        self.balance = initial_balance
        self.transaction_history = []
    
    def deposit(self, amount):
        """Deposit money into account"""
        if amount <= 0:
            raise InvalidAmountError("Deposit amount must be positive")
        self.balance += amount
        self.transaction_history.append(f"Deposited: ${amount}")
        return self.balance
    
    def withdraw(self, amount):
        """Withdraw money from account"""
        if amount <= 0:
            raise InvalidAmountError("Withdrawal amount must be positive")
        if amount > self.balance:
            raise InsufficientFundsError("Insufficient funds for withdrawal")
        self.balance -= amount
        self.transaction_history.append(f"Withdrew: ${amount}")
        return self.balance
    
    def get_balance(self):
        """Get current balance"""
        return self.balance
    
    def transfer(self, amount, recipient_account):
        """Transfer money to another account"""
        if amount <= 0:
            raise InvalidAmountError("Transfer amount must be positive")
        if amount > self.balance:
            raise InsufficientFundsError("Insufficient funds for transfer")
        
        self.withdraw(amount)
        recipient_account.deposit(amount)
        self.transaction_history.append(f"Transferred: ${amount} to {recipient_account.account_holder}")
        return self.balance
    
    def apply_interest(self, rate):
        """Apply interest rate to balance"""
        if rate < 0:
            raise InvalidAmountError("Interest rate cannot be negative")
        interest = self.balance * (rate / 100)
        self.balance += interest
        self.transaction_history.append(f"Interest applied: ${interest:.2f} at {rate}%")
        return self.balance
    
    def get_transaction_history(self):
        """Get list of all transactions"""
        return self.transaction_history
    
    def __str__(self):
        """String representation of account"""
        return f"Account Holder: {self.account_holder}, Balance: ${self.balance:.2f}"