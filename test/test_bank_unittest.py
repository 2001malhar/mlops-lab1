import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from bank_account import BankAccount, InsufficientFundsError, InvalidAmountError

class TestBankAccount(unittest.TestCase):
    
    def test_account_creation(self):
        """Test creating a new account"""
        account = BankAccount("John Doe", 1000)
        self.assertEqual(account.account_holder, "John Doe")
        self.assertEqual(account.get_balance(), 1000)
    
    def test_account_creation_negative_balance(self):
        """Test that negative initial balance raises error"""
        with self.assertRaises(InvalidAmountError):
            BankAccount("Jane Doe", -100)
    
    def test_deposit(self):
        """Test depositing money"""
        account = BankAccount("Alice", 500)
        new_balance = account.deposit(200)
        self.assertEqual(new_balance, 700)
        self.assertEqual(account.get_balance(), 700)
    
    def test_deposit_invalid_amount(self):
        """Test depositing invalid amount"""
        account = BankAccount("Bob", 500)
        with self.assertRaises(InvalidAmountError):
            account.deposit(-50)
        with self.assertRaises(InvalidAmountError):
            account.deposit(0)
    
    def test_withdraw(self):
        """Test withdrawing money"""
        account = BankAccount("Charlie", 1000)
        new_balance = account.withdraw(300)
        self.assertEqual(new_balance, 700)
        self.assertEqual(account.get_balance(), 700)
    
    def test_withdraw_insufficient_funds(self):
        """Test withdrawing more than balance"""
        account = BankAccount("David", 100)
        with self.assertRaises(InsufficientFundsError):
            account.withdraw(200)
    
    def test_withdraw_invalid_amount(self):
        """Test withdrawing invalid amount"""
        account = BankAccount("Eve", 500)
        with self.assertRaises(InvalidAmountError):
            account.withdraw(-50)
        with self.assertRaises(InvalidAmountError):
            account.withdraw(0)
    
    def test_transfer(self):
        """Test transferring money between accounts"""
        account1 = BankAccount("Frank", 1000)
        account2 = BankAccount("Grace", 500)
        
        account1.transfer(300, account2)
        
        self.assertEqual(account1.get_balance(), 700)
        self.assertEqual(account2.get_balance(), 800)
    
    def test_transfer_insufficient_funds(self):
        """Test transfer with insufficient funds"""
        account1 = BankAccount("Henry", 100)
        account2 = BankAccount("Ivy", 200)
        
        with self.assertRaises(InsufficientFundsError):
            account1.transfer(150, account2)
    
    def test_apply_interest(self):
        """Test applying interest"""
        account = BankAccount("Jack", 1000)
        new_balance = account.apply_interest(5)  # 5% interest
        self.assertEqual(new_balance, 1050)
    
    def test_apply_negative_interest(self):
        """Test that negative interest raises error"""
        account = BankAccount("Kate", 1000)
        with self.assertRaises(InvalidAmountError):
            account.apply_interest(-5)
    
    def test_transaction_history(self):
        """Test transaction history tracking"""
        account = BankAccount("Leo", 1000)
        account.deposit(500)
        account.withdraw(200)
        
        history = account.get_transaction_history()
        self.assertEqual(len(history), 2)
        self.assertIn("Deposited: $500", history)
        self.assertIn("Withdrew: $200", history)
    
    def test_account_string_representation(self):
        """Test string representation of account"""
        account = BankAccount("Maya", 1500)
        self.assertEqual(str(account), "Account Holder: Maya, Balance: $1500.00")

if __name__ == '__main__':
    unittest.main()