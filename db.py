import mysql.connector
import os

db = mysql.connector.connect(
    host=os.getenv("MYSQLHOST"),
    user=os.getenv("MYSQLUSER"),
    password=os.getenv("MYSQLPASSWORD"),
    database=os.getenv("MYSQL_DATABASE"),
    port=os.getenv("MYSQLPORT"),
    autocommit=True
)

cursor = db.cursor(dictionary=True)