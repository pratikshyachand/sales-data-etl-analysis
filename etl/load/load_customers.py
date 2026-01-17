import pandas as pd
from config import getConnection

def LoadCustomers(df):
 try:
    con = getConnection()
#   print("Connection successfully established")

    cursor = con.cursor() 
  
# ---- Customers ETL ----

    df_customers = pd.read_csv('data/customers.csv')
    df_customers = df_customers[['CustomerID', 'FirstName', 'LastName', 'Country']]


    df_customers.drop_duplicates(inplace=True)

    for _, row in df_customers.iterrows():
      cursor.execute("""
        INSERT INTO customers(CustomerID, FirstName, LastName, Country)
           VALUES(?, ?, ?, ?)
      """, row['CustomerID'], row['FirstName'], row['LastName'], row['Country'])


    con.commit()
    cursor.close()
    con.close()


 except Exception as e:
   print(f"COnnection failed. {e}")