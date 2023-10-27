class Product:
    def __init__(self, product_id, name, category, price, quantity_in_stock):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.price = price
        self.quantity_in_stock = quantity_in_stock

class Inventory:
    def __init__(self):
        self.products = []

    def isEmpty(self):
        return not bool(self.products)
    
    def add_product(self, product):
        self.products.append(product)
        print("Successfully added this product!")

    #Using this to update the stock, will make a new class so the interface is will only use one or two classes
    def update_stock(self, product_id, new_quantity):
        for product in self.products:
            if product.product_id == product_id:
                product.quantity_in_stock = new_quantity
                return True
        return False
    
    def get_product_info(self, product_id):
        for product in self.products:
            if product.product_id == product_id:
                print(f"Product Information: {product.name} ({product.category}) - {product.quantity_in_stock} in stock")
                return product

class Transaction:
    def __init__(self, transaction_id, products, total_amount):
        self.transaction_id = transaction_id
        self.products = products
        self.total_amount = total_amount

class Store:
    def __init__(self):
        self.inventory = Inventory()
        self.transactions = []

    def add_product(self, product):
        self.inventory.add_product(product)

    #To purchase something in the inventory
    def purchase_products(self, products_and_quantities):
        purchased_products = []
        total_amount = 0
    
        for product_id, quantity in products_and_quantities.items():
            product = self.inventory.get_product_info(product_id)
            if product and product.quantity_in_stock >= quantity:
                purchased_products.append(Product(product.product_id, product.name, product.category, product.price, quantity))
                total_amount += product.price * quantity
                self.inventory.update_stock(product_id, product.quantity_in_stock - quantity)

        transaction_id = len(self.transactions) + 1
        transaction = Transaction(transaction_id, purchased_products, total_amount)
        self.transactions.append(transaction)
        print("Thank you for your patronage!")
        
    def generate_report(self):
        # Current stock levels report
        print("Current Stock Levels:")
        for product in self.inventory.products:
            print(f"{product.name} ({product.category}): {product.quantity_in_stock} in stock")

        # Sales history report
        print("\nSales History:")
        for transaction in self.transactions:
            print(f"Transaction ID: {transaction.transaction_id}")
            for product in transaction.products:
                print(f"  {product.name} ({product.category}): {product.quantity_in_stock}")
            print(f"  Total Amount: ${transaction.total_amount:.2f}\n")

        # Total revenue report
        total_revenue = sum(transaction.total_amount for transaction in self.transactions)
        print(f"Total Revenue: ${total_revenue:.2f}")
        pass

    def help(self):
        print("Use the following commands in the console to use our store correctly:")
        print('')
        print("To suggest a product you want, type a name for the product and set it equal")
        print("to (An ID number you want with this product, the name of this product, the")
        print("type/category this product belongs to, the price, and the quantity you would like to stock.")
        print("Then using the product you assinged previously type inventory.add_product(THE NAME OF THE PRODUCT ASSIGNED) and press enter!")
        print("Note, please use a quotations mark around any words.")
        print("Example usage: product1 = Product(1, Laptop, Electronics, 999.99, 10)")
        print('')
        print("To make a purchase, type store.purchase_products(THE ID #: QUANTITY).")
        print('')
        print("To generate a report, type store.generate_report().")

# Create inventory and add products
inventory = Inventory()
# Create a store and set its inventory
store = Store()
store.inventory = inventory

print("Welcome what would you like to purchase?")
print("If you need help please type store.help()")


