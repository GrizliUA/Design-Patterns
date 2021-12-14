from abc import ABCMeta, abstractmethod
from dataclasses import dataclass
from iacct import IAcct, AccountProxy,Account

class IDB(metaclass=ABCMeta):
    @abstractmethod
    def login(self, acct_id: str) -> IAcct:
        pass

    @abstractmethod
    def logout(self, acct: IAcct):
        pass

class acctDatabase(IDB):
    def login(self, acct_id: str):
        print("Welcome!")
        return Account(acct_id)

    def logout(self, acct: IAcct):
        print("See you in future,bye.")

@dataclass
class DatabaseProxy(IDB):
    real_database:acctDatabase
    real_acct = None

    def login(self, acct_id: str) -> IAcct:
        self.real_acct = self.real_database.login(acct_id)
        balance = self.real_acct.get_balance()
        return self.make_acct_proxy(balance)

    def logout(self, acct: IAcct):
        self.real_acct.balance = acct.get_balance()
        self.real_database.logout(self.real_acct)

    def make_acct_proxy(self, start_amount: int):
        return AccountProxy(start_amount)