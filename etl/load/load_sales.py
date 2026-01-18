import pandas as pd
from config import getConnection

def LoadSales(df):
 try:
    con = getConnection()
    cursor = con.cursor() 
   
    for _, row in df.iterrows():
      cursor.execute("""
       INSERT INTO sales(OrderID, CustomerID, ProductID, OrderDate, Quantity, UnitPrice, SalesAmount)
       VALUES (?,?,?,?,?,?,?)
      """, row['OrderID'], row['CustomerID'], row['ProductID'], row['OrderDate'], row['Quantity'], row['UnitPrice'], row['SalesAmount'])

    con.commit()
    cursor.close()
    con.close()

 except Exception as e:
   print(f"Connection failed. {e}")