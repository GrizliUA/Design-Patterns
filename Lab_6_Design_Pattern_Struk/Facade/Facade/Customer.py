from Payment import Payment
from OrderFacade import OrderFacade
from Inventory import Stock , Product
from Shipment import ShipmentProvider
from OrderProcess import  ShoppingCart
from dataclasses import dataclass

@dataclass
class Customer:
    payment:Payment

    def order_item(self, order_id, provider_id, product_price, order_facade: OrderFacade) -> None:
        print('\nEnter card number or 0 to exit')
        while True:
            card_number = str(input('\n- '))
            if card_number == self.payment.card_details['card_number']: break
            elif card_number == '0': return
        if self.payment.verify_payment(order_facade.shopping_cart) >= product_price:
            order_facade.do_operation(order_id, provider_id, product_price)
            print(f"\nBalance: {self.payment.card_details['balance']}₴")
            self.payment.card_details['balance'] -= product_price
            print(f"\n-{product_price}₴\nBalance: {self.payment.card_details['balance']}₴")
        else: print(f"\nYou should pay {product_price}₴, you lack {product_price-self.payment.card_details['balance']}₴")







# The client code
product1 = Product(1, 20, 'Bread')
product2 = Product(2, 35, 'Chips')

stock = Stock(1)
stock.update_stock(product1,40)
stock.select_stock_item(product1)
stock.update_stock(product2,15)
stock.select_stock_item(product2)

shopping_cart = ShoppingCart(stock)

shipment_provider = ShipmentProvider(1,'Morgan Freeman','097-96-2343-3')
shipment_provider.add_provider()
order_facade = OrderFacade(stock, shipment_provider, shopping_cart)

payment = Payment()
payment.add_card_details('1234-5678-8765-4321', 150.0)
print(payment.card_details)

customer = Customer(payment)

customer.order_item(1,
                    shipment_provider.id,
                    product_price=product1.price+product2.price,
                    order_facade=order_facade)