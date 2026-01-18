import pandas as pd
from config import getConnection

def LoadCustomers(df):
 try:
    con = getConnection()
#   print("Connection successfully established")

    cursor = con.cursor() 
  
    for _, row in df.iterrows():
      cursor.execute("""
        INSERT INTO customers(CustomerID, FirstName, LastName, Country)
           VALUES(?, ?, ?, ?)
      """, row['CustomerID'], row['FirstName'], row['LastName'], row['Country'])

    con.commit()
    cursor.close()
    con.close()

 except Exception as e:
   print(f"COnnection failed. {e}")