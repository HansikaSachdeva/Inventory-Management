#PYTHN MODULE: MENULIB
import Purchases
import Sales
import Inventory
import streamlit as st

def MenuPurchases():

    Purchases.clrscreen()
    st.text("\t\t\t Purchase Record Management\n")
    st.text("=================================================================")
    st.text("1. Add Purchase Record")
    st.text("2. Search Purchase Record")
    st.text("3. Delete Purchase Record")
    st.text("4. Update Purchase Record")
    st.text("=================================================================")
    choice = st.number_input("Enter Choice between 1 to 4 -------> : ")
    if choice == 0:
        st.text(" ")
    if choice == 1:
        Purchases.insertData()
    elif choice == 2:
        Purchases.searchData()
    elif choice == 3:
        Purchases.deleteData()
    elif choice == 4:
        Purchases.updateData()
    else:
        st.text("Wrong Choice.....Enter Your Choice again")
        

def MenuSales():
    Purchases.clrscreen()
    st.text("\t\t\t Sales Record Management\n")
    st.text("=================================================================")
    st.text("1. Add Sales Record")
    st.text("2. Search Sales Record")
    st.text("3. Delete Sales Record")
    st.text("4. Update Sales Record")
    st.text("=================================================================")
    choice = st.number_input("Enter Choice between 1 to 4 ------> : ")
    if choice == 0:
        st.text("")
    if choice == 1:
        Sales.insertData()
    elif choice == 2:
        Sales.searchData()
    elif choice == 3:
        Sales.deleteData()
    elif choice == 4:
        Sales.updateData()
    else:
        st.text("Wrong Choice.....Enter Your Choice again")
       

def MenuInventory():
    Purchases.clrscreen()
    st.text("\t\t\t Inventory Record Management\n")
    st.text("=================================================================")
    st.text("1. Search from Inventory")
    Inventory.searchData()