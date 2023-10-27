class Product:
    #For all the product's details
    def __init__(self, product_id, name, category, price, quantity_in_stock):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.price = price
        self.quantity_in_stock = quantity_in_stock

class Inventory:
    def __init__(self):
        self.products = []
    #Just making this in case I need it
    def isEmpty(self):
        return not bool(self.products)
    #Adding a product
    def add_product(self, product):
        self.products.append(product)
        print("Successfully added this product!")
    #Updating the stock of an item
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
    #Calling from the Inventory class(does the same thing)
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
        print('')
        print("To add a product to out empty store, please type: add_product")
        print('')
        print("To look at one product's information in particular, please type: get_info")
        print('')
        print("To purchase a product, please type: purchase")
        print('')
        print("To pull a report of the items purchased, please type: report")
        print('')
        print("To exit our store, please type: exit")
        
    def run_interface(self):
        print("Welcome to the Store Management System!")
        
        while True:
            command = input("Enter a command (type 'help' for instructions): ").lower()

            if command == 'help':
                self.help()
            elif command == 'add_product':
                product_id = int(input("Enter product ID: "))
                name = input("Enter product name: ")
                category = input("Enter product category: ")
                price = float(input("Enter product price: "))
                quantity = int(input("Enter quantity in stock: "))
                product = Product(product_id, name, category, price, quantity)
                self.add_product(product)
            elif command == 'purchase':
                products_and_quantities = {}
                while True:
                    product_id = input("Enter product ID to purchase (type 'done' when finished): ")
                    if product_id.lower() == 'done':
                        break
                    quantity = int(input("Enter quantity to purchase: "))
                    products_and_quantities[int(product_id)] = quantity
                self.purchase_products(products_and_quantities)
            elif command == 'report':
                self.generate_report()
            elif command == 'get_info':
                product_id = int(input("Enter product ID to get information: "))
                self.inventory.get_product_info(product_id)
            elif command == 'exit':
                print("Thank you for using the Store Management System. Goodbye!")
                break
            else:
                print("Invalid command. Type 'help' for instructions.")
                
#Example usage

# Create inventory 
inventory = Inventory()

# Create a store and set its inventory
store = Store()
store.inventory = inventory
# Start the interface
store.run_interface()


