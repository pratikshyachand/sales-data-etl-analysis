import pandas as pd

def TransformCustomers(df_raw):

   df = df_raw[['CustomerID', 'FirstName', 'LastName', 'Country']].copy()

   # the commented out below lines of code is for understanding dataset before cleaning/conversion
   '''print(df.head(10)) #returns top 10 rows
   df.info()  # returns structure of dataset
   print(df.isnull().sum()) #calulates total nulls in a column
   print(df.isna().sum())  #calculates total N/A in a column
   print(df.duplicated(subset="CustomerID").sum()) #calulates total duplicate values in CustomerID'''
    
   for col in ['FirstName', 'LastName', 'Country']:
       df[col] = df[col].str.strip().str.title()

#    print(df.head(10))
#    df.info()

   return df

    


