"""CREATING DATABASES AND ALL THE REQUIRED TABLES NEEDED TO RUN THE PROJECT
DATABASE NAME: Inventory
TABLES: Purchases, Sales, and Inventory"""

import mysql.connector
from decouple import config

API_USERNAME = config('USER')
API_PASS = config('PASS')

def DatabaseCreate():
    cnx = mysql.connector.connect(user=API_USERNAME, password=API_PASS, host='127.0.0.1')
    Cursor = cnx.cursor()
    Cursor.execute("CREATE DATABASE IF NOT EXISTS Inventory")
    Cursor.execute("")
    Cursor.close()
    cnx.close()


def TablesCreate():
    cnx = mysql.connector.connect(user=API_USERNAME, password=API_PASS, host='127.0.0.1', database='Inventory')
    Cursor = cnx.cursor()
    Cursor.execute("CREATE TABLE IF NOT EXISTS Purchases(ProductCode int(2) Primary Key, ProductName varchar(20), PurchaseDate Date, PurchasePrice int(3), ProductStock int(2))")
    Cursor.execute("CREATE TABLE IF NOT EXISTS Sales(ProductCode int(2) Primary Key, ProductName varchar(20), SalesDate Date, SalesPrice int(3))")
    Cursor.execute("CREATE TABLE IF NOT EXISTS Inventory(ProductCode int(2) Primary Key, ProductName varchar(20), PurchaseDate Date, SalesDate Date, PurchasePrice int(3), SalesPrice int(3))")
    Cursor.close()
    cnx.close()