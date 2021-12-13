from dataclasses import dataclass
from abc import ABC, abstractmethod

@dataclass
class Checking:
    id:int
    cid:int

@dataclass
class Savings:
    id:int
    cid:int

@dataclass
class Account:
    id:int
    customer_id:int
    savings:int = 0

@dataclass
class Loan:
    id:int
    type:str
    account_id:int
    customer_id:int

@dataclass
class Bank:
    id:int
    name:str
    location:str
    tellers = []
    customers = []

class ICustomer(ABC):
    @abstractmethod
    def copy(self):
        pass
    @abstractmethod
    def deepcopy(self):
        pass


@dataclass
class Customer(ICustomer):
    id:int
    name:str
    adress:str
    phone_number:int
    acct_number:int
    bank:Bank
    accounts = []
    loans = []
    
    def GeneralInquiry():
        pass

    def DepositMoney(self,account_id:int,amount:int):
        for x in range(len(self.accounts)):
            if self.accounts[x].id == account_id:
                self.accounts[x].savings += amount
                print(f'\n{amount}₴ was deposited to your account')

    def WithdrawMoney(self,account_id:int,amount:int):
        for x in range(len(self.accounts)):
            if self.accounts[x].id == account_id:
                if self.accounts[x].savings >= amount:
                    self.accounts[x].savings -= amount
                    print(f'\n{amount}₴ was withdrawed from you account')
                else:
                    print(f'\nYou dont have {self.accounts[x].savings - amount}₴ more to withdraw them')

    def OpenAccount(self,account_id: int):
        self.accounts.append(Account(account_id,self.id))
        print(f"\nAn account with id={account_id} opened successfully")

    def CloseAccount(self,account_id: int):
        self.accounts.remove(Account(account_id,self.id))
        print(f"\nAn account with id={account_id} closed successfully")

    def ApplyForLoan(self, teller, loan_id: int, loan_type: str, account_id: int):
        teller.loanRequest(self, loan_id, loan_type, account_id)

    def RequestCard():
        pass

    def copy(self):
        return type(self)(
            self.id,
            self.name,
            self.adress,
            self.phone_number,
            self.acct_number,
            self.bank
        )

    def deepcopy(self):
        return type(self)(
            self.id,
            self.name,
            self.adress,
            self.phone_number,
            self.acct_number,
            self.bank
        )



@dataclass
class Teller:
    id:int
    name:str
    bank:Bank

    def CollectMoney(self, customer: Customer):
        amount = 0
        for x in range(len(customer.accounts)):
            amount += customer.accounts[x].savings
        choose = input(f'\nThere are {amount}₴ on all your accounts, are you sure to withdraw all money from all accounts?\nYes or No?\nYour choice: ')
        if choose.lower() == 'yes':
            for x in range(len(customer.accounts)):
                amount = 0
                amount += customer.accounts[x].savings
                customer.accounts[x].savings = 0
                print(f"\nA {amount}₴ was withdrawed successfully from account with ID: {customer.accounts[x].id}")
        else:
            print('\nOperation was canceled')

    def OpenAccount(self, customer: Customer, account_id: int):
        if account_id not in customer.accounts:
            customer.accounts.append(Account(account_id,customer.id))
            print(f"\nAn account with id={account_id} opened successfully")
        else:
            print('\nNo account with such ID')

    def CloseAccount(self, customer: Customer, account_id: int):
        for x in range(len(customer.accounts)):
            if customer.accounts[x].id == account_id:
                customer.accounts.pop(x)
                print(f"\nAn account with id={account_id} closed successfully")
                break
            else:
                print('\nNo account with such ID')

    def LoanRequest(self, customer: Customer, loan_id: int, loan_type: str, account_id: int):
        self.openAccount(customer, account_id)
        if loan_id not in customer.loans:
            customer.loans[loan_id] = Loan(loan_id, loan_type, account_id, customer.id)

    def ProvideInfo(self,customer):
        for x in range(len(customer.accounts)):
            print(f'\nAccount №{customer.accounts[x].id}'
                  f'\nCustomer id: {customer.accounts[x].customer_id}'
                  f'\nCustomer name: {customer.name}'
                  f'\nSaving: {customer.accounts[x].savings}₴')

    def IssueCard():
        pass





bank = Bank(1,'Privat','Ternopil')
new = Customer(5,'John','Baker street 3',8,0,bank)
#print(new)
new2 = new.copy()
new2.id = 6
new2.acct_number = 7
#print(new2)
new3 = new2.deepcopy()
new3.name = 'Martin'
new3.adress = 'Burger square'
new3.phone_number = 10
#print(new3)
#print('\n\n')
tanya = Teller(1,'Tanya','Privat Bank')
new3.OpenAccount(7)
#print(new3.accounts)

#new3.CloseAccount(7)
#print(new3.accounts)

tanya.OpenAccount(new3,15)
#print(new3.accounts)

#tanya.CloseAccount(new3,7)
#print(new3.accounts)


new3.DepositMoney(15,3000)
new3.DepositMoney(7,5000)
#tanya.ProvideInfo(new3)

new3.WithdrawMoney(15,1000)
#tanya.ProvideInfo(new3)

new3.WithdrawMoney(15,2500)
tanya.ProvideInfo(new3)

tanya.CollectMoney(new3)
tanya.ProvideInfo(new3)