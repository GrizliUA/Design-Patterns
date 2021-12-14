from Inventory import Stock
from dataclasses import dataclass

@dataclass
class ShoppingCart:
    stock:Stock
    total = 0
    items = {}

    def update_amount(self, stock_id, new_amount: float) -> None:
        self.items = {stock_id: new_amount}

    def add_item(self, product_price) -> None:
        self.total += self.stock.amount * product_price

    def checkout(self, cash_paid: float):
        if cash_paid >= self.total:
            return cash_paid - self.total
        return 'Not enough cash'

@dataclass
class Order:
    id:int
    shopping_cart = None

    def create_order(self, stock, product_price):
        self.shopping_cart = ShoppingCart(stock)
        self.shopping_cart.add_item(product_price)

    def edit_order(self, stock_id, amount, shopping_cart: ShoppingCart):
        shopping_cart.update_amount(stock_id, amount)

