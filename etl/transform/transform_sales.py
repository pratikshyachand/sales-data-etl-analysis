import pandas as pd

def TransformSales(df_raw):

    # select only required columns
    df = df_raw[['OrderID', 'CustomerID', 'ProductID', 'OrderDate', 'Quantity', 'UnitPrice', 'SalesAmount' ]].copy()

    # the commented out below lines of code is for understanding dataset before cleaning/conversion
    '''print(df.head(10))
    df.info()
    print(df.isnull().sum())
    print(df.isna().sum())
    print(df.duplicated(subset="OrderID").sum())'''

    # Handle missing values
    df_products = pd.read_csv("data/products.csv")
    df = df.merge(df_products[['ProductID', 'Price']], on="ProductID", how="left")
    df['UnitPrice'] = df['UnitPrice'].fillna(df['Price'])
    df['SalesAmount'] = df['UnitPrice'] * df['Quantity']

    # Handle data types
    df['OrderDate'] = pd.to_datetime(df['OrderDate'], format = "%m/%d/%Y")

    # df.info()
    # print(df.head(10))

    return df

