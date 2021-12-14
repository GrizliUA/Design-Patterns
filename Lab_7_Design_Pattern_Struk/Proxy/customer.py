from idb import DatabaseProxy
from iacct import AccountProxy
from dataclasses import dataclass


@dataclass
class Customer:
    id:int
    name:str
    acct_number:str

    def notify(self, acct_proxy: AccountProxy):
        acct_proxy.notify()
        print(f"\nCustomer\n\tID: {self.id}\n\tName: {self.name}\n\tacct Number: {self.acct_number}]")

    def withdraw(self, amount: int, proxy_database: DatabaseProxy):
        return proxy_database.real_acct.withdraw(amount)