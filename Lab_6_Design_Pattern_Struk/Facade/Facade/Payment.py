from OrderProcess import ShoppingCart
from dataclasses import dataclass

@dataclass
class Payment:
    card_details = {}

    def add_card_details(self, card_number, money) -> None:
        self.card_details = {'card_number': card_number, 'balance': money}

    def verify_payment(self, shopping_cart: ShoppingCart):
        return shopping_cart.checkout(self.card_details['balance'])