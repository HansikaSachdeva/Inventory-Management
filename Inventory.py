#PYTHON MODULE: INVENTORY
import mysql.connector
from mysql.connector import errorcode
from datetime import date
from mysql.connector import (connection)
import os
import streamlit as st
from decouple import config

API_USERNAME = config('USER')
API_PASS = config('PASS')

def clrscreen():
    st.text('\n' * 5)


def searchData():
    try:
        os.system('cls')
        cnx = mysql.connector.connect(user=API_USERNAME, password=API_PASS, host='127.0.0.1', database='Inventory')
        Cursor = cnx.cursor()
        ProductCode = st.number_input("Enter Product Code to be searched from the Inventory : ")
        query = ("SELECT * FROM Inventory where ProductCode = %s")
        rec_srch = (ProductCode,)
        Cursor.execute(query, rec_srch)
        Rec_count = 0
        for (ProductCode, ProductName, PurchaseDate, SalesDate, PurchasePrice, SalesPrice) in Cursor:
            Rec_count += 1
            st.text("=============================================================")
            st.text("1.Product Code : ", ProductCode)
            st.text("2.Product Name : ", ProductName)
            st.text("3.Purchase Date : ", PurchaseDate)
            st.text("4.Sales Date : ", SalesDate)
            st.text("5.Purchase Price : ", PurchaseDate)
            st.text("6.Sales Price : ", SalesPrice)
            st.text("=============================================================")
            if Rec_count%2 == 0:
                st.number_input("Press any key continue")
                clrscreen()
                st.text(Rec_count, "Record(s) found")
        Cursor.close()
        cnx.close()
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            st.text("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            st.text("Database does not exist")
        else:
            st.text(err)
    else:
        cnx.close()