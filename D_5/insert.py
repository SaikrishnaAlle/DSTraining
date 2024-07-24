import sqlite3


class insertdata:
    def __init__(self):
        self.conn = sqlite3.connect("ecommerce.db")
        self.cur = self.conn.cursor()

    def insert_product(self, name, description, price):
        self.cur.execute(
            "INSERT INTO Product (Name, Description, Price) VALUES (?, ?, ?)", (name, description, price))
        self.conn.commit()

    def insert_customer(self, name, email, address):
        self.cur.execute(
            "INSERT INTO Customer (Name, Email, Address) VALUES (?, ?, ?)", (name, email, address))
        self.conn.commit()

    def insert_order(self, customer_id, product_id, quantity):
        self.cur.execute(
            "SELECT Price FROM Product WHERE ProductID = ?", (product_id,))
        product = self.cur.fetchone()
        if product:
            price = product[0]
            total_cost = price * quantity
            self.cur.execute("INSERT INTO Orders (CustomerID, ProductID, Quantity, TotalCost) VALUES (?, ?, ?, ?)",
                             (customer_id, product_id, quantity, total_cost))
            self.conn.commit()
        else:
            print("Product not found")

    def __del__(self):
        self.conn.close()
