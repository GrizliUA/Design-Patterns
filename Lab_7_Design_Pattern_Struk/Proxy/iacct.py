from abc import ABCMeta, abstractmethod
from dataclasses import dataclass

class IAcct(metaclass=ABCMeta):
    @abstractmethod
    def get_balance(self) -> int:
        pass

    @abstractmethod
    def withdraw(self, amount: int) -> bool:
        pass

    @abstractmethod
    def attach_customer(self, customer) -> None:
        pass

    @abstractmethod
    def detach_customer(self, customer) -> None:
        pass

    @abstractmethod
    def notify(self) -> None:
        pass

@dataclass
class Account(IAcct):
    acct_id:int
    balance = 0

    def get_balance(self) -> int:
        return self.balance

    def deposit(self, amount: int) -> bool:
        if amount > 0:
            self.balance += amount
            return True
        else: return False

    def withdraw(self, amount: int) -> bool:
        if amount <= self.balance:
            self.balance -= amount
            return True
        else: return amount

    def attach_customer(self, customer) -> None:
        print(f"\nIAcct: Connected")
    
    def detach_customer(self, customer) -> None:
        print(f"\nIAcct: Disconected")

    def notify(self) -> None:
        print("IAcct: Attention")


@dataclass
class AccountProxy(IAcct):
    def __init__(self, balance: int):
        self.balance = balance
        self.customers = []
        self.acct = Account(self)

    def get_balance(self) -> int:
        self.notify()
        return self.acct.get_balance()

    def deposit(self, amount: int) -> bool:
        return self.acct.deposit(amount)

    def withdraw(self, amount: int) -> bool:
        return self.acct.withdraw(amount)

    def attach_customer(self, customer) -> None:
        self.acct.attach_customer(customer)
        self.customers.append(customer)

    def detach_customer(self, customer) -> None:
        self.acct.detach_customer(customer)
        self.customers.remove(customer)

    def notify(self) -> None:
        self.acct.notify()
        for customer in self.customers:
            customer.notify(self)