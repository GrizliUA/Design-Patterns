from idb import DatabaseProxy, acctDatabase
from atm import ATM
from customer import Customer
from dataclasses import dataclass
import os

if __name__ == '__main__':
    database = acctDatabase()
    proxy_database = DatabaseProxy(database)
    atm = ATM(proxy_database)
    customer = Customer(id=1, name='Morgan Freeman', acct_number='1234-5678')
    os.system('CLS')
    choice = str(input("You want to login?\nYes or No: "))
    if choice.lower() == 'yes':
        os.system('CLS')
        an = str(input('Enter account number: '))
        if an == customer.acct_number:
            atm.handle_login('1')
            proxy_database.real_acct.attach_customer(customer=customer)
            choice_2 = 0
            while choice_2 != 4:
                os.system('CLS')
                print('Menu')
                print("1 - Balance")
                print("2 - Deposit")
                print("3 - Withdraw")
                print("4 - Exit")
                choice_2 = int(input(': '))
                if choice_2 == 1:
                    print(f"\nBalance:\n\t{atm.handle_balance_request()}₴")
                    input('\nPress any button to continue: ')
                elif choice_2 == 2:
                    amount = int(input('\nEnter amount to deposit: '))
                    atm.handle_deposit(amount)
                    print(f'\nYou deposited:\n\t{amount}₴')
                    input('\nPress any button to continue: ')
                elif choice_2 == 3:
                    amount = int(input('\nEnter amount to withdraw: '))
                    if atm.handle_balance_request() > atm.handle_withdrawal(amount,customer):
                        print(f'\nYou withdraw:\n\t{amount}₴')
                        input('\nPress any button to continue: ')
                    else: print(f'\nYou lack {atm.handle_withdrawal(amount,customer)-atm.handle_balance_request()}₴ to do withdrawal')
                    input('\nPress any button to continue: ')
            proxy_database.real_acct.detach_customer(customer)
            atm.handle_logout()
    elif choice.lower == 'no':
        print("Next time,ok?")
