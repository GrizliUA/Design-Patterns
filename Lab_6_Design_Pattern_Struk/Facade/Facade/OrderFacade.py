from Inventory import Stock
from Shipment import ShipmentProvider , Shipment
from OrderProcess import Order , ShoppingCart
from dataclasses import dataclass

@dataclass
class OrderFacade:
    stock:Stock
    shipment_provider:ShipmentProvider
    shopping_cart:ShoppingCart

    def do_operation(self, order_id, provider_id, product_price) -> None:
        order = Order(order_id)
        shipment = Shipment(order, self.shipment_provider)
        order.create_order(self.stock, product_price)
        shipment.change_provider(provider_id, self.shopping_cart.total, self.stock)
        print(f"You should pay {product_price}₴")