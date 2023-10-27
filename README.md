# cmpsci132
for my cmpsci132 class
.
# Implemented Functionalities:
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
* help: Prints out a large number of strings that help the user use the code if called.
* run_interface: Initializes the user friendly interface
Testing(Pictures will be attached seperately):

Initializing the classes/assigning values to my classes: Nothing went wrong there since my code would not work otherwise

# Testing all the methods in the Inventory/Product Class:

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

## Results:
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

## Note: 
Overall, it went according to plan. All the testing print statements went through, meaning the code went without any hiccups.

# Testing all the methods in the Transaction/Store class:

Create inventory:

inventory = Inventory()

Create a store:

store = Store()
store.inventory = inventory
Start the interface:

store.run_interface()

store.help()

# Results:

Welcome to the Store Management System!
Enter a command (type 'help' for instructions): help

To add a product to out empty store, please type: add_product

To look at one product's information in particular, please type: get_info

To purchase a product, please type: purchase

To pull a report of the items purchased, please type: report

To exit our store, please type: exit
Enter a command (type 'help' for instructions): add_product
Enter product ID: 1
Enter product name: Laptop
Enter product category: Electronics
Enter product price: 999.99
Enter quantity in stock: 10
Successfully added this product!
Enter a command (type 'help' for instructions): get_info
Enter product ID to get information: 1
Product Information: Laptop (Electronics) - 10 in stock
Enter a command (type 'help' for instructions): purchase
Enter product ID to purchase (type 'done' when finished): 1
Enter quantity to purchase: 3
Enter product ID to purchase (type 'done' when finished): done
Product Information: Laptop (Electronics) - 10 in stock
Thank you for your patronage!
Enter a command (type 'help' for instructions): get_info
Enter product ID to get information: 1
Product Information: Laptop (Electronics) - 7 in stock
Enter a command (type 'help' for instructions): report
Current Stock Levels:
Laptop (Electronics): 7 in stock

Sales History:
Transaction ID: 1
  Laptop (Electronics): 3
  Total Amount: $2999.97

Total Revenue: $2999.97
Enter a command (type 'help' for instructions): exit
Thank you for using the Store Management System. Goodbye!

Note: Once again went without a hitch, the results is a lot longer than the previous one due to the help method having so many print statements and the interface also has a lot of print statements.Obviously the interface worked since everything went smoothly and the system responded bacl. You can tell that the get_product_info works from the Inventory class since the number updated correctly. The report looks good as well. The help method is just print statements so it cannot really go wrong. Adding a product and purchasing one also went well since the correct number of items were purchases and accounted for in the report.

## Conclusion:
Overall, I am pretty proud on what I made here. I did run into some trouble when debugging my code, that will all be in the parenthesis below since I ended up fixing this problem. This took a lot of rime, blood, sweat, and energy drinks but I ended up doing a pretty good job if I do say so myself.

(There is one hiccup in this code and it is that the get_product_info method will always print out every products info which is not inherently bad but I created the code thinking I was going to only pull up one of the items infos. Changing it now would require me to change my purchase_products method, which I do not want to do since that was the bulk of the coding.)
