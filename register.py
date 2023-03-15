from cash_register import CashRegister
from customer import Customer
from item import Item

milk = Item(100, "Milk", 4.5, "Litre")
egg = Item(101, "Eggs", 4.99, "Piece")
rice = Item(102, "Rice", 3.50, "Kg")
apple = Item(103, "Apples", 2.99, "Kg")

customer1= Customer("Shameer", "Khan")

cr1= CashRegister(customer1)

cr1.add_item(milk)
cr1.add_item(egg, 24, 2.50)
cr1.add_item(rice, 2)
cr1.add_item(apple, 12, 2.00)
cr1.update_item(egg, 6)
cr1.remmove_item(milk)

cr1.display_invoice_total()