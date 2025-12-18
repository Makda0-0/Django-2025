import json
from abc import ABC, abstractmethod

class Account(ABC):
    @abstractmethod
    def get_account_type(self):
        pass

class SavingsAccount(Account):
    def get_account_type(self):
        return "Savings Account"

class CurrentAccount(Account):
    def get_account_type(self):
        return "Current Account"

json_data = '''
[
    {"type": "savings", "account_number": "ACC001"},
    {"type": "current", "account_number": "ACC002"},
    {"type": "savings", "account_number": "ACC003"}
]
'''


def create_accounts_from_json(json_string):#Create accounts from JSON
    """Create account objects based on JSON data"""
    data = json.loads(json_string)
    accounts = []
    
    for item in data:
        account_type = item["type"]
        
        if account_type == "savings":
            accounts.append(SavingsAccount())
        elif account_type == "current":
            accounts.append(CurrentAccount())
    
    return accounts

print("=== Creating Accounts from JSON ===")

accounts = create_accounts_from_json(json_data)

print(f"Created {len(accounts)} accounts from JSON")

print("\n Demonstrating Polymorphism ")

for i, account in enumerate(accounts):
    result = account.get_account_type()  # Polymorphism 
    print(f"Account {i+1}: {result}")