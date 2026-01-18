import pandas as pd
from config import getConnection

def LoadProducts(df):
 try:
    con = getConnection()
    cursor = con.cursor() 
 
    for _, row in df.iterrows():
      cursor.execute("""
       INSERT INTO products(ProductID, Name, Category, Price)
       VALUES (?,?,?,?)
      """, row['ProductID'], row['Name'], row['Category'], row['Price'])

    con.commit()
    cursor.close()
    con.close()

 except Exception as e:
   print(f"COnnection failed. {e}")