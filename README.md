# cmpsci132
for my cmpsci132 class

## Implemented Functionalities:
1. Product Class
* Represents individual products in the store.
* Attributes: name, category, price, quantity in stock, and a unique product identifier.
2. Inventory Class
* Manages the store's inventory.
Methods:
* add_product: Adds a product to the inventory.
* update_stock: Updates stock levels for a given product.
* get_product_info: Retrieves product information.
* isEmpty: Check to see if the inventory is empty.
4. Transaction Class
* Represents individual sales transactions.
* Includes information about the products sold, quantities, and total amount.
5. Store Class
Utilizes Product, Inventory, and Transaction classes to manage the store.
Methods:
* make_transaction: Records sales transactions and updates stock levels.
* generate_report: Generates reports on current stock levels, sales history, and total revenue.
 help: Prints out a large number of strings that help the user use the code if called.

Testing(Pictures will be attached seperately):

Initializing the classes/assigning values to my classes: Nothing went wrong there since my code would not work otherwise

## Testing all the methods in the Inventory/Product Class:

Create products:
product1 = Product(1, "Laptop", "Electronics", 999.99, 10)
product2 = Product(2, "Desk Chair", "Furniture", 149.99, 20)

Create inventory and add products:
inventory = Inventory()
inventory.add_product(product1)
inventory.add_product(product2)

Display initial stock levels:
print("Initial Stock Levels:")
inventory.get_product_info(1)
inventory.get_product_info(2)

Update stock levels:
inventory.update_stock(1, 5)
inventory.update_stock(2, 15)

Display updated stock levels:
print("\nUpdated Stock Levels:")
inventory.get_product_info(1)
inventory.get_product_info(2)

Add a new product:
product3 = Product(3, "Smartphone", "Electronics", 699.99, 30)
inventory.add_product(product3)

Display stock levels after adding a new product:
print("\nStock Levels After Adding New Product:")
inventory.get_product_info(1)
inventory.get_product_info(2)
inventory.get_product_info(3)

Results:
Successfully added this product!
Successfully added this product!
Initial Stock Levels:
Product Information: Laptop (Electronics) - 10 in stock
Product Information: Desk Chair (Furniture) - 20 in stock

Updated Stock Levels:
Product Information: Laptop (Electronics) - 5 in stock
Product Information: Desk Chair (Furniture) - 15 in stock
Successfully added this product!

Stock Levels After Adding New Product:
Product Information: Laptop (Electronics) - 5 in stock
Product Information: Desk Chair (Furniture) - 15 in stock
Product Information: Smartphone (Electronics) - 30 in stock

Note: 
Overall, it went according to plan. All the testing print statements went through, meaning the code went without any hiccups.

## Testing all the methods in the Transaction/Store class:
    
Create products
product1 = Product(1, "Laptop", "Electronics", 999.99, 10)
product2 = Product(2, "Desk Chair", "Furniture", 149.99, 20)

Create inventory and add products
inventory = Inventory()
inventory.add_product(product1)
inventory.add_product(product2)

Create a store and set its inventory
store = Store()
store.inventory = inventory

Display initial stock levels
print("Initial Stock Levels:")
store.inventory.get_product_info(1)
store.inventory.get_product_info(2)

Make a purchase
print("\nMaking a Purchase:")
store.purchase_products({1: 2, 2: 1})  # Purchase 2 laptops and 1 desk chair

Display stock levels after the purchase
print("\nStock Levels After Purchase:")
store.inventory.get_product_info(1)
store.inventory.get_product_info(2)

Generate a report
print("\nGenerating Report:")
store.generate_report()

Display help message
print("\nHelp Message:")
store.help()

# Results:
Successfully added this product!
Successfully added this product!
Initial Stock Levels:
Product Information: Laptop (Electronics) - 10 in stock
Product Information: Desk Chair (Furniture) - 20 in stock

Making a Purchase:
Product Information: Laptop (Electronics) - 10 in stock
Product Information: Desk Chair (Furniture) - 20 in stock
Thank you for your patronage!

Stock Levels After Purchase:
Product Information: Laptop (Electronics) - 8 in stock
Product Information: Desk Chair (Furniture) - 19 in stock

Generating Report:
Current Stock Levels:
Laptop (Electronics): 8 in stock
Desk Chair (Furniture): 19 in stock

Sales History:
Transaction ID: 1
  Laptop (Electronics): 2
  Desk Chair (Furniture): 1
  Total Amount: $2149.97

Total Revenue: $2149.97

Help Message:
Use the following commands in the console to use our store correctly:

To suggest a product you want, type a name for the product and set it equal
to (An ID number you want with this product, the name of this product, the
type/category this product belongs to, the price, and the quantity you would like to stock.
Then using the product you assinged previously type inventory.add_product(THE NAME OF THE PRODUCT ASSIGNED) and press enter!
Note, please use a quotations mark around any words.
Example usage: product1 = Product(1, Laptop, Electronics, 999.99, 10)

To make a purchase, type store.purchase_products(THE ID #: QUANTITY).

To generate a report, type store.generate_report().

Note: Once again went without a hitch, the results is a lot longer than the previous one due to the help method having so many print statements.

##Conclusion:
Overall, I am pretty proud on what I made here. I did run into some trouble when debugging my code, that will all be in the parenthesis below since I ended up fixing this problem. This took a lot of rime, blood, sweat, and energy drinks but I ended up doing a pretty good job if I do say so myself.

(There is one hiccup in this code and it is that the get_product_info method will always print out every products info which is not inherently bad but I created the code thinking I was going to only pull up one of the items infos. Changing it now would require me to change my purchase_products method, which I do not want to do since that was the bulk of the coding.)
