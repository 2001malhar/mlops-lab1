import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from bank_account import BankAccount, InsufficientFundsError, InvalidAmountError
import pytest

def test_account_creation():
    """Test creating a new account"""
    account = BankAccount("John Doe", 1000)
    assert account.account_holder == "John Doe"
    assert account.get_balance() == 1000

def test_account_creation_negative_balance():
    """Test that negative initial balance raises error"""
    with pytest.raises(InvalidAmountError):
        BankAccount("Jane Doe", -100)

def test_deposit():
    """Test depositing money"""
    account = BankAccount("Alice", 500)
    new_balance = account.deposit(200)
    assert new_balance == 700
    assert account.get_balance() == 700

def test_deposit_invalid_amount():
    """Test depositing invalid amount"""
    account = BankAccount("Bob", 500)
    with pytest.raises(InvalidAmountError):
        account.deposit(-50)
    with pytest.raises(InvalidAmountError):
        account.deposit(0)

def test_withdraw():
    """Test withdrawing money"""
    account = BankAccount("Charlie", 1000)
    new_balance = account.withdraw(300)
    assert new_balance == 700
    assert account.get_balance() == 700

def test_withdraw_insufficient_funds():
    """Test withdrawing more than balance"""
    account = BankAccount("David", 100)
    with pytest.raises(InsufficientFundsError):
        account.withdraw(200)

def test_withdraw_invalid_amount():
    """Test withdrawing invalid amount"""
    account = BankAccount("Eve", 500)
    with pytest.raises(InvalidAmountError):
        account.withdraw(-50)
    with pytest.raises(InvalidAmountError):
        account.withdraw(0)

def test_transfer():
    """Test transferring money between accounts"""
    account1 = BankAccount("Frank", 1000)
    account2 = BankAccount("Grace", 500)
    
    account1.transfer(300, account2)
    
    assert account1.get_balance() == 700
    assert account2.get_balance() == 800

def test_transfer_insufficient_funds():
    """Test transfer with insufficient funds"""
    account1 = BankAccount("Henry", 100)
    account2 = BankAccount("Ivy", 200)
    
    with pytest.raises(InsufficientFundsError):
        account1.transfer(150, account2)

def test_apply_interest():
    """Test applying interest"""
    account = BankAccount("Jack", 1000)
    new_balance = account.apply_interest(5)  # 5% interest
    assert new_balance == 1050

def test_apply_negative_interest():
    """Test that negative interest raises error"""
    account = BankAccount("Kate", 1000)
    with pytest.raises(InvalidAmountError):
        account.apply_interest(-5)

def test_transaction_history():
    """Test transaction history tracking"""
    account = BankAccount("Leo", 1000)
    account.deposit(500)
    account.withdraw(200)
    
    history = account.get_transaction_history()
    assert len(history) == 2
    assert "Deposited: $500" in history
    assert "Withdrew: $200" in history

def test_account_string_representation():
    """Test string representation of account"""
    account = BankAccount("Maya", 1500)
    assert str(account) == "Account Holder: Maya, Balance: $1500.00"