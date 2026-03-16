import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="expense_tracker",
    autocommit=True
)

cursor = db.cursor(dictionary=True)