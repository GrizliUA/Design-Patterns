from dataclasses import dataclass
from abc import ABCMeta, abstractmethod
from cryptography.fernet import Fernet


class ICreditCard(metaclass=ABCMeta):
    @abstractmethod
    def give_details(self,*args) -> dict:
        pass

class CreditCard(ICreditCard):
    def __init__(self,client:str,account_number:str,credit_limit:float,grace_period:int):
        self.client = client
        self.account_number = account_number
        self.credit_limit = credit_limit
        self.grace_period = grace_period
        self._cvv = ''
        self.key = Fernet.generate_key()

    @property
    def cvv(self):
        return self._decrypt(self._cvv)

    @cvv.setter
    def cvv(self, cvv):
        self._cvv = self._encrypt(cvv)
        print(f"encrypted: {self._cvv}")

    def give_details(self, *args) -> dict:
        args = {'Client name' : self.client,
                'Account number' : self.account_number,
                'Credit limit' : self.credit_limit,
                'Grace period' : self.grace_period,
                'CVV' : self.cvv }
        return args

    def _encrypt(self, value: str):
        return Fernet(self.key).encrypt(value.encode())

    def _decrypt(self, value):
        return Fernet(self.key).decrypt(value).decode()

class CreditCardDecorator:
    def __init__(self, decorated_card):
        self.decorated_card = decorated_card

    def add_paypass(self):
        self.decorated_card.paypass = True
        return self.decorated_card

class GoldenCreditCard(CreditCardDecorator):
    def __init__(self, decorated_card):
        super(GoldenCreditCard,self).__init__(decorated_card)

    def add_paypass(self):
        super(GoldenCreditCard,self).add_paypass()
        print('Paypass added')

class CorporateCreditCard(CreditCardDecorator):
    def __init__(self, decorated_card):
        super(CorporateCreditCard,self).__init__(decorated_card)

    def add_paypass(self):
        super(CorporateCreditCard,self).add_paypass()
        print('Paypass added')

class BankInfo:
    def __init__(self,bank_name:str,holder_name:str):
        self.bank_name = bank_name
        self.holder_name = holder_name
        self.accounts_number = ()
        self.credit_history = {'credit_history' : []}

    def credit_history(self, account_number: str):
        for i in range(len(self.accounts_number)):
            if self.accounts_number[i] == account_number:
                self.credit_history['credit_history'].append(self.accounts_number[i])
        return self.credit_history['credit_history']

@dataclass
class PersonalInfo:
    id:int
    name:str
    adress:str
    phone_number:str
    email:str

class BankCustomer:
    def __init__(self,personal_info: PersonalInfo, bank_details: BankInfo):
        self._personal_info = personal_info
        self.bank_details = bank_details

    def give_details(self, *details) -> dict:
        details = {'bank_name' : self.bank_details.bank_name,
                'holder_name' : self.bank_details.holder_name,
                'accounts_number' : self.bank_details.accounts_number,
                'credit_history' : self.bank_details.credit_history}
        return details

class BankCustomerDecorator:
    def __init__(self, decorated_customer):
        self.decorated_customer = decorated_customer

    def add_image(self):
        self.decorated_customer.image = input('\nEnter image URL: ')
        return self.decorated_customer

    def add_company(self):
        self.decorated_customer.company = input('\nEnter company name: ')
        return self.decorated_customer

    def add_vip_status(self):
        self.decorated_customer.status = 'VIP'
        return self.decorated_customer


class IndividualCustomer(BankCustomerDecorator):
    def __init__(self, decorated_customer):
        super(IndividualCustomer,self).__init__(decorated_customer)

    def add_image(self):
        super(IndividualCustomer,self).add_image()
        print('Image added')

class CorporateCustomer(BankCustomerDecorator):
    def __init__(self, decorated_customer):
        super(CorporateCustomer,self).__init__(decorated_customer)

    def add_company(self):
        super(CorporateCustomer,self).add_company()
        print('Company added')
    
class VIPCustomer(BankCustomerDecorator):
    def __init__(self, decorated_customer):
        super(VIPCustomer,self).__init__(decorated_customer)

    def add_vip_status(self):
        super(VIPCustomer,self).add_vip_status()
        print('Vip added')


credit_card = CreditCard(client='Bane', account_number='1', credit_limit=150, grace_period=20)

credit_card.cvv = '123'
print(f'Decrypted: {credit_card.cvv}')
print(credit_card.give_details(credit_card))

premium_card = GoldenCreditCard(credit_card)
premium_card.add_paypass()

cust = PersonalInfo(id = 1,name = 'Jack', adress = 'test street',phone_number='123456',email='test@mail.test')
bank_info = BankInfo('Privat Bank','Maksym Stryk')
bank_customer = BankCustomer(cust,bank_info)

individual_customer = IndividualCustomer(bank_customer)
individual_customer.add_image()
print(individual_customer.decorated_customer.image)

company_customer = IndividualCustomer(bank_customer)
company_customer.add_company()
print(individual_customer.decorated_customer.company)

vip_customer = IndividualCustomer(bank_customer)
vip_customer.add_vip_status()

print()
print(individual_customer.decorated_customer.status)