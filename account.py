from __future__ import annotations
from typing import Dict, List


class Account:

    account_number: int
    owner: Owner
    balance: float
    accounts: Dict[int, Account] = {}
    transactions: Dict[int, Transaction] = {}

    def __init__(self, account_number: int, owner: Owner) -> None:
        self.account_number = account_number
        self.owner = owner
        self.balance = 0.0
        Account.accounts[account_number] = self

    def get_balance(self) -> float:
        return self.balance

    def deposit(self, amount: float) -> float:
        self.balance += amount
        transaction = Transaction("deposit", amount)
        self.transactions[len(self.transactions) + 1] = transaction
        return self.balance

    def withdraw(self, amount: float) -> float:
        self.balance -= amount
        transaction = Transaction("withdraw", amount)
        self.transactions[len(self.transactions) + 1] = transaction
        return self.balance

    def transfer(self, amount: float, other: Account) -> None:
        self.balance -= amount
        other.balance += amount
        transaction = Transaction("transfer", amount, other)
        self.transactions[len(self.transactions) + 1] = transaction

    @staticmethod
    def get_accounts() -> List[Account]:
        return list(Account.accounts.values())

    # @staticmethod
    # def get_accounts() -> List[Account]:
    #     account_list = []
    #     for account in Account.accounts.values():
    #         account_list.append(account)
    #     return account_list

    @staticmethod
    def get_account(account_id: int) -> Account:
        return Account.accounts.get(account_id)

    def get_transactions(self) -> List[Transaction]:
        return list(self.transactions.values())


class Owner:

    id_number: int
    name: str
    owners: Dict[int, Owner] = {}

    def __init__(self, id_number: int, name: str) -> None:
        self.id_number = id_number
        self.name = name
        Owner.owners[id_number] = self


class Transaction:

    transaction_type: str
    amount: float
    receiver: Account | None = None

    def __init__(self, transaction_type: str, amount: float, receiver: Account = None) -> None:
        self.transaction_type = transaction_type
        self.amount = amount
        if receiver:
            self.receiver = receiver

    def __repr__(self):
        return f"[{self.transaction_type}, {self.amount}{f', {self.receiver}' if self.receiver else ''}]"
