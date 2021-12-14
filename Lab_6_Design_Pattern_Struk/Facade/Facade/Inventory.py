from dataclasses import dataclass

@dataclass
class Product:
    id:int
    price:float
    type:str

    def add_product(self, id: int, price: float, type: str) -> None:
        self.id = id
        self.price = price
        self.type = type
        print(f"\nProduct ID: {self.id} added\n")

    def update_product(self):
        return f"\nProduct:\n\tID: {self.id}\n\tType: {self.type}\n\tPrice: {self.price}\n"

@dataclass
class Stock:
    id:int
    amount = 0
    products = []

    def select_stock_item(self, product) -> None:
        for i in range(len(self.products)):
            if product.id == self.products[i]['id']:
                print(f"\nStock\n\tID: {self.id}\n\tAmount: {self.amount}\n\t{product.update_product()}")

    def update_stock(self, product: Product, amount: int):
        self.amount = amount
        product.add_product(product.id, product.price, product.type)
        self.products.append({"id": product.id, "price": product.price, "type:": product.type})