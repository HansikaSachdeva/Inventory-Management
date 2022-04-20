#PYTHON MODULE: PURCHASES
import mysql.connector
from mysql.connector import errorcode
from datetime import date, datetime, timedelta
from mysql.connector import(connection)
import os
import platform
import streamlit as st
from decouple import config

API_USERNAME = config('USER')
API_PASS = config('PASS')

def clrscreen():
    if platform.system() == "Windows":
        st.text(os.system("cls"))


def insertData():
    try:
        cnx = mysql.connector.connect(user=API_USERNAME, password=API_PASS, host='127.0.0.1', database='Inventory')
        Cursor = cnx.cursor()
        ProductCode = st.number_input("Enter Product Code : ", step = 1)
        ProductName = st.text_input("Enter Product Name : ")
        PurchaseDate = st.date_input("Enter Date of Purchase : ")
        PurchasePrice = st.number_input("Enter Product Price : ", step = 1)
        ProductStock = st.number_input("Enter Quantity purchased : ", step = 1)
        Qry = ("INSERT INTO Purchases VALUES (%s, %s, %s, %s, %s)")
        data = (ProductCode, ProductName, PurchaseDate, PurchasePrice, ProductStock)
        Cursor.execute(Qry,data)
        Qry1 = ("INSERT INTO Inventory(ProductCode,ProductName,PurchaseDate,PurchasePrice) VALUES(%s, %s, %s, %s)")
        data1 = (ProductCode, ProductName, PurchaseDate, PurchasePrice)
        Cursor.execute(Qry1,data1)
        cnx.commit()
        Cursor.close()
        cnx.close()
        st.text("Record Inserted.")
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    cnx.close()


def deleteData():
    try:
        cnx = mysql.connector.connect(user=API_USERNAME, password=API_PASS, host='127.0.0.1', database='Inventory')
        Cursor = cnx.cursor()
        ProductCode = st.number_input("Enter Product Code to be deleted from the Purchases : ", step = 1)
        Qry = ("""DELETE FROM Purchases WHERE ProductCode = %s""")
        del_rec = (ProductCode,)
        Cursor .execute(Qry, del_rec)
        cnx.commit()
        Cursor.close()
        cnx.close()
        st.text(Cursor.rowcount, "Record(s) Deleted Successfully.")
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            st.text("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            st.text("Database does not exist")
        else:
            st.text(err)
    cnx.close()


def searchData():
    try:
        cnx = mysql.connector.connect(user=API_USERNAME, password=API_PASS, host='127.0.0.1', database='Inventory')
        Cursor = cnx.cursor()
        ProductCode = st.number_input("Enter Product Code to be searched from the Purchases : ", step = 1)
        query = ("SELECT * FROM Purchases WHERE ProductCode = %s ")
        rec_srch = (ProductCode,)
        Cursor.execute(query, rec_srch)
        Rec_count = 0
        for(ProductCode, ProductName, PurchaseDate, PurchasePrice, ProductStock) in Cursor:
            Rec_count += 1
            st.text("=============================================================")
            st.text("Product Code : ", ProductCode)
            st.text("Product Name : ", ProductName)
            st.text("Purchased on : ", PurchaseDate)
            st.text("Price of Product : ", PurchasePrice)
            st.text("Product in Stock : ", ProductStock)
            st.text("=============================================================")
            if Rec_count%2 == 0:
                st.number_input("Press any key continue", step = 1)
                clrscreen()
                st.text(Rec_count, "Record(s) found")
        cnx.commit()
        Cursor.close()
        cnx.close()
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
           print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
        cnx.close()


def updateData():
    try:
        cnx = mysql.connector.connect(user=API_USERNAME, password=API_PASS, host='127.0.0.1', database='Inventory')
        Cursor = cnx.cursor()
        ProductCode = st.number_input("Enter Product Code to be updated from the Purchases : ", step = 1)
        query = ("SELECT * FROM Purchases WHERE ProductCode = %s ")
        rec_srch = (ProductCode,)
        st.text("Enter new data")
        ProductName = st.text_input("Enter Product Name : ")
        PurchaseDate = st.date_input("Enter Date of Purchase : ")
        PurchasePrice = st.number_input("Enter Product Price : ", step = 1)
        ProductStock = st.number_input("Enter Quantity purchased : ", step = 1)
        Qry = ("UPDATE Purchases SET ProductName=%s, PurchaseDate=%s, PurchasePrice=%s, ProductStock=%s  WHERE ProductCode=%s")
        data = (ProductName, PurchaseDate, PurchasePrice, ProductStock, ProductCode)
        Cursor.execute(Qry,data)
        cnx.commit()
        Cursor.close()
        cnx.close()
        st.text(Cursor.rowcount, "Record(s) Updated Successfully.")
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    cnx.close()