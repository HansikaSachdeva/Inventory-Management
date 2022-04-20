#PYTHON MODULE: SALES
import mysql.connector
from mysql.connector import errorcode
from datetime import date, datetime, timedelta
from mysql.connector import(connection)
import os
import streamlit as st
from decouple import config

API_USERNAME = config('USER')
API_PASS = config('PASS')


def clrscreen():
    st.text('\n' * 5)


def insertData():
    try:
        cnx = mysql.connector.connect(user=API_USERNAME, password=API_PASS, host='127.0.0.1', database='Inventory')
        Cursor = cnx.cursor()
        ProductCode = st.number_input("Enter Product Code : ")
        ProductName = st.text_input("Enter Product Name : ")
        SalesDate = st.date_input("Enter Date of Sale : ")
        SalesPrice = st.number_input("Enter Sales Price : ")
        st.button("Click me for no reason")
 
        # Create a button, that when clicked, shows a text
        if(st.button("About")):
            Qry = ("INSERT INTO Sales VALUES(%s, %s, %s, %s)")
            data = (ProductCode, ProductName, SalesDate, SalesPrice)
            Cursor.execute(Qry, data)
            #Qry1 = ("INSERT INTO Inventory(SalesDate,SalesPrice) SELECT SalesDate, SalesPrice FROM Sales WHERE ProductCode")
            #data1 = (ProductCode)
            #Cursor.execute(Qry1,data1)
            cnx.commit()
        Cursor.close()
        cnx.close()
        st.text("Record Inserted.")
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            st.text("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            st.text("Database does not exist")
        else:
            st.text(err)
        cnx.close()


def deleteData():
    try:
        cnx = mysql.connector.connect(user=API_USERNAME, password=API_PASS, host='127.0.0.1', database='Inventory')
        Cursor = cnx.cursor()
        ProductCode = st.number_input("Enter Product Code to be deleted from the Sales : ")
        Qry =("""DELETE FROM Sales WHERE ProductCode = %s""")
        del_rec = (ProductCode,)
        Cursor.execute(Qry, del_rec)
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
        ProductCode = st.number_input("Enter Product Code to be searched from the Sales : ")
        query = ("SELECT * FROM Sales where ProductCode = %s")
        rec_srch = (ProductCode,)
        Cursor.execute(query, rec_srch)
        Rec_count = 0
        for(ProductCode, ProductName, SalesDate, SalesPrice) in Cursor:
            Rec_count += 1
            st.text("=============================================================")
            st.text("Product Code : ", ProductCode)
            st.text("Product Name : ", ProductName)
            st.text("Date of Sale : ", SalesDate)
            st.text("Sale Price : ", SalesPrice)
            st.text("=============================================================")
            if Rec_count%2 == 0:
                st.number_input("Press any key to continue: ")
                clrscreen()
                st.text(Rec_count, "Record(s) found")
        cnx.commit()
        Cursor.close()
        cnx.close()
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            st.text("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            st.text("Database does not exist")
        else:
            st.text(err)
        cnx.close()


def updateData():
    try:
        cnx = mysql.connector.connect(user=API_USERNAME, password=API_PASS, host='127.0.0.1', database='Inventory')
        Cursor = cnx.cursor()
        ProductCode = st.number_input("Enter Product Code to be updated from the Sales : ", step = 1)
        query = ("SELECT * FROM Sales WHERE ProductCode = %s")
        rec_srch = (ProductCode,)
        st.text("Enter new data")
        ProductName = st.text_input("Enter Product Name : ")
        SalesDate = st.date_input("Enter Date of Sale : ")
        SalesPrice = st.number_input("Enter Sales Price : ", step = 1
        )
        Qry = ("UPDATE Sales SET ProductName=%s, SalesDate=%s, SalesPrice=%s WHERE ProductCode=%s")
        data = (ProductName, SalesDate, SalesPrice, ProductCode)
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
            st.text(err)
    cnx.close()