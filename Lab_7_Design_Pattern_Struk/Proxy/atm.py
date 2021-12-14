from idb import DatabaseProxy
from iacct import IAcct
from dataclasses import dataclass



@dataclass
class ATM:
    proxy_database:DatabaseProxy

    def handle_balance_request(self) -> int:
        return self.proxy_database.real_acct.get_balance()

    def handle_login(self, acct_id: str) -> IAcct:
        return self.proxy_database.login(acct_id)

    def handle_logout(self):
        return self.proxy_database.logout(self.proxy_database.real_acct)

    def handle_deposit(self, amount: int) -> bool:
        return self.proxy_database.real_acct.deposit(amount)

    def handle_withdrawal(self, amount: int, customer):
        return customer.withdraw(amount, self.proxy_database)