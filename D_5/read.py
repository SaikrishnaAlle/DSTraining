import sqlite3


class readdata:
    def __init__(self):
        self.conn = sqlite3.connect("ecommerce.db")
        self.cur = self.conn.cursor()

    def read_product(self, product_id):
        self.cur.execute(
            "SELECT * FROM Product WHERE ProductID = ?", (product_id,))
        product = self.cur.fetchone()
        if product:
            print(
                f"ProductID: {product[0]},\nName: {product[1]},\nDescription: {product[2]},\nPrice: {product[3]}")
        else:
            print("Product not found")

    def read_customer(self, customer_id):
        self.cur.execute(
            "SELECT * FROM Customer WHERE CustomerID = ?", (customer_id,))
        customer = self.cur.fetchone()
        if customer:
            print(
                f"CustomerID: {customer[0]},\nName: {customer[1]},\nEmail: {customer[2]},\nAddress: {customer[3]}")
        else:
            print("Customer not found")

    def read_order(self, order_id):
        self.cur.execute('''
            SELECT Orders.OrderID, Customer.Name, Product.Name, Orders.Quantity, Orders.TotalCost, Orders.OrderDate
            FROM Orders
            JOIN Customer ON Orders.CustomerID = Customer.CustomerID
            JOIN Product ON Orders.ProductID = Product.ProductID
            WHERE Orders.OrderID = ?
        ''', (order_id,))
        order = self.cur.fetchone()
        if order:
            print(
                f"OrderID: {order[0]},\nCustomer Name: {order[1]},\nProduct Name: {order[2]},\nQuantity: {order[3]},\nTotal Cost: {order[4]},\nOrder Date: {order[5]}")
        else:
            print("Order not found")

    def __del__(self):
        self.conn.close()
