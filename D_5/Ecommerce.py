from insert import insertdata
from update import updatedata
from delete import deletedata
from read import readdata
from create import create_tables
from dummydata import insert_dummy_data

# Create tables if they don't exist
create_tables()

obj_insert = insertdata()
obj_update = updatedata()
obj_delete = deletedata()
obj_read = readdata()

print("_____________Welcome to Krishna's Super Store__________")
print("For Insertion Press 1, Updation Press 2, Deletion Press 3, Reading Press 4")
print("For Generating Dummy Data Press 5")

num = int(input("Enter your option:"))

if num == 1:
    print("Choose 1 for Product, 2 for Customer, 3 for Order")
    n = int(input("Please enter your option:"))
    if n == 1:
        name = input("Enter product name:")
        description = input("Enter product description:")
        price = float(input("Enter product price:"))
        obj_insert.insert_product(name, description, price)

    elif n == 2:
        name = input("Enter customer name:")
        email = input("Enter customer email:")
        address = input("Enter customer address:")
        obj_insert.insert_customer(name, email, address)

    elif n == 3:
        customer_id = int(input("Enter customer ID:"))
        product_id = int(input("Enter product ID:"))
        quantity = int(input("Enter quantity:"))
        obj_insert.insert_order(customer_id, product_id, quantity)

elif num == 2:
    print("Choose 1 for Product, 2 for Customer, 3 for Order")
    n = int(input("Please enter your option:"))
    if n == 1:
        product_id = int(input("Enter product ID:"))
        name = input("Enter product name:")
        description = input("Enter product description:")
        price = float(input("Enter product price:"))
        obj_update.update_product(product_id, name, description, price)

    elif n == 2:
        customer_id = int(input("Enter customer ID:"))
        name = input("Enter customer name:")
        email = input("Enter customer email:")
        address = input("Enter customer address:")
        obj_update.update_customer(customer_id, name, email, address)

    elif n == 3:
        order_id = int(input("Enter order ID:"))
        customer_id = int(input("Enter customer ID:"))
        product_id = int(input("Enter product ID:"))
        quantity = int(input("Enter quantity:"))
        order_date = input("Enter order date (YYYY-MM-DD):")
        obj_update.update_order(order_id, customer_id,
                                product_id, quantity, order_date)

elif num == 3:
    print("Choose 1 for Product, 2 for Customer, 3 for Order")
    n = int(input("Please enter your option:"))
    if n == 1:
        product_id = int(input("Enter product ID:"))
        obj_delete.delete_product(product_id)
    elif n == 2:
        customer_id = int(input("Enter customer ID:"))
        obj_delete.delete_customer(customer_id)
    elif n == 3:
        order_id = int(input("Enter order ID:"))
        obj_delete.delete_order(order_id)

elif num == 4:
    print("Choose 1 for Product, 2 for Customer, 3 for Order")
    n = int(input("Please enter your option:"))
    if n == 1:
        product_id = int(input("Enter product ID:"))
        obj_read.read_product(product_id)
    elif n == 2:
        customer_id = int(input("Enter customer ID:"))
        obj_read.read_customer(customer_id)
    elif n == 3:
        order_id = int(input("Enter order ID:"))
        obj_read.read_order(order_id)

elif num == 5:
    print("Choose 1 for Customer, 2 for Product, 3 for All")
    n = int(input("Please enter your option:"))
    record_count = int(input("Enter the number of records to insert:"))

    if n == 1:
        insert_dummy_data(record_count, 0)
    elif n == 2:
        insert_dummy_data(0, record_count)
    elif n == 3:
        insert_dummy_data(record_count, record_count)

else:
    print("Invalid option")
