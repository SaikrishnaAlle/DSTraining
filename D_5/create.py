import sqlite3


def create_tables():
    conn = sqlite3.connect("ecommerce.db")
    cur = conn.cursor()

    cur.execute('''
        CREATE TABLE IF NOT EXISTS Customer(
            CustomerID INTEGER PRIMARY KEY AUTOINCREMENT,
            Name TEXT,
            Email TEXT,
            Address TEXT
        )
    ''')
    conn.commit()

    cur.execute('''
        CREATE TABLE IF NOT EXISTS Product(
            ProductID INTEGER PRIMARY KEY AUTOINCREMENT,
            Name TEXT,
            Description TEXT,
            Price REAL
        )
    ''')
    conn.commit()

    cur.execute('''
        CREATE TABLE IF NOT EXISTS Orders(
            OrderID INTEGER PRIMARY KEY AUTOINCREMENT,
            CustomerID INTEGER,
            ProductID INTEGER,
            Quantity INTEGER,
            OrderDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            TotalCost REAL,
            FOREIGN KEY (CustomerID) REFERENCES Customer(CustomerID),
            FOREIGN KEY (ProductID) REFERENCES Product(ProductID)
        )
    ''')
    conn.commit()

    conn.close()
