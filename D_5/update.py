import sqlite3


class updatedata:
    def __init__(self):
        self.conn = sqlite3.connect("ecommerce.db")
        self.cur = self.conn.cursor()

    def update_product(self, product_id, name, description, price):
        self.cur.execute(
            "UPDATE Product SET Name = ?, Description = ?, Price = ? WHERE ProductID = ?",
            (name, description, price, product_id)
        )
        self.conn.commit()
        print("Product updated successfully")

    def update_customer(self, customer_id, name, email, address):
        self.cur.execute(
            "UPDATE Customer SET Name = ?, Email = ?, Address = ? WHERE CustomerID = ?",
            (name, email, address, customer_id)
        )
        self.conn.commit()
        print("Customer updated successfully")

    def update_order(self, order_id, customer_id, product_id, quantity, order_date):
        self.cur.execute(
            "UPDATE Orders SET CustomerID = ?, ProductID = ?, Quantity = ?, OrderDate = ? WHERE OrderID = ?",
            (customer_id, product_id, quantity, order_date, order_id)
        )
        self.conn.commit()
        print("Order updated successfully")

    def __del__(self):
        self.conn.close()
