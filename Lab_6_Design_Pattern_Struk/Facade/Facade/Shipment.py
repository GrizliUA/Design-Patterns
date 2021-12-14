from OrderProcess import Order
from Inventory import Stock
from dataclasses import dataclass

@dataclass
class ShipmentProvider:
    id:int
    name:str
    phone_number:str
    providers = []

    def modify_provider(self, id: int, name: str, phone_number: str):
        self.id = id
        self.name = name
        self.phone_number = phone_number
        self.providers = []

    def add_provider(self) -> None:
        print(f"Provider ID: {self.id} added")
        self.providers.append({'id': self.id,
                               'name': self.name,
                               'email': self.phone_number})

@dataclass
class Shipment:
    order:Order
    provider:ShipmentProvider

    def change_provider(self, provider_id: int, product_price: float, stock: Stock) -> None:
        for x in range(len(self.provider.providers)):
            if provider_id == self.provider.id:
                self.order.create_order(stock, product_price)
                print(f"Your order ID: {self.order.id}")

    def add_provider(self, provider_id: int):
        self.provider.add_provider(provider_id)