"""Carrito de la compra. Los precios son floats en euros."""


class Cart:
    def __init__(self):
        self.items = []

    def add(self, name, price, quantity=1):
        self.items.append({"name": name, "price": price, "quantity": quantity})

    def total(self):
        return sum(item["price"] for item in self.items)
