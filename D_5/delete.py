import sqlite3


class deletedata:
    def __init__(self):
        self.conn = sqlite3.connect("ecommerce.db")
        self.cur = self.conn.cursor()

    def delete_product(self, product_id):
        self.cur.execute(
            "DELETE FROM Product WHERE ProductID = ?", (product_id,))
        self.conn.commit()
        print("Product deleted successfully")

    def delete_customer(self, customer_id):
        self.cur.execute(
            "DELETE FROM Customer WHERE CustomerID = ?", (customer_id,))
        self.conn.commit()
        print("Customer deleted successfully")

    def delete_order(self, order_id):
        self.cur.execute("DELETE FROM Orders WHERE OrderID = ?", (order_id,))
        self.conn.commit()
        print("Order deleted successfully")

    def __del__(self):
        self.conn.close()
