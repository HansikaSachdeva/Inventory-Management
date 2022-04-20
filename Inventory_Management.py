#Project on Inventory Management System
#Author : Sanjeet
#--------------------------------------------------------------------------------
#MODULE : INVENTORY MANAGEMENT
import Database
import Purchases
import Menulib
import streamlit as st

Database.DatabaseCreate()
Database.TablesCreate()

menu = ["Purchase Management","Sales Management", "Inventory Management" ]
choice = st.sidebar.radio("Menu",menu)

if choice == "Purchase Management":
    Menulib.MenuPurchases()
elif choice == "Sales Management":
    Menulib.MenuSales()
elif choice == "Inventory Management":
    Menulib.MenuInventory()
