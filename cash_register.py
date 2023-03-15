from customer import Customer
from invoice_item import InvoiceItem
from datetime import datetime
from item import Item


class CashRegister:
    def __init__(self, customer: Customer) -> None:
        self.customer = customer
        self.items: dict[str, InvoiceItem] = {}
        self.purchase_date = datetime.now()
        self._invoice_total: float = 0

    def __str__(self) -> str:
        return f"Customer: {self.customer}, Total Items: {len(self.items)}"
        # because we have str method in class customer and it returns 1st name and last name therefore we just called self.customer

    def _inc_invoice_total(self, item: InvoiceItem) -> None:
        self._invoice_total += item.get_sub_total()

    def _dec_invoice_total(self, item: InvoiceItem) -> None:
        self._invoice_total -= item.get_sub_total()

    def add_item(self, item: Item, qty: int = 1, discount: float = 0) -> None:
        if item.name not in self.items:
            new_item = InvoiceItem(item, qty, discount)
            self.items[item.name] = new_item
            self._inc_invoice_total(new_item)
        else:
            print(f"{item.name} already in cart, update instead?")

    def update_item(self, item: Item, qty: int = 1, discount: float = 0) -> None:
        if item.name in self.items:
            old_item = self.items[item.name]
            self._dec_invoice_total(old_item)

            new_item = InvoiceItem(item, qty, discount)
            self.items[item.name] = new_item
            self._inc_invoice_total(new_item)
        else:
            print(f"{item.name} not in cart, purchase instead?")

    def remmove_item(self, item: Item) -> None:
        if item.name in self.items:
            old_item = self.items[item.name]
            self._dec_invoice_total(old_item)

            del self.items[item.name]

    def get_invoice_total(self) -> float:
        return self._invoice_total

    def display_invoice_total(self) -> None:
        print()
        print(f"+" * 70)
        print(self)
        print(f"Date: {self.purchase_date.strftime('%B %d, %Y')}")
        print(f"-" * 70)
        for item in self.items.values():
            print(item)
        print(f"-" * 70)
        print(f"Total Price: ${self.get_invoice_total():.2f}")
        print(f"+" * 70)
