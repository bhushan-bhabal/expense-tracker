import mysql.connector
import os

db = mysql.connector.connect(
    host=os.getenv("MYSQLHOST"),
    user=os.getenv("MYSQLUSER"),
    password=os.getenv("MYSQLPASSWORD"),
    database=os.getenv("MYSQL_DATABASE"),
    port=int(os.getenv("MYSQLPORT")),
    autocommit=True
)

cursor = db.cursor()

# CREATE TABLES AUTOMATICALLY
cursor.execute("""
CREATE TABLE IF NOT EXISTS categories (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS expenses (
    id INT AUTO_INCREMENT PRIMARY KEY,
    category_id INT NOT NULL,
    amount DECIMAL(10,2) NOT NULL,
    description VARCHAR(255),
    expense_date DATE NOT NULL,
    FOREIGN KEY (category_id) REFERENCES categories(id)
)
""")

# INSERT DEFAULT CATEGORIES (only if empty)
cursor.execute("SELECT COUNT(*) FROM categories")
count = cursor.fetchone()[0]

if count == 0:
    cursor.executemany("""
    INSERT INTO categories (name) VALUES (%s)
    """, [
        ("Food",),
        ("Transport",),
        ("Shopping",),
        ("Bills",),
        ("Entertainment",)
    ])

# dictionary cursor for rest of app
cursor = db.cursor(dictionary=True)