# MLOps Lab 1 — Bank Account Management System

A Python-based Bank Account Management System built to demonstrate **MLOps fundamentals** including modular code design, comprehensive testing with both `pytest` and `unittest`, and CI/CD automation via GitHub Actions.

## Project Structure

```
mlops-lab1/
├── .github/workflows/       # GitHub Actions CI/CD pipeline
├── src/
│   └── bank_account.py      # Core bank account module
├── test/
│   ├── test_bank_pytest.py   # Test suite using pytest
│   └── test_bank_unittest.py # Test suite using unittest
├── requirements.txt          # Minimal dependencies (pytest)
├── requirements-full.txt     # Full environment dependencies
└── README.md
```

## Features

- **Account Management** — Create accounts with an initial balance and track the account holder's name.
- **Deposits & Withdrawals** — Perform transactions with built-in validation to prevent invalid or negative amounts.
- **Fund Transfers** — Transfer funds between accounts with automatic balance checks on both sides.
- **Interest Application** — Apply a percentage-based interest rate to the current balance.
- **Transaction History** — Every operation is logged and retrievable via `get_transaction_history()`.
- **Custom Exceptions** — `InsufficientFundsError` and `InvalidAmountError` provide clear, descriptive error handling.

## Getting Started

### Prerequisites

- Python 3.8+

### Installation

```bash
git clone https://github.com/2001malhar/mlops-lab1.git
cd mlops-lab1
pip install -r requirements.txt
```

### Usage

```python
from src.bank_account import BankAccount

# Create accounts
alice = BankAccount("Alice", 1000)
bob = BankAccount("Bob", 500)

# Deposit & withdraw
alice.deposit(250)       # Balance: 1250
alice.withdraw(100)      # Balance: 1150

# Transfer between accounts
alice.transfer(300, bob)  # Alice: 850, Bob: 800

# Apply interest
bob.apply_interest(5)     # 5% interest → Bob: 840

# View history
print(alice.get_transaction_history())
print(alice)              # Account Holder: Alice, Balance: $850.00
```

## Running Tests

The project includes two parallel test suites covering identical scenarios — one in **pytest** and one in **unittest** — to demonstrate both testing frameworks.

```bash
# Run pytest suite
pytest test/test_bank_pytest.py -v

# Run unittest suite
python -m unittest test/test_bank_unittest.py -v
```

### Test Coverage

| Category                | Tests                                                    |
|-------------------------|----------------------------------------------------------|
| Account Creation        | Valid creation, negative initial balance rejection        |
| Deposits                | Valid deposit, zero/negative amount rejection             |
| Withdrawals             | Valid withdrawal, insufficient funds, invalid amounts     |
| Transfers               | Valid transfer, insufficient funds for transfer           |
| Interest                | Valid interest application, negative rate rejection       |
| Transaction History     | Logging accuracy after multiple operations               |
| String Representation   | Correct `__str__` output format                          |

## CI/CD

The repository includes a GitHub Actions workflow (`.github/workflows/`) that automatically runs the test suite on pushes to the `main` branch, ensuring continuous integration.

## Tech Stack

- **Language:** Python 3
- **Testing:** pytest, unittest
- **CI/CD:** GitHub Actions

## License

This project is for educational purposes as part of the MLOps course at Northeastern University.