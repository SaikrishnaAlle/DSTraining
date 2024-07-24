import sqlite3
from faker import Faker
import random
from datetime import datetime, timedelta


def insert_dummy_data(customer_count, product_count):
    conn = sqlite3.connect("ecommerce.db")
    cur = conn.cursor()
    faker = Faker()

    customer_ids = []
    product_ids = []

    for _ in range(customer_count):
        name = faker.name()
        email = faker.email()
        address = faker.address()
        cur.execute(
            "INSERT INTO Customer (Name, Email, Address) VALUES (?, ?, ?)", (name, email, address))
        customer_ids.append(cur.lastrowid)

    conn.commit()

    for _ in range(product_count):
        name = faker.word().capitalize()
        description = faker.text(max_nb_chars=100)
        price = round(faker.random_number(digits=5) /
                      100, 2)
        cur.execute("INSERT INTO Product (Name, Description, Price) VALUES (?, ?, ?)",
                    (name, description, price))
        product_ids.append(cur.lastrowid)

    conn.commit()

    if customer_ids and product_ids:
        for _ in range(customer_count):
            customer_id = random.choice(customer_ids)
            product_id = random.choice(product_ids)
            quantity = random.randint(1, 5)
            order_date = datetime.now() - timedelta(days=random.randint(0, 30)
                                                    )
            cur.execute(
                "SELECT Price FROM Product WHERE ProductID = ?", (product_id,))
            product_price = cur.fetchone()[0]
            total_cost = round(quantity * product_price, 2)
            cur.execute(
                "INSERT INTO Orders (CustomerID, ProductID, Quantity, OrderDate, TotalCost) VALUES (?, ?, ?, ?, ?)",
                (customer_id, product_id, quantity,
                 order_date.strftime('%Y-%m-%d %H:%M:%S'), total_cost)
            )

    conn.commit()
    conn.close()
    print("Dummy data inserted successfully!")


if __name__ == "__main__":
    customer_count = int(input("Enter the number of customers to insert: "))
    product_count = int(input("Enter the number of products to insert: "))
    insert_dummy_data(customer_count, product_count)
